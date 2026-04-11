# Student Portfolio API - Quick Reference

## Base URL
```
http://localhost:8000/api
```

## Authentication
All endpoints (except auth) require: `Authorization: Bearer {token}`

## Endpoints at a Glance

### 🔐 Authentication
| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/register` | Register new user |
| POST | `/login` | Login & get token |

### 👤 Users
| Method | Endpoint | Auth | Admin |
|--------|----------|------|-------|
| GET | `/users/me` | Yes | No |
| GET | `/users/` | Yes | Yes |
| GET | `/users/{id}` | Yes | Yes |
| DELETE | `/users/{id}` | Yes | Yes |

### 📋 Items
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/items/` | List all items |
| POST | `/items/` | Create item |
| GET | `/items/{id}` | Get item |
| PUT | `/items/{id}` | Update item |
| DELETE | `/items/{id}` | Delete item |

---

## Quick Examples

### Register
```bash
curl -X POST "http://localhost:8000/api/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john",
    "name": "John Doe",
    "password": "pass123"
  }'
```

### Login (Save the token!)
```bash
curl -X POST "http://localhost:8000/api/login" \
  -H "Content-Type: application/json" \
  -d '{"username":"john","password":"pass123"}'
```

### Create Item
```bash
TOKEN="your_token_here"
curl -X POST "http://localhost:8000/api/items/" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Project",
    "description": "Description"
  }'
```

### Get Items
```bash
TOKEN="your_token_here"
curl -X GET "http://localhost:8000/api/items/" \
  -H "Authorization: Bearer $TOKEN"
```

### Update Item
```bash
TOKEN="your_token_here"
curl -X PUT "http://localhost:8000/api/items/1" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Title"}'
```

### Delete Item
```bash
TOKEN="your_token_here"
curl -X DELETE "http://localhost:8000/api/items/1" \
  -H "Authorization: Bearer $TOKEN"
```

---

## Data Models

### User Request
```json
{
  "username": "john",
  "name": "John Doe",
  "password": "pass123",
  "role": "viewer"
}
```

### User Response
```json
{
  "id": 1,
  "username": "john",
  "name": "John Doe",
  "role": "viewer"
}
```

### Item Request
```json
{
  "title": "Project Title",
  "description": "Optional description"
}
```

### Item Response
```json
{
  "id": 1,
  "title": "Project Title",
  "description": "Optional description"
}
```

### Login Response
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {...}
}
```

---

## Common Status Codes
| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Created |
| 400 | Bad request (invalid input) |
| 401 | Unauthorized (no/invalid token) |
| 403 | Forbidden (insufficient permissions) |
| 404 | Not found |
| 500 | Server error |

---

## Common Errors
| Error | Cause | Solution |
|-------|-------|----------|
| "Could not validate credentials" | Invalid/expired token | Login again to get new token |
| "Admin access required" | User is not admin | Need admin role |
| "Username already registered" | Username taken | Choose different username |
| "User not found" | Invalid user ID | Check the ID and try again |
| "Item not found" | Invalid item ID | Check the ID and try again |

---

## Testing Options
1. **Swagger UI**: http://localhost:8000/api/docs
2. **REST Client**: Use vs code extension with `API_REQUESTS.rest`
3. **cURL**: Command line (examples above)
4. **Postman**: Import OpenAPI schema from `/api/openapi.json`

---

## Documentation Links
- **Full Docs**: [API_DOCUMENTATION.md](./API_DOCUMENTATION.md)
- **Setup Guide**: [README.md](./README.md)
- **Improvements**: [IMPROVEMENTS.md](./IMPROVEMENTS.md)
- **OpenAPI**: http://localhost:8000/api/openapi.json

---

## Token Tips
- Save tokens in variables for easy reuse
- Tokens last 24 hours
- Always use "Bearer" before token
- Keep tokens private
- Get new token by logging in again

---

## Development Tips
1. Use REST Client extension in VS Code for quick testing
2. Check `/api/docs` for interactive testing
3. Save frequently-used tokens in environment files
4. Read error messages carefully - they explain what went wrong
5. All responses are JSON

---

Quick Start:
1. `POST /api/register` → Create account
2. `POST /api/login` → Get token
3. `POST /api/items/` → Create item
4. `GET /api/items/` → View items
5. `PUT /api/items/{id}` → Update item
6. `DELETE /api/items/{id}` → Delete item
