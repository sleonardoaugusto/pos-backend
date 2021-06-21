from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps

router = APIRouter()


class Stock:
    def __init__(self, db, provider_id):
        self._db = db
        self.provider_id = provider_id

    def entry(self, products):
        return [
            crud.product.create(
                self._db,
                obj_in=schemas.ProductCreate(
                    **product.dict(), provider_id=self.provider_id
                ),
            )
            for product in products
        ]


@router.post('/entry', response_model=List[schemas.Product])
def create_stock_entry(
    *, db: Session = Depends(deps.get_db), stock_in: schemas.StockEntryCreate
):
    stock = Stock(db, stock_in.provider_id)
    products = stock.entry(stock_in.products)
    return products
