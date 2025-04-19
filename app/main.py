from fastapi import FastAPI
from app.database import lifespan as db_lifespan
from app.routers.order import router as order_router 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(lifespan=db_lifespan)

app.include_router(order_router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "OK"}