from pydantic import BaseModel
from typing import List
from app.models.order import OrderItem
from enum import Enum

class OrderCreate(BaseModel):
    user_id: str
    items: List[OrderItem]
    
class OrderStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class OrderStatusUpdate(BaseModel):
    status: OrderStatus 

class OrderResponse(OrderCreate):
    id: str
    total_price: float
    status: str