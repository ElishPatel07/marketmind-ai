from fastapi import FastAPI

app = FastAPI(
    title="MarketMind AI",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {"message": "MarketMind AI running"}