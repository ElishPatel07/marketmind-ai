"""
Centralized application configuration.

This file uses Pydantic Settings to:
- load environment variables
- validate config types
- provide typed settings access

Benefits:
- centralized configuration management
- safer deployments
- easier environment switching
- improved maintainability
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from .env file.

    Every setting becomes available through:
    settings.SETTING_NAME
    """

    APP_NAME: str = "MarketMind AI"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"

    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000

    LOG_LEVEL: str = "INFO"

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    REDIS_HOST: str
    REDIS_PORT: int

    DATABASE_URL: str

    CHROMA_DB_DIR: str

    GROQ_API_KEY: str

    # Load variables from .env file
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)


# Global settings object used across the application
settings = Settings()
