from pydantic import BaseModel


class ResearchRequest(BaseModel):
    query: str


class ResearchResponse(BaseModel):
    query: str

    themes: list[str]

    risks: list[str]

    opportunities: list[str]

    outlook: str

    report: str
