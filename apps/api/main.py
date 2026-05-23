"""
Main FastAPI application entry point.

This file initializes:
- FastAPI app instance
- application metadata
- startup lifecycle events
- API route registration

As the project grows, additional routers and middleware
will be registered here.
"""

from fastapi import FastAPI

# Health check router
from apps.api.routes.health import router as health_router

# Centralized logging system
from configs.logging_config import logger

# Typed application settings loaded from environment variables
from configs.settings import settings

# Initialize FastAPI application
app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)


@app.on_event("startup")
async def startup_event():
    """
    Runs once when the FastAPI application starts.

    Useful for:
    - startup logging
    - DB connection checks
    - model loading
    - cache warmup
    - background scheduler initialization
    """

    logger.info("Starting MarketMind AI API")


# Register API routers
app.include_router(health_router)


@app.get("/")
async def root():
    """
    Root endpoint.

    Used mainly for:
    - quick API verification
    - uptime checks
    - basic connectivity testing
    """

    logger.info("Root endpoint accessed")

    return {"message": f"{settings.APP_NAME} running"}
