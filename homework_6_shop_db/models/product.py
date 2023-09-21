from pydantic import BaseModel, Field
from typing import Optional


class ProductIn(BaseModel):
    productname: str = Field(..., max_length=50)
    description: Optional[str] = Field(min_length=3)
    price: float = Field(...,ge=0.00)


class Product(BaseModel):
    id: int
    productname: str = Field(..., max_length=50)
    description: Optional[str] = Field(min_length=3)
    price: float = Field(..., ge=0.00)