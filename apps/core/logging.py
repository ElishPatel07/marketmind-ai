"""
Centralized application logging configuration.
"""

import sys

from loguru import logger


def patch_request_id(record):
    """
    Ensure request_id always exists.
    """

    if "request_id" not in record["extra"]:
        record["extra"]["request_id"] = "system"

    return record


def configure_logging():
    """
    Configure structured application logging.
    """

    # Remove default logger
    logger.remove()

    # Patch logger records globally
    patched_logger = logger.patch(patch_request_id)

    # Console logger configuration
    patched_logger.add(
        sys.stdout,
        level="INFO",
        format=(
            "{time:YYYY-MM-DD HH:mm:ss} | {level} | {extra[request_id]} | {message}"
        ),
        colorize=True,
    )

    return patched_logger
