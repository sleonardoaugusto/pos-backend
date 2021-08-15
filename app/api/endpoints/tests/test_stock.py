import pytest
from sqlalchemy.orm import Session
from starlette import status
from starlette.testclient import TestClient

from app import crud
from app.models import Provider, Product


@pytest.fixture
def fix_provider(db: Session):
    db_obj = Provider(name='Fake provider')
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def test_create_stock_entry(db: Session, client: TestClient, fix_provider):
    payload = {
        'provider_id': fix_provider.id,
        'products': [
            {'name': 'Fake Product 1', 'qty': 1},
            {'name': 'Fake Product 2', 'qty': 2},
        ],
    }
    response = client.post('/api/stock/entry', json=payload)
    assert len(crud.product.get_multi(db)) == 2
    assert response.status_code == status.HTTP_201_CREATED


@pytest.fixture
def fix_two_products(db: Session, fix_provider):
    db.add_all(
        [
            Product(name='Fake Product 1', qty=1, provider_id=fix_provider.id),
            Product(name='Fake Product 2', qty=1, provider_id=fix_provider.id),
        ]
    )
    db.commit()
    return db.query(Product).all()


def test_create_out_of_stock(db: Session, client: TestClient, fix_two_products):
    product_one, product_two = fix_two_products
    payload = {
        'products': [
            {'id': product_one.id, 'qty': 1},
            {'id': product_two.id, 'qty': 1},
        ]
    }
    response = client.post('/api/stock/out', json=payload)
    db.refresh(product_one)
    db.refresh(product_two)

    assert product_one.qty == 0
    assert product_two.qty == 0
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() is None
