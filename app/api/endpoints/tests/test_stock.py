from http import HTTPStatus

import pytest
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from app.models import Provider, Product


@pytest.fixture
def fix_provider(db: Session):
    db_obj = Provider(name='Fake provider')
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def test_create_stock_entry(client: TestClient, fix_provider):
    payload = {
        'provider_id': fix_provider.id,
        'products': [
            {'name': 'Fake Product 1', 'qty': 1},
            {'name': 'Fake Product 2', 'qty': 2},
        ],
    }
    response = client.post('/api/stock/entry', json=payload)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == [
        {'id': 1, 'name': 'Fake Product 1', 'qty': 1},
        {'id': 2, 'name': 'Fake Product 2', 'qty': 2},
    ]


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


def test_create_out_of_stock(client: TestClient, fix_two_products):
    payload = {
        'products': [
            {'id': fix_two_products[0].id, 'qty': 1},
            {'id': fix_two_products[1].id, 'qty': 1},
        ]
    }
    response = client.post('/api/stock/out', json=payload)
    assert response.status_code == 200
    assert response.json() == [
        {'id': 1, 'name': 'Fake Product 1', 'qty': 0},
        {'id': 2, 'name': 'Fake Product 2', 'qty': 0},
    ]
