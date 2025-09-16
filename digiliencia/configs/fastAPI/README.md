# Chat Service API Documentation

This document provides details on the structure, setup and endpoints of the Chat Service API built with FastAPI.

---

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

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables

Copy the example env file into place and edit it with your values (DB URL, JWT secret, etc.):

```bash
cp .env_example .env
# then edit .env to set your values
```

Note: the repository also contains a `configs/.env` file that can be used for local testing; ensure the values match your environment.

## Run the server (development)

Start the development server using Uvicorn from the `configs/fastAPI` directory. This repository uses the host 0.0.0.0 and port 8080 in its development tasks, so the example below uses the same settings:

```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

The API will be available at http://0.0.0.0:8080. Interactive documentation (Swagger UI) is available at http://0.0.0.0:8080/docs.

## Example `.env` values

Here is a minimal example of the variables expected by the application. A copy of this file is available as `.env_example` in this folder.

```
DB_OWNER_USER=your_db_user
DB_OWNER_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
APP_DB_NAME=your_database_name

# JWT settings
JWT_SECRET_KEY=replace_with_a_long_random_secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# CORS origins as a JSON list, e.g. ["http://localhost:3000"]
ALLOWED_ORIGINS=["http://localhost:3000"]
```

## Health check

The app exposes a simple health endpoint at `/health` that returns a small JSON payload when the service is reachable. Example using curl:

```bash
curl -s -f http://0.0.0.0:8080/health || echo "service unavailable"
```

If the service is healthy the command prints:

```json
{"status":"ok"}
```

## API Endpoints

All endpoints are mounted under the `/api` prefix by default.

### Authentication (`/auth`)

| Method | Route                    | Requires Auth | Description                                         |
| :----- | :------------------------ | :------------ | :-------------------------------------------------- |
| `POST` | `/auth/login`             | No            | Log in with email and password. Returns a token.    |
| `POST` | `/auth/logout`            | Yes           | Logs out the user.                                  |
| `POST` | `/auth/register`          | No            | Registers a new user.                               |
| `POST` | `/auth/verify/{token}`    | No            | Verifies the user's email with a token.             |
| `POST` | `/auth/forgot-password`   | No            | Starts the password recovery process.               |
| `POST` | `/auth/reset-password/{token}` | No       | Sets a new password using a token.                   |

### Users (`/users`)

| Method   | Route                 | Requires Auth | Description                                         |
| :------- | :--------------------- | :------------ | :-------------------------------------------------- |
| `GET`    | `/users/me`            | Yes           | Gets the authenticated user's data.                 |
| `PATCH`  | `/users/me`            | Yes           | Updates the authenticated user's data.              |
| `DELETE` | `/users/me`            | Yes           | Deletes the current user's account.                 |
| `GET`    | `/users/{id}/export`   | Yes           | **(Custom)** Exports the user's data.               |

### Chats and conversations

| Method  | Route                   | Requires Auth | Description                                         |
| :------ | :---------------------- | :------------ | :-------------------------------------------------- |
| `GET`   | `/api/conversations`    | Yes           | Returns the list of the user's conversations.       |
| `GET`   | `/api/chats/{chat_id}`  | Yes           | Returns the full content of a conversation.         |
| `PATCH` | `/api/chats/{chat_id}`  | Yes           | Sends a question to the chat and gets a response.   |
| `PUT`   | `/api/chats/{chat_id}`  | Yes           | Imports/replaces a complete conversation.           |
| `DELETE`| `/api/chats/{chat_id}`  | Yes           | Deletes a conversation.                             |

---

If you want, I can also:

- add a minimal example `.env_example` file to this folder,
- add a short HEALTH endpoint description or an example curl request to test the server,
- or translate the entire README to Spanish.

Finished: README updated to reflect current run configuration and practical instructions.
