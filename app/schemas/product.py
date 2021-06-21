from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    qty: int


class ProductCreate(ProductBase):
    provider_id: int


class ProductUpdate(ProductBase):
    pass


class ProductInDBBase(ProductBase):
    id: int

    class Config:
        orm_mode = True


class Product(ProductInDBBase):
    pass
