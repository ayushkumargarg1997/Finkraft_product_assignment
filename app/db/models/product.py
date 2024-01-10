from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Product(BaseModel):
    product_name: str
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    status: str
    category: str
    subcategory: str
    description: str
    price: float
    discount: int
    image_url: str
    quantity: int
    supplier: str








    



