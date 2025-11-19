# Chat Service API Documentation

This document provides details on the structure, setup and endpoints of the Chat Service API built with FastAPI.

## Project structure (overview)

The project is organized into modules for clear separation of concerns, following FastAPI best practices. Key folders and files:

```
configs/fastAPI/
├─ api/            # routers and API endpoints
├─ auth/           # auth adapter, manager and transport
├─ core/           # configuration and settings
├─ db/             # database models & session
├─ schemas/        # pydantic schemas
├─ main.py         # application entrypoint
├─ requirements.txt
└─ .env (copy from .env_example)
```

## Setup and installation

1. Configure environment variables

Copy the example env file into place and edit it with your values (DB URL, JWT secret, etc.):

```bash
cp .env_example .env
# then edit .env to set your values
```

2. Use the Dockerfile to build the image.

## Run the server (development)

Start the development server using Uvicorn from the `configs/fastAPI` directory. This repository uses the host 0.0.0.0 and port 8080 in its development tasks, so the example below uses the same settings:

```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

The API will be available at http://0.0.0.0:8080. Interactive documentation (Swagger UI) is available at http://0.0.0.0:8080/docs.

## Configuration

### Environment Variables

The application requires several environment variables to be set. Copy `.env_example` to `.env` and configure:

```ini
# Database Configuration
DB_OWNER_USER=your_db_user
DB_OWNER_PASSWORD=your_db_password
DB_HOST=localhost            # Database host
DB_PORT=5432                # PostgreSQL default port
APP_DB_NAME=your_database   # Database name

# Security Settings
JWT_SECRET_KEY=replace_with_a_long_random_secret  # Min 32 characters recommended
JWT_ALGORITHM=HS256         # JWT signing algorithm
ACCESS_TOKEN_EXPIRE_MINUTES=60

# CORS Configuration
ALLOWED_ORIGINS=["http://localhost:3000"]  # List of allowed origins
```

### Security Configuration

1. Generate a secure JWT secret:
   ```bash
   openssl rand -hex 32
   ```
2. Configure CORS origins in `.env` for your frontend domains

## Health check

The app exposes a simple health endpoint at `/health` that returns a small JSON payload when the service is reachable. Example using curl:

```bash
curl -s -f http://0.0.0.0:8080/health || echo "service unavailable"
```

If the service is healthy the command prints:

```json
{"status":"ok"}
```

## API Documentation

All endpoints are mounted under the `/api` prefix. Authentication uses JWT tokens.

### Base Endpoints

| Method | Route | Description | Response |
|:-------|:------|:------------|:---------|
| GET | `/` | Welcome message | `{"message": "Welcome to the Chat API"}` |
| GET | `/health` | Health check | `{"status": "ok"}` |

### Authentication

All authentication endpoints are under `/api/auth`

| Method | Endpoint | Description | Request Body | Response |
|:-------|:---------|:------------|:------------|:---------|
| POST | `/auth/login` | Email/password login | `{"email": "user@example.com", "password": "secret"}` | `{"access_token": "jwt", "token_type": "bearer"}` |
| POST | `/auth/jwt/login` | JWT token login | `{"username": "user@example.com", "password": "secret"}` | `{"access_token": "jwt", "token_type": "bearer"}` |
| POST | `/register` | Create account | `{"email": "user@example.com", "password": "secret"}` | Created user object |
| POST | `/verify` | Verify email | `{"token": "verification_token"}` | Success message |

### User Management

All user endpoints are under `/api/users`

| Method | Endpoint | Auth Required | Description | Response |
|:-------|:---------|:--------------|:------------|:---------|
| DELETE | `/me` | Yes | Delete account | `204 No Content` |
| GET | `/{id}/export` | Yes | Export user data | User data object |

### Chat Operations

All chat endpoints are under `/api/chats`

| Method | Endpoint | Request Body | Response | Description |
|:-------|:---------|:-------------|:---------|:------------|
| GET | `/conversations` | - | `{"conversations": {...}}` | List all chats |
| GET | `/{chat_id}` | - | `[{"text": "message"}]` | Get chat history |
| PATCH | `/{chat_id}` | `{"text": "question", "model": "model_name"}` | `{"text": "AI response"}` | Send question |
| PUT | `/{chat_id}` | `[{"text": "message"}]` | Imported messages | Import chat |
| DELETE | `/{chat_id}` | - | `204 No Content` | Delete chat |

### Example API Usage

1. Register a new user:
```bash
curl -X POST http://localhost:8080/api/register \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "secure_password"}'
```

2. Login and get token:
```bash
curl -X POST http://localhost:8080/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "secure_password"}'
```

3. Use the API with token:
```bash
curl http://localhost:8080/api/conversations \
  -H "Authorization: Bearer your_token_here"
```

## Security Features

1. **Authentication**
   - JWT-based token authentication
   - Email verification flow
   - Secure password hashing

2. **Rate Limiting**
   - 100 requests per minute per IP
   - Configurable rate limits per endpoint

3. **Security Headers**
   - Strict Transport Security (HSTS)
   - Content Type Options
   - Frame Options (anti-clickjacking)

4. **CORS Protection**
   - Configurable allowed origins
   - Secure cross-origin policy

## Development Tools

### Interactive Documentation
- Swagger UI: `/docs`
- ReDoc: `/redoc`

### Testing
Run the test suite:
```bash
pytest tests/ -v
```

### Code Quality
Format code with black:
```bash
black .
```

## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
