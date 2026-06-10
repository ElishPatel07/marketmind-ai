"""
Centralized application logging configuration.
"""

import sys

from loguru import logger

from configs.settings import settings


def patch_request_id(record):
    """
    Ensure request_id always exists.
    """

    record["extra"].setdefault(
        "request_id",
        "system",
    )

    return record


def configure_logging():
    """
    Configure structured application logging.
    """

    logger.remove()

    logger.add(
        sys.stdout,
        level=("DEBUG" if settings.APP_ENV == "development" else "INFO"),
        format=("{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"),
        colorize=(not settings.LOG_JSON_FORMAT),
        serialize=(settings.LOG_JSON_FORMAT),
    )

    return logger
