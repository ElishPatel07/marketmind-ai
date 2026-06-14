from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.db.models.alert import Alert


class AlertRepository:
    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

    async def create_alert(
        self,
        ticker: str,
        severity: str,
        alert_type: str,
        message: str,
    ):
        alert = Alert(
            ticker=ticker,
            severity=severity,
            alert_type=alert_type,
            message=message,
        )

        self.db.add(alert)

        await self.db.commit()

        await self.db.refresh(alert)

        return alert

    async def get_alerts(
        self,
    ):
        result = await self.db.execute(select(Alert))

        return result.scalars().all()
