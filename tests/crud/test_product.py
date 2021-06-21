import pytest
from sqlalchemy.orm import Session

from app import crud
from app.models import Provider
from app.schemas import ProductCreate


@pytest.fixture
def fix_provider(db: Session):
    db_obj = Provider(name='Fake provider')
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def test_create_product(db: Session, fix_provider):
    obj = dict(name='Fake Product', qty=1)
    product_in = ProductCreate(**obj, provider_id=fix_provider.id)
    product = crud.product.create(db=db, obj_in=product_in)
    assert product.name == obj['name']
    assert product.qty == obj['qty']
    assert product.provider_id == fix_provider.id
