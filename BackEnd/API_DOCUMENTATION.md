# Student Portfolio API Documentation

Welcome to the Student Portfolio API! This document describes all available endpoints and how to use them.

## Quick Start

### Base URL
```
http://localhost:8000/api
```

### Interactive Documentation
- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc
- **OpenAPI Schema**: http://localhost:8000/api/openapi.json

## Authentication

The API uses JWT (JSON Web Token) for authentication.

### Getting a Token
1. Register a new user with `POST /api/register`
2. Login with `POST /api/login` to get a token

### Using the Token
Include the token in your requests:
```bash
Authorization: Bearer {your_token}
```

### Token Expiration
Tokens expire after 24 hours. You'll need to login again to get a new token.

---

## API Endpoints

### ✅ Health Check

#### GET `/`
Health check endpoint to verify API is running.

**Response:**
```json
{
  "message": "Student Portfolio API",
  "status": "ok"
}
```

---

### 🔐 Authentication Endpoints

#### POST `/api/register`
Register a new user.

**Request Body:**
```json
{
  "username": "johndoe",
  "name": "John Doe",
  "password": "password123",
  "role": "viewer"
}
```

**Parameters:**
- `username` (required): Unique username (3-50 characters)
- `name` (required): Full name
- `password` (required): Password (minimum 6 characters)
- `role` (optional): "viewer" (default) or "admin" (requires admin token)

**Response:**
```json
{
  "id": 1,
  "username": "johndoe",
  "name": "John Doe",
  "role": "viewer"
}
```

**Status Codes:**
- `200`: User registered successfully
- `400`: Username already exists
- `403`: Admin access required to create admin user

**Example:**
```bash
curl -X POST "http://localhost:8000/api/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "name": "John Doe",
    "password": "password123"
  }'
```

---

#### POST `/api/login`
Authenticate a user and receive an access token.

**Request Body:**
```json
{
  "username": "johndoe",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "username": "johndoe",
    "name": "John Doe",
    "role": "viewer"
  }
}
```

**Status Codes:**
- `200`: Login successful
- `401`: Incorrect username or password

**Example:**
```bash
curl -X POST "http://localhost:8000/api/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "password123"
  }'
```

---

### 👤 User Endpoints

#### GET `/api/users/me`
Get the profile of the currently authenticated user.

**Authorization:** Required (Bearer token)

**Response:**
```json
{
  "id": 1,
  "username": "johndoe",
  "name": "John Doe",
  "role": "viewer"
}
```

**Status Codes:**
- `200`: Success
- `401`: No valid token provided

**Example:**
```bash
curl -X GET "http://localhost:8000/api/users/me" \
  -H "Authorization: Bearer {token}"
```

---

#### GET `/api/users/`
Get all users in the system. **Admin only.**

**Authorization:** Required (Bearer token, admin role)

**Response:**
```json
[
  {
    "id": 1,
    "username": "johndoe",
    "name": "John Doe",
    "role": "viewer"
  },
  {
    "id": 2,
    "username": "janedoe",
    "name": "Jane Doe",
    "role": "admin"
  }
]
```

**Status Codes:**
- `200`: Success
- `401`: No valid token
- `403`: Admin access required

**Example:**
```bash
curl -X GET "http://localhost:8000/api/users/" \
  -H "Authorization: Bearer {admin_token}"
```

---

#### GET `/api/users/{user_id}`
Get a specific user by ID. **Admin only.**

**Authorization:** Required (Bearer token, admin role)

**Path Parameters:**
- `user_id` (required): The user's ID

**Response:**
```json
{
  "id": 1,
  "username": "johndoe",
  "name": "John Doe",
  "role": "viewer"
}
```

**Status Codes:**
- `200`: User found
- `401`: No valid token
- `403`: Admin access required
- `404`: User not found

**Example:**
```bash
curl -X GET "http://localhost:8000/api/users/1" \
  -H "Authorization: Bearer {admin_token}"
```

---

#### DELETE `/api/users/{user_id}`
Delete a user. **Admin only.**

**Authorization:** Required (Bearer token, admin role)

**Path Parameters:**
- `user_id` (required): The user's ID

**Response:**
```json
{
  "message": "User deleted successfully"
}
```

**Status Codes:**
- `200`: User deleted
- `401`: No valid token
- `403`: Admin access required
- `404`: User not found

**Example:**
```bash
curl -X DELETE "http://localhost:8000/api/users/1" \
  -H "Authorization: Bearer {admin_token}"
```

---

### 📋 Item Endpoints

#### GET `/api/items/`
Get all items in the system.

**Authorization:** Required (Bearer token)

**Response:**
```json
[
  {
    "id": 1,
    "title": "My Project",
    "description": "A cool project I created"
  },
  {
    "id": 2,
    "title": "Second Project",
    "description": "Another great project"
  }
]
```

**Status Codes:**
- `200`: Success
- `401`: No valid token

**Example:**
```bash
curl -X GET "http://localhost:8000/api/items/" \
  -H "Authorization: Bearer {token}"
```

---

#### POST `/api/items/`
Create a new item.

**Authorization:** Required (Bearer token)

**Request Body:**
```json
{
  "title": "My New Project",
  "description": "A description of my project"
}
```

**Parameters:**
- `title` (required): Item title (1-255 characters)
- `description` (optional): Item description (max 1000 characters)

**Response:**
```json
{
  "id": 3,
  "title": "My New Project",
  "description": "A description of my project"
}
```

**Status Codes:**
- `200`: Item created
- `401`: No valid token

**Example:**
```bash
curl -X POST "http://localhost:8000/api/items/" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My New Project",
    "description": "A description of my project"
  }'
```

---

#### GET `/api/items/{item_id}`
Get a specific item by ID.

**Authorization:** Required (Bearer token)

**Path Parameters:**
- `item_id` (required): The item's ID

**Response:**
```json
{
  "id": 1,
  "title": "My Project",
  "description": "A cool project I created"
}
```

**Status Codes:**
- `200`: Item found
- `401`: No valid token
- `404`: Item not found

**Example:**
```bash
curl -X GET "http://localhost:8000/api/items/1" \
  -H "Authorization: Bearer {token}"
```

---

#### PUT `/api/items/{item_id}`
Update an existing item.

**Authorization:** Required (Bearer token)

**Path Parameters:**
- `item_id` (required): The item's ID

**Request Body:**
```json
{
  "title": "Updated Title",
  "description": "Updated description"
}
```

**Parameters:**
- `title` (optional): New title
- `description` (optional): New description

**Response:**
```json
{
  "id": 1,
  "title": "Updated Title",
  "description": "Updated description"
}
```

**Status Codes:**
- `200`: Item updated
- `401`: No valid token
- `404`: Item not found

**Example:**
```bash
curl -X PUT "http://localhost:8000/api/items/1" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Title"
  }'
```

---

#### DELETE `/api/items/{item_id}`
Delete an item.

**Authorization:** Required (Bearer token)

**Path Parameters:**
- `item_id` (required): The item's ID

**Response:**
```json
{
  "message": "Item deleted successfully"
}
```

**Status Codes:**
- `200`: Item deleted
- `401`: No valid token
- `404`: Item not found

**Example:**
```bash
curl -X DELETE "http://localhost:8000/api/items/1" \
  -H "Authorization: Bearer {token}"
```

---

## Error Handling

When an error occurs, the API returns a JSON response with details:

```json
{
  "detail": "Error message describing what went wrong"
}
```

### Common Error Codes
- `400`: Bad Request - Invalid input
- `401`: Unauthorized - Invalid or missing token
- `403`: Forbidden - Insufficient permissions
- `404`: Not Found - Resource doesn't exist
- `500`: Internal Server Error - Server error

---

## Quick Example: Complete Workflow

### 1. Register a new user
```bash
curl -X POST "http://localhost:8000/api/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "alice",
    "name": "Alice Smith",
    "password": "secure123"
  }'
```

**Response:**
```json
{
  "id": 1,
  "username": "alice",
  "name": "Alice Smith",
  "role": "viewer"
}
```

### 2. Login
```bash
curl -X POST "http://localhost:8000/api/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "alice",
    "password": "secure123"
  }'
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "username": "alice",
    "name": "Alice Smith",
    "role": "viewer"
  }
}
```

### 3. Create an item
```bash
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

curl -X POST "http://localhost:8000/api/items/" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Portfolio Project",
    "description": "A showcase of my work"
  }'
```

### 4. Get all items
```bash
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

curl -X GET "http://localhost:8000/api/items/" \
  -H "Authorization: Bearer $TOKEN"
```

### 5. Get your profile
```bash
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

curl -X GET "http://localhost:8000/api/users/me" \
  -H "Authorization: Bearer $TOKEN"
```

---

## Tips for Developers

1. **Use the interactive docs**: Visit http://localhost:8000/api/docs for an interactive Swagger UI where you can test endpoints directly
2. **Check token expiration**: Tokens expire after 24 hours, so save and reuse tokens during development
3. **Admin users**: Only existing admin users can create new admin users
4. **Error messages**: Read the error `detail` field for specific information about what went wrong

---

## Troubleshooting

### "Could not validate credentials"
- Token is missing or invalid
- Token has expired (get a new one by logging in)
- Make sure you're using "Bearer" before the token

### "Admin access required"
- Your user role is "viewer", not "admin"
- Contact an admin to upgrade your account

### "Username already registered"
- That username is already taken
- Choose a different username

---

## Support

For more information, check the interactive API docs at `/api/docs` or `/api/redoc`
