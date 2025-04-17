from beanie import Document
from pydantic import BaseModel, Field
from typing import List

class OrderItem(BaseModel):
    product_id: str  # References Product Service's product ID
    quantity: int = Field(gt=0)

class Order(Document):
    user_id: str
    items: List[OrderItem]
    total_price: float
    status: str = "pending"  # pending/completed/cancelled

    class Settings:
        name = "orders"