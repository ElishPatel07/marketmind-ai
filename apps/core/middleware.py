"""
Application middleware.

Middleware handles:
- request tracing
- correlation IDs
- request timing
- request lifecycle logging
"""

import time
import uuid

from fastapi import Request
from starlette.middleware.base import (
    BaseHTTPMiddleware,
)


class RequestContextMiddleware(BaseHTTPMiddleware):
    """
    Middleware for request tracing and observability.
    """

    async def dispatch(
        self,
        request: Request,
        call_next,
    ):
        """
        Process incoming request.
        """

        # Generate unique request correlation ID
        request_id = str(uuid.uuid4())

        # Attach request ID to request state
        request.state.request_id = request_id

        # Record request start time
        start_time = time.perf_counter()

        # Process downstream request
        response = await call_next(request)

        # Calculate request duration
        process_time = time.perf_counter() - start_time

        # Add tracing headers to response
        response.headers["X-Request-ID"] = request_id

        response.headers["X-Process-Time"] = f"{process_time:.4f}"

        return response
