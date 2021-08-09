from typing import List

from pydantic import BaseModel

from app import schemas


class StockEntryCreate(BaseModel):
    provider_id: int
    products: List[schemas.ProductBase]


class OutOfStockCreate(BaseModel):
    products: List[schemas.ProductOutOfStock]
