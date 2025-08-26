# Chat Service API Documentation

This document provides details on the structure, setup, and endpoints of the Chat Service API, built with FastAPI.

---

## Project Structure

The project is organized into modules for clear separation of concerns, following FastAPI best practices.
```
/
|-- api/
|   |-- routers/
|   |   |-- auth.py           # Authentication & user endpoints
|   |   +-- chats.py          # Chat & conversation endpoints
|   +-- dependencies.py       # Shared dependencies (e.g., get_current_user)
|
|-- core/
|   |-- config.py             # Environment variable loading
|   +-- security.py           # Password hashing & JWT logic
|
|-- db/
|   |-- crud.py               # Database CRUD (Create, Read, Update, Delete) operations
|   |-- models.py             # SQLAlchemy ORM models
|   +-- session.py            # Database session configuration
|
|-- schemas/
|   |-- chat.py               # Pydantic schemas for chats
|   |-- token.py              # Pydantic schemas for tokens
|   +-- user.py               # Pydantic schemas for users
|
|-- .env                      # Environment variables
|-- main.py                   # Main application entry point
+-- requirements.txt          # Python project dependencies
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