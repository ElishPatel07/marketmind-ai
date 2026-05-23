"""
Database session management.

This module is responsible for:
- creating async database engine
- creating async database sessions
- providing reusable DB dependencies

FastAPI dependency injection will use get_db()
inside API routes.
"""

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from configs.settings import settings

# Create async SQLAlchemy engine
# echo=False disables verbose SQL logs
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
    future=True,
)

# Session factory for creating async DB sessions
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    """
    Dependency injected database session.

    Each request receives its own DB session.

    FastAPI automatically handles cleanup after request completion.
    """

    async with AsyncSessionLocal() as session:
        yield session
