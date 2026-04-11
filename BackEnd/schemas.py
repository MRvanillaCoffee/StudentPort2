from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# ==================== User Schemas ====================

class UserBase(BaseModel):
    """Base user information"""
    username: str = Field(..., min_length=3, max_length=50, description="Unique username")
    name: str = Field(..., min_length=1, max_length=255, description="Full name of user")
    role: str = Field(default="viewer", description="User role: 'admin' or 'viewer'")

class UserCreate(UserBase):
    """Schema for creating a new user"""
    password: str = Field(..., min_length=6, description="Password (minimum 6 characters)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "name": "John Doe",
                "password": "password123",
                "role": "viewer"
            }
        }

class UserLogin(BaseModel):
    """Schema for user login"""
    username: str = Field(..., description="Username")
    password: str = Field(..., description="Password")
    
    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "password123"
            }
        }

class UserResponse(UserBase):
    """User response with ID"""
    id: int
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "johndoe",
                "name": "John Doe",
                "role": "viewer"
            }
        }

class TokenResponse(BaseModel):
    """Authentication token response"""
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(default="bearer", description="Token type")
    user: UserResponse = Field(..., description="Authenticated user information")
    
    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer",
                "user": {
                    "id": 1,
                    "username": "johndoe",
                    "name": "John Doe",
                    "role": "viewer"
                }
            }
        }

# ==================== Item Schemas ====================

class ItemBase(BaseModel):
    """Base item information"""
    title: str = Field(..., min_length=1, max_length=255, description="Item title")
    description: Optional[str] = Field(None, max_length=1000, description="Item description")

class ItemCreate(ItemBase):
    """Schema for creating a new item"""
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "My Project",
                "description": "A cool project"
            }
        }

class ItemUpdate(BaseModel):
    """Schema for updating an item"""
    title: Optional[str] = Field(None, min_length=1, max_length=255, description="Item title")
    description: Optional[str] = Field(None, max_length=1000, description="Item description")
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Updated Project",
                "description": "Updated description"
            }
        }

class ItemResponse(ItemBase):
    """Item response with ID"""
    id: int
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "My Project",
                "description": "A cool project"
            }
        }

# ==================== Error Response ====================

class ErrorResponse(BaseModel):
    """Standard error response"""
    detail: str = Field(..., description="Error message")
    
    class Config:
        json_schema_extra = {
            "example": {
                "detail": "User not found"
            }
        }
