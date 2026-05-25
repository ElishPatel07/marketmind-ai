"""
Health endpoint tests.
"""

import pytest


@pytest.mark.asyncio
async def test_health_endpoint(
    async_client,
):
    """
    Validate health endpoint response.
    """

    response = await async_client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"

    assert data["database"] == "connected"

    assert "request_id" in data
