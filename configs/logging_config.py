"""
Centralized logging configuration.

Production systems rely heavily on structured logging for:
- debugging
- observability
- monitoring
- incident response
- auditing

This logger outputs:
- colored console logs
- rotating log files
"""

import sys

from loguru import logger

# Remove default logger configuration
logger.remove()

# Console logger
logger.add(
    sys.stdout,
    # Structured log format
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} | {message}"
    ),
    level="INFO",
    colorize=True,
)

# Persistent file logger
logger.add(
    "logs/app.log",
    # Rotate log file after size limit
    rotation="10 MB",
    # Keep logs for 10 days
    retention="10 days",
    # Compress old logs
    compression="zip",
    level="INFO",
)
