from app import models, schemas
from app.crud.base import CRUDBase
from app.models import Product


class CRUDProduct(
    CRUDBase[models.Product, schemas.ProductCreate, schemas.ProductUpdate]
):
    pass


product = CRUDProduct(Product)
