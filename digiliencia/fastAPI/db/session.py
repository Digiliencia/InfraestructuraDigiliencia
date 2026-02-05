# /db/session.py
"""
This module initializes the asynchronous database connection.

It configures the SQLAlchemy engine using settings from `core.config`,
creates the session factory, and provides the dependency used by FastAPI
routers to access the database.
"""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

# Initialize the asynchronous engine.
# 'future=True' enables SQLAlchemy 2.0 style usage.
# 'echo=False' disables SQL logging to console (set to True for local debugging only).
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
    future=True,
    pool_size=20,
    max_overflow=40,
    pool_timeout=60,
)


# Create a configured "Session" class.
# This factory generates new AsyncSession instances for each request.
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,  # Objects remain accessible after commit (required for async)
    autoflush=False,  # We manually flush/commit to control transaction boundaries
    autocommit=False,  # We manually manage transactions
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI Dependency for database sessions.

    Creates a new asynchronous database session for an incoming request
    and ensures it is closed when the request completes.

    Yields:
        AsyncSession: An active database session context.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            # In case of an unhandled error within the route,
            # we assume the session might be in a bad state.
            # The context manager usually handles rollback on exit if needed,
            # but explicit handling can be added here if custom logic is required.
            await session.rollback()
            raise
        finally:
            # The 'async with' block automatically closes the session,
            # returning the connection to the pool.
            pass
