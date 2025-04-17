from fastapi import APIRouter, HTTPException
from beanie import PydanticObjectId
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderResponse, OrderStatusUpdate
from app.utils.product_service import get_product

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=Order)
async def create_order(order_data: OrderCreate):
    # Calculate total price by checking Product Service
    total_price = 0.0
    
    for item in order_data.items:
        product = await get_product(item.product_id)
        total_price += product["price"] * item.quantity
    
    # Create order document
    new_order = Order(
        **order_data.model_dump(),
        total_price=total_price
    )
    
    await new_order.insert()
    return new_order

@router.get("/", response_model=list[Order])
async def get_all_orders():
    orders = await Order.find_all().to_list()
    return orders

@router.get("/{id}", response_model=Order)
async def get_order(id: PydanticObjectId):
    order = await Order.get(id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.patch("/{id}/status", response_model=Order)
async def update_order_status(
    id: PydanticObjectId, 
    status_data: OrderStatusUpdate
):
    order = await Order.get(id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    order.status = status_data.status
    await order.save()
    return order