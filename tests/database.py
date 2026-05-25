"""
Test database configuration.
"""

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from configs.settings import settings

# Dedicated async test engine
test_engine = create_async_engine(
    settings.TEST_DATABASE_URL,
    echo=False,
)

# Async session factory for tests
TestSessionLocal = async_sessionmaker(
    bind=test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
