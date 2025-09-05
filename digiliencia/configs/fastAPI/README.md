# Chat Service API Documentation

This document provides details on the structure, setup, and endpoints of the Chat Service API, built with FastAPI.

---

## Project Structure

The project is organized into modules for clear separation of concerns, following FastAPI best practices.
```
/
|-- api/
|   |-- routers/
|   |   |-- chats.py            # Endpoints for chats and conversations
|   |   +-- custom_users.py     # Custom user endpoints (delete, export)
|
|-- auth/
|   |-- db.py                   # Database adapter for FastAPI-Users
|   |-- manager.py              # User logic manager
|   +-- transport.py            # Token transport configuration (JWT)
|
|-- core/
|   +-- config.py               # Load environment variables with Pydantic
|
|-- db/
|   |-- models.py               # SQLAlchemy ORM models (E-R model reflection)
|   +-- session.py              # Async database session configuration
|
|-- schemas/
|   |-- chat.py                 # Pydantic schemas for chats
|   +-- user.py                 # Pydantic schemas for users
|
|-- .env_example                # Environment variable template
|-- main.py                     # Application entry point and middlewares
+-- requirements.txt            # Project dependencies
```

## Setup and Installation

### 1. Configure Environment
Copy the `.env_example` file to a new file named `.env` and update it with your database URL and a unique JWT secret key.

## 3. Run the Server
Start the development server using Uvicorn. The --reload flag will automatically restart the server on code changes.

```
uvicorn main:app --reload
```
The API will be available at http://127.0.0.1:8000. Interactive documentation (Swagger UI) can be accessed at http://127.0.0.1:8000/docs.

## API Endpoints

All endpoints are under the ```/api``` prefix.

### Authentication (`/auth`)

| Method | Route                    | Requires Auth | Description                                         |
| :----- | :------------------------ | :------------ | :-------------------------------------------------- |
| `POST` | `login`         | No            | Log in with email and password. Returns a token.    |
| `POST` | `/auth/logout`            | Yes           | Logs out the user.                                  |
| `POST` | `/register`               | No            | Registers a new user.                               |
| `POST` | `/verify/{token}`         | No            | Verifies the user's email with a token.             |
| `POST` | `/forgot-password`        | No            | Starts the password recovery process.               |
| `POST` | `/reset-password/{token}` | No            | Sets a new password using a token.                   |


### Users (`/users`)

| Method   | Route                 | Requires Auth | Description                                         |
| :------- | :--------------------- | :------------ | :-------------------------------------------------- |
| `GET`    | `/users/me`            | Yes           | Gets the authenticated user's data.                 |
| `PATCH`  | `/users/me`            | Yes           | Updates the authenticated user's data.              |
| `DELETE` | `/users/me`            | Yes           | Deletes the current user's account.    |
| `GET`    | `/users/{id}/export`   | Yes           | **(Custom)** Exports the user's data.               |


### Chats and Conversations

| Method  | Route                   | Requires Auth | Description                                         |
| :------ | :---------------------- | :------------ | :-------------------------------------------------- |
| `GET`   | `/conversations`        | Yes           | Returns the list of the user's conversations.       |
| `GET`   | `/chats/{chat_id}`      | Yes           | Returns the full content of a conversation.         |
| `PATCH` | `/chats/{chat_id}`      | Yes           | Sends a question to the chat and gets a response.   |
| `PUT`   | `/chats/{chat_id}`      | Yes           | Imports/replaces a complete conversation.           |
| `DELETE`| `/chats/{chat_id}`      | Yes           | Deletes a conversation.                             |
