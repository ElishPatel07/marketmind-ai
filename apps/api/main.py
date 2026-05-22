from fastapi import FastAPI

from apps.api.routes.health import router as health_router
from configs.logging_config import logger
from configs.settings import settings

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)


@app.on_event("startup")
async def startup_event():
    logger.info("Starting MarketMind AI API")


app.include_router(health_router)


@app.get("/")
async def root():
    logger.info("Root endpoint accessed")

    return {"message": f"{settings.APP_NAME} running"}
