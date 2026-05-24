"""
Health check endpoints.

Health endpoints validate:
- API availability
- database connectivity
- infrastructure readiness
"""

from fastapi import APIRouter, Depends, Request
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from apps.db.session import get_db

# Router instance
router = APIRouter()


@router.get("/health")
async def health_check(request: Request, db: AsyncSession = Depends(get_db)):  # noqa: B008
    """
    Validate API and database connectivity.
    """

    # Simple database connectivity test
    await db.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected",
        "request_id": request.state.request_id,
    }
