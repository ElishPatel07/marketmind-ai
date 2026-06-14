from apps.repositories.alert_repository import AlertRepository


class AlertService:
    def __init__(
        self,
        repository: AlertRepository,
    ):
        self.repository = repository

    async def generate_sentiment_alert(
        self,
        ticker: str,
        sentiment: str,
    ):
        if sentiment != "BEARISH":
            return None

        return await self.repository.create_alert(
            ticker=ticker,
            severity="HIGH",
            alert_type="SENTIMENT",
            message=(f"Bearish sentiment detected for {ticker}"),
        )
