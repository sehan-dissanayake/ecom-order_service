from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.models.order import Order 
import os

MONGO_DETAILS = os.getenv("MONGODB_URL", "mongodb://root:password@localhost:27017")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.order_db

async def initialize_database():
    await init_beanie(
        database=database,
        document_models=[Order]  # We'll create this next
    )
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    await initialize_database()
    print("Connected to MongoDB!")
    yield
    # Shutdown code
    client.close()
    print("Disconnected from MongoDB!")      