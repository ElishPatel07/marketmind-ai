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

from apps.api.routes.chat import router as chat_router
from apps.api.routes.health import router as health_router
from apps.api.routes.intelligence import router as intelligence_router
from apps.api.routes.news import router as news_router
from apps.api.routes.portfolio import router as portfolio_router
from apps.api.routes.rag import router as rag_router
from apps.api.routes.research import router as research_router
from apps.api.routes.search import router as search_router
from apps.api.routes.system import router as system_router
from apps.core.handlers import register_exception_handlers
from apps.core.logging import configure_logging
from apps.core.middleware import RequestContextMiddleware
from apps.scheduler.scheduler import start_scheduler

# Typed application settings loaded from environment variables
from configs.settings import settings

# Initialize FastAPI application
app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

app.include_router(search_router)
app.include_router(rag_router)
app.include_router(chat_router)
app.include_router(intelligence_router)
app.include_router(system_router)
app.include_router(research_router)
app.include_router(portfolio_router)
app.add_middleware(RequestContextMiddleware)

logger = configure_logging()

register_exception_handlers(app)


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
    logger.info(f"Application environment: {settings.APP_ENV}")
    logger.info(f"JSON logging enabled: {settings.LOG_JSON_FORMAT}")

    start_scheduler()


# Register API routers
app.include_router(health_router)
app.include_router(news_router)


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
