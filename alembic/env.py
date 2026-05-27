import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context
from apps.db.base import Base

# Import ORM models so Alembic detects metadata
from apps.db.models.news_article import NewsArticle  # noqa: F401
from configs.settings import settings

# Alembic configuration object
config = context.config

# Dynamically select database URL
database_url = os.getenv(
    "TEST_DATABASE_URL",
    settings.DATABASE_URL,
)

# Alembic requires sync driver
database_url = database_url.replace(
    "postgresql+asyncpg",
    "postgresql",
)

config.set_main_option(
    "sqlalchemy.url",
    database_url,
)
if database_url:
    config.set_main_option(
        "sqlalchemy.url",
        database_url,
    )

# Configure Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# SQLAlchemy metadata for autogeneration
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """
    Run migrations in offline mode.
    """

    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    Run migrations in online mode.
    """

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
