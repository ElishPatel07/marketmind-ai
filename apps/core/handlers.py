"""
Global exception handlers.

These handlers:
- centralize API errors
- standardize responses
- improve observability
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from loguru import logger

from apps.core.exceptions import (
    ArticleNotFoundException,
    DatabaseOperationException,
)


def register_exception_handlers(
    app: FastAPI,
):
    """
    Register all global exception handlers.
    """

    @app.exception_handler(ArticleNotFoundException)
    async def article_not_found_handler(
        request: Request,
        exc: ArticleNotFoundException,
    ):
        """
        Handle article not found exceptions.
        """

        request_logger = logger.bind(request_id=request.state.request_id)

        request_logger.warning(f"Article not found: {exc.message}")

        return JSONResponse(
            status_code=404,
            content={
                "error": "ARTICLE_NOT_FOUND",
                "message": exc.message,
            },
        )

    @app.exception_handler(DatabaseOperationException)
    async def database_exception_handler(
        request: Request,
        exc: DatabaseOperationException,
    ):
        """
        Handle database operation failures.
        """
        request_logger = logger.bind(request_id=request.state.request_id)

        request_logger.error(f"Database operation failed: {exc.message}")

        return JSONResponse(
            status_code=500,
            content={
                "error": "DATABASE_OPERATION_FAILED",
                "message": exc.message,
            },
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ):
        """
        Catch unexpected application exceptions.
        """

        request_logger = logger.bind(request_id=request.state.request_id)
        request_logger.exception("Unhandled application exception")

        return JSONResponse(
            status_code=500,
            content={
                "error": "INTERNAL_SERVER_ERROR",
                "message": "Unexpected server error occurred",
            },
        )
