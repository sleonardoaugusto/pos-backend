from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps

router = APIRouter()


class Stock:
    def __init__(self, db):
        self._db = db

    def entry(self, products, provider_id):
        return [
            crud.product.create(
                self._db,
                obj_in=schemas.ProductCreate(**product.dict(), provider_id=provider_id),
            )
            for product in products
        ]

    def out(self, products):
        records = []
        for product in products:
            record = crud.product.get(self._db, product.id)
            product.qty = record.qty - product.qty
            records.append(crud.product.update(self._db, db_obj=record, obj_in=product))
        return records


@router.post('/entry', response_model=List[schemas.Product])
def create_stock_entry(
    *, db: Session = Depends(deps.get_db), stock_in: schemas.StockEntryCreate
):
    stock = Stock(db)
    products = stock.entry(stock_in.products, stock_in.provider_id)
    return products


@router.post('/out', response_model=List[schemas.Product])
def create_out_of_stock(
    *, db: Session = Depends(deps.get_db), stock_in: schemas.OutOfStockCreate
):
    stock = Stock(db)
    return stock.out(stock_in.products)
