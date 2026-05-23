"""
SQLAlchemy declarative base.

All ORM models inherit from Base.

SQLAlchemy uses Base metadata for:
- ORM mappings
- schema generation
- Alembic migrations
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all database models.
    """

    pass
