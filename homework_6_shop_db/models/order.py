from pydantic import BaseModel


class OrderIn(BaseModel):
    user_id: int
    product_id: int
    orderdate: str
    status: str


class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    orderdate: str
    status: str