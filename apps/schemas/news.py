"""
Pydantic schemas for financial news APIs.

Schemas define:
- request validation
- response serialization
- API data contracts

Important:
Schemas are separate from SQLAlchemy ORM models.

Benefits:
- cleaner architecture
- safer API validation
- independent API evolution
- better security boundaries
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class NewsArticleCreate(BaseModel):
    """
    Schema for creating a news article.
    """

    title: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="Financial news article title",
    )

    source: str = Field(
        ...,
        min_length=2,
        max_length=255,
        description="News source name",
    )

    content: str = Field(
        ...,
        min_length=20,
        description="Full article content",
    )

    published_at: datetime | None = None

    article_url: str | None = None

    sentiment: str | None = None
    sentiment_score: float | None = None


class NewsArticleResponse(BaseModel):
    """
    Schema returned to API clients.
    """

    id: int
    title: str
    source: str
    content: str
    created_at: datetime

    # Allows conversion from ORM model -> Pydantic schema
    model_config = ConfigDict(from_attributes=True)
    published_at: datetime | None
    article_url: str | None
