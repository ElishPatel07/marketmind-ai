from pydantic import BaseModel


class PortfolioCreate(BaseModel):
    name: str

    holdings: list[str]
