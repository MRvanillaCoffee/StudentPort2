from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from fastapi.openapi.utils import get_openapi
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional, List
try:
    from . import database, models, schemas
except ImportError:
    import database
    import models
    import schemas

app = FastAPI(
    title="Student Portfolio API",
    description="API for Student Portfolio management with authentication and authorization",
    version="1.0.0",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# CORS configuration for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_db_check_and_init() -> None:
    """Ensure database is reachable before serving requests."""
    try:
        with database.engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        models.Base.metadata.create_all(bind=database.engine)
    except SQLAlchemyError as exc:
        raise RuntimeError(
            "Database startup failed. Ensure MariaDB is running and reachable at "
            f"{database.DB_HOST}:{database.DB_PORT} and that DB '{database.DB_NAME}' exists. "
            "You can create it using BackEnd/create_db.py."
        ) from exc

# Security settings
SECRET_KEY = "your-secret-key-change-this-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60  # 24 hours

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")
oauth2_scheme_optional = OAuth2PasswordBearer(tokenUrl="/api/login", auto_error=False)

def get_db():
    """Database session dependency"""
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def hash_password(password: str) -> str:
    """Hash a password"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash"""
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception:
        # Support legacy plain-text passwords already stored in DB.
        return plain_password == hashed_password

def create_access_token(data: dict, expires_delta: timedelta = None):
    """Create a JWT access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def _decode_user_from_token(token: str, db: Session):
    """Decode JWT token and return user"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Dependency to get current authenticated user"""
    return _decode_user_from_token(token, db)

def get_current_admin(current_user: models.User = Depends(get_current_user)):
    """Dependency to ensure current user is admin"""
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user

# ========================= HEALTH CHECK =========================

@app.get("/", tags=["Health"])
def read_root():
    """Health check endpoint"""
    return {"message": "Student Portfolio API", "status": "ok"}

# ========================= AUTHENTICATION =========================

@app.post(
    "/api/register",
    response_model=schemas.UserResponse,
    tags=["Authentication"],
    summary="Register a new user",
    responses={
        200: {"description": "User registered successfully"},
        400: {"description": "Username already exists"},
        403: {"description": "Admin access required to create admin user"},
    }
)
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
    token: Optional[str] = Depends(oauth2_scheme_optional),
):
    """
    Register a new user.
    
    - **Public registration**: Users can register as 'viewer' without authentication
    - **Admin registration**: Creating 'admin' users requires an existing admin token
    """
    # Public registration is allowed only for viewer role.
    if user.role == "admin":
        if not token:
            raise HTTPException(status_code=403, detail="Admin access required to create admin user")
        requester = _decode_user_from_token(token, db)
        if requester.role != "admin":
            raise HTTPException(status_code=403, detail="Admin access required to create admin user")

    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = hash_password(user.password)
    db_user = models.User(
        username=user.username,
        name=user.name,
        password=hashed_password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post(
    "/api/login",
    response_model=schemas.TokenResponse,
    tags=["Authentication"],
    summary="Login with username and password",
    responses={
        200: {"description": "Login successful"},
        401: {"description": "Incorrect username or password"},
    }
)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    Authenticate user and return JWT token.
    
    Use the returned token in the Authorization header as "Bearer {token}"
    """
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user.username}, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": db_user
    }

# ========================= USERS =========================

@app.get(
    "/api/users/me",
    response_model=schemas.UserResponse,
    tags=["Users"],
    summary="Get current user profile"
)
def get_current_user_info(current_user: models.User = Depends(get_current_user)):
    """Get the profile of the currently authenticated user"""
    return current_user

@app.get(
    "/api/users/",
    response_model=List[schemas.UserResponse],
    tags=["Users"],
    summary="List all users (admin only)",
    responses={
        200: {"description": "List of users"},
        403: {"description": "Admin access required"},
    }
)
def read_users(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin),
):
    """Get all users in the system (admin only)"""
    return db.query(models.User).all()

@app.get(
    "/api/users/{user_id}",
    response_model=schemas.UserResponse,
    tags=["Users"],
    summary="Get user by ID (admin only)",
    responses={
        200: {"description": "User found"},
        404: {"description": "User not found"},
        403: {"description": "Admin access required"},
    }
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin),
):
    """Get a specific user by ID (admin only)"""
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete(
    "/api/users/{user_id}",
    tags=["Users"],
    summary="Delete user (admin only)",
    responses={
        200: {"description": "User deleted successfully"},
        404: {"description": "User not found"},
        403: {"description": "Admin access required"},
    }
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin),
):
    """Delete a specific user (admin only)"""
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

# ========================= ITEMS =========================

@app.get(
    "/api/items/",
    response_model=List[schemas.ItemResponse],
    tags=["Items"],
    summary="List all items (authenticated)"
)
def read_items(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Get all items in the system (requires authentication)"""
    return db.query(models.Item).all()

@app.post(
    "/api/items/",
    response_model=schemas.ItemResponse,
    tags=["Items"],
    summary="Create a new item",
    responses={
        201: {"description": "Item created successfully"},
        401: {"description": "Unauthorized"},
    }
)
def create_item(
    item: schemas.ItemCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Create a new item (requires authentication)"""
    db_item = models.Item(title=item.title, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get(
    "/api/items/{item_id}",
    response_model=schemas.ItemResponse,
    tags=["Items"],
    summary="Get item by ID",
    responses={
        200: {"description": "Item found"},
        404: {"description": "Item not found"},
        401: {"description": "Unauthorized"},
    }
)
def get_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Get a specific item by ID (requires authentication)"""
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put(
    "/api/items/{item_id}",
    response_model=schemas.ItemResponse,
    tags=["Items"],
    summary="Update an item",
    responses={
        200: {"description": "Item updated successfully"},
        404: {"description": "Item not found"},
        401: {"description": "Unauthorized"},
    }
)
def update_item(
    item_id: int,
    item_update: schemas.ItemUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Update an existing item (requires authentication)"""
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    if item_update.title is not None:
        db_item.title = item_update.title
    if item_update.description is not None:
        db_item.description = item_update.description
    
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete(
    "/api/items/{item_id}",
    tags=["Items"],
    summary="Delete an item",
    responses={
        200: {"description": "Item deleted successfully"},
        404: {"description": "Item not found"},
        401: {"description": "Unauthorized"},
    }
)
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Delete an item (requires authentication)"""
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}
