"""
Shared pytest fixtures.
"""

import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from apps.api.main import app
from tests.database import TestSessionLocal


@pytest_asyncio.fixture
async def async_client():
    """
    Async FastAPI test client.
    """

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        yield client


@pytest_asyncio.fixture
async def db_session():
    """
    Isolated async database session.
    """

    async with TestSessionLocal() as session:
        try:
            yield session

        finally:
            await session.rollback()
            await session.close()
