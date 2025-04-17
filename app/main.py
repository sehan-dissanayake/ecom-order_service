from fastapi import FastAPI
from app.database import lifespan as db_lifespan
from app.routers import order 

app = FastAPI(lifespan=db_lifespan)

app.include_router(order.router)

@app.get("/health")
async def health_check():
    return {"status": "OK"}