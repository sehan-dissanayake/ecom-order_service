import httpx
from fastapi import HTTPException
import os

PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL")

async def get_product(product_id: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{PRODUCT_SERVICE_URL}products/{product_id}")
            print(PRODUCT_SERVICE_URL)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError:
            raise HTTPException(
                status_code=404,
                detail=f"Product {product_id} not found in Product Service"
            )