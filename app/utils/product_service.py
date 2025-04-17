import httpx
from fastapi import HTTPException

PRODUCT_SERVICE_URL = "http://localhost:8000/products/"

async def get_product(product_id: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{PRODUCT_SERVICE_URL}{product_id}")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError:
            raise HTTPException(
                status_code=404,
                detail=f"Product {product_id} not found in Product Service"
            )