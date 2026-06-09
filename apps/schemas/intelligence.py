from pydantic import BaseModel


class IntelligenceSummary(BaseModel):
    total_articles: int
    bullish: int
    bearish: int
    neutral: int
