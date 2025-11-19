# /db/session.py
"""
This module is responsible for setting up the asynchronous database connection.

It initializes the SQLAlchemy async engine, creates a session factory for
generating new database sessions, and provides a FastAPI dependency (`get_db`)
for injecting sessions into API route functions.
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings

# The asynchronous database engine is the core interface to the database.
# It is configured once using the DATABASE_URL from the application settings.
# `echo=True` logs all generated SQL statements, which is useful for debugging.
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# A factory for creating new AsyncSession objects. This is the primary way
# the application will interact with the database. The settings ensure that
# sessions behave correctly in an async environment.
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,  # Prevents SQLAlchemy from expiring objects after commit
    autocommit=False,  # Transactions are managed manually with `await session.commit()`
    autoflush=False,  # Changes are not automatically sent to the DB
)

# A declarative base class used by all SQLAlchemy ORM models.
# Although defined here, models in `db/models.py` will inherit from this Base.
Base = declarative_base()


async def get_db() -> AsyncSession:
    """
    FastAPI dependency to provide a database session for a single request.

    This function is a generator that yields a new `AsyncSession` for each
    incoming API request. It uses a context manager (`async with`) to ensure
    that the session is always closed properly after the request is finished,
    even if errors occur.

    Yields:
        AsyncSession: An active, asynchronous database session.
    """
    async with AsyncSessionLocal() as session:
        yield session
