# Student Portfolio API

A FastAPI-based REST API for Student Portfolio management with authentication and authorization.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup

1. **Create virtual environment** (if not already created)
   ```bash
   python -m venv .venv
   ```

2. **Activate virtual environment**
   ```bash
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the API**
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

### Interactive Documentation (Choose One)
- **Swagger UI** (Recommended): http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc
- **OpenAPI Schema**: http://localhost:8000/api/openapi.json

### Detailed Documentation
See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for complete endpoint reference with examples.

## 🧪 Testing the API

### Option 1: Using REST Client in VS Code (Recommended)
1. Install [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
2. Open [API_REQUESTS.rest](API_REQUESTS.rest)
3. Click "Send Request" above any request

### Option 2: Using cURL
```bash
# Register
curl -X POST "http://localhost:8000/api/register" \
  -H "Content-Type: application/json" \
  -d '{"username":"john","name":"John Doe","password":"pass123"}'

# Login
curl -X POST "http://localhost:8000/api/login" \
  -H "Content-Type: application/json" \
  -d '{"username":"john","password":"pass123"}'

# Get your profile (replace TOKEN with actual token)
curl -X GET "http://localhost:8000/api/users/me" \
  -H "Authorization: Bearer TOKEN"
```

### Option 3: Using Swagger UI
1. Go to http://localhost:8000/api/docs
2. Click "Try it out" on any endpoint
3. Fill in the parameters and click "Execute"

## 📋 API Overview

### 🔐 Authentication
- **POST `/api/register`** - Register a new user
- **POST `/api/login`** - Login and get JWT token

### 👤 User Management
- **GET `/api/users/me`** - Get current user profile
- **GET `/api/users/`** - List all users (admin only)
- **GET `/api/users/{id}`** - Get specific user (admin only)
- **DELETE `/api/users/{id}`** - Delete user (admin only)

### 📦 Items
- **GET `/api/items/`** - List all items
- **POST `/api/items/`** - Create new item
- **GET `/api/items/{id}`** - Get specific item
- **PUT `/api/items/{id}`** - Update item
- **DELETE `/api/items/{id}`** - Delete item

All item endpoints require authentication.

## � Endpoints Details

### 🔐 Authentication Endpoints

#### POST `/api/register`
**Purpose**: Register a new user account
- **Who can use**: Anyone (public)
- **Input**: username, name, password, role (optional)
- **Returns**: User object with ID
- **Roles**: Creates viewer by default (admin requires existing admin token)

#### POST `/api/login`
**Purpose**: Authenticate user and receive JWT token
- **Who can use**: Anyone with valid credentials
- **Input**: username, password
- **Returns**: JWT token + user information
- **Token Duration**: 24 hours
- **Use This For**: Getting access token for all other requests

---

### 👤 User Management Endpoints

#### GET `/api/users/me`
**Purpose**: Get the profile of the currently logged-in user
- **Who can use**: Any authenticated user
- **Authentication**: Required (Bearer token)
- **Input**: None
- **Returns**: Current user's information (id, username, name, role)
- **Use This For**: Displaying logged-in user profile, checking user role

#### GET `/api/users/`
**Purpose**: Get list of all users in the system
- **Who can use**: Admin only
- **Authentication**: Required (Bearer token + admin role)
- **Input**: None
- **Returns**: Array of all users
- **Use This For**: Admin dashboard, managing all users

#### GET `/api/users/{user_id}`
**Purpose**: Get information about a specific user
- **Who can use**: Admin only
- **Authentication**: Required (Bearer token + admin role)
- **Input**: user_id (user's ID number)
- **Returns**: Specific user's information
- **Use This For**: Viewing user details, user management page

#### DELETE `/api/users/{user_id}`
**Purpose**: Delete a user from the system
- **Who can use**: Admin only
- **Authentication**: Required (Bearer token + admin role)
- **Input**: user_id (user's ID number)
- **Returns**: Success message
- **Use This For**: Admin removing users, account deletion

---

### 📦 Item (Portfolio) Endpoints

#### GET `/api/items/`
**Purpose**: Get list of all portfolio items
- **Who can use**: Any authenticated user
- **Authentication**: Required (Bearer token)
- **Input**: None
- **Returns**: Array of all items (id, title, description)
- **Use This For**: Displaying portfolio list, dashboard overview

#### POST `/api/items/`
**Purpose**: Create a new portfolio item
- **Who can use**: Any authenticated user
- **Authentication**: Required (Bearer token)
- **Input**: title, description (optional)
- **Returns**: Newly created item with ID
- **Use This For**: Adding new project/item to portfolio

#### GET `/api/items/{item_id}`
**Purpose**: Get details of a specific portfolio item
- **Who can use**: Any authenticated user
- **Authentication**: Required (Bearer token)
- **Input**: item_id (item's ID number)
- **Returns**: Specific item's information
- **Use This For**: View detailed item information, portfolio detail page

#### PUT `/api/items/{item_id}`
**Purpose**: Update/edit an existing portfolio item
- **Who can use**: Any authenticated user
- **Authentication**: Required (Bearer token)
- **Input**: item_id + (title and/or description to update)
- **Returns**: Updated item information
- **Use This For**: Editing project title or description, updating portfolio

#### DELETE `/api/items/{item_id}`
**Purpose**: Delete a portfolio item
- **Who can use**: Any authenticated user
- **Authentication**: Required (Bearer token)
- **Input**: item_id (item's ID number)
- **Returns**: Success message
- **Use This For**: Removing item from portfolio

---

### 🏥 Health Check

#### GET `/`
**Purpose**: Check if API is running
- **Who can use**: Anyone
- **Authentication**: Not required
- **Input**: None
- **Returns**: Status message
- **Use This For**: Monitoring, health checks

## �🔑 Authentication

The API uses JWT (JSON Web Token) for secure authentication.

### How to Authenticate
1. Call `POST /api/login` with username and password
2. You'll receive an `access_token` in the response
3. Include the token in all subsequent requests:
   ```
   Authorization: Bearer {your_token}
   ```

### Token Details
- **Duration**: 24 hours
- **Renewal**: Call login again to get a new token

## 📊 Data Models

### User
```json
{
  "id": 1,
  "username": "john_doe",
  "name": "John Doe",
  "role": "viewer|admin"
}
```

### Item
```json
{
  "id": 1,
  "title": "Project Title",
  "description": "Project description"
}
```

## 🎯 Common Use Cases

### Register and Login
```bash
# 1. Register
curl -X POST "http://localhost:8000/api/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "alice",
    "name": "Alice Smith",
    "password": "secure123"
  }'

# 2. Login (save the token!)
curl -X POST "http://localhost:8000/api/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "alice",
    "password": "secure123"
  }'
```

### Create and View Items
```bash
# Create item
curl -X POST "http://localhost:8000/api/items/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Portfolio",
    "description": "Showcase of my work"
  }'

# Get all items
curl -X GET "http://localhost:8000/api/items/" \
  -H "Authorization: Bearer YOUR_TOKEN"

# Get specific item
curl -X GET "http://localhost:8000/api/items/1" \
  -H "Authorization: Bearer YOUR_TOKEN"

# Update item
curl -X PUT "http://localhost:8000/api/items/1" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Title"}'

# Delete item
curl -X DELETE "http://localhost:8000/api/items/1" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## 🔒 Security Features

- ✅ JWT-based authentication
- ✅ Password hashing with bcrypt
- ✅ Role-based access control (admin/viewer)
- ✅ CORS configuration for frontend integration
- ✅ Input validation on all endpoints
- ✅ Secure password verification

## ⚡ Performance Tips

1. **Reuse tokens**: Don't login on every request
2. **Use REST Client**: Faster testing than Postman
3. **Filter results**: Use pagination for large datasets (coming soon)

## 🆕 What's New in This Version

### Improved API Design
- ✨ **Auto-generated documentation** with Swagger UI and ReDoc
- ✨ **Detailed endpoint descriptions** and examples
- ✨ **Better error messages** with clear status codes
- ✨ **Tags for organization** (Authentication, Users, Items)

### New Endpoints Added
- ✨ `GET /api/users/{id}` - Get specific user (admin)
- ✨ `POST /api/items/` - Create new item
- ✨ `GET /api/items/{id}` - Get specific item
- ✨ `PUT /api/items/{id}` - Update item (new!)
- ✨ `DELETE /api/items/{id}` - Delete item (new!)

### Better Documentation
- 📚 `API_DOCUMENTATION.md` - Complete endpoint reference
- 🧪 `API_REQUESTS.rest` - Ready-to-use REST client requests
- 📖 `README.md` (this file) - Quick start guide

### Enhanced Schemas
- 🏷️ Field descriptions and constraints
- 📝 JSON schema examples
- ✔️ Input validation

## 🐛 Troubleshooting

### "Could not validate credentials"
- Check your token is valid and not expired
- Make sure you're using the correct format: `Bearer {token}`
- Login again to get a fresh token

### "Admin access required"
- Your user needs admin role
- Ask an existing admin to upgrade your account

### API won't start
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check the database connection
- Try removing old `.db` files and restart

## 📁 Project Structure

```
BackEnd/
├── main.py                 # Main API file with all endpoints
├── models.py              # Database models
├── schemas.py             # Pydantic request/response schemas
├── database.py            # Database configuration
├── requirements.txt       # Python dependencies
├── API_DOCUMENTATION.md   # Complete API reference
├── API_REQUESTS.rest      # REST Client test file
└── README.md             # This file
```

## 🚀 Deployment

For production deployment:
1. Change `SECRET_KEY` in `main.py` to a secure random string
2. Update CORS `allow_origins` with your frontend URL
3. Use a production database (MariaDB/MySQL)
4. Use a production server like Gunicorn

## 📞 Support

For issues or questions:
1. Check the documentation at `/api/docs`
2. Review detailed examples in `API_DOCUMENTATION.md`
3. Test with `API_REQUESTS.rest` file

## 📜 License

This project is part of the Student Portfolio application.
