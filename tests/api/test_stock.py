from http import HTTPStatus

import pytest
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from app.models import Provider


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
            {'name': 'Fake Product', 'qty': 1},
            {'name': 'Fake Product 2', 'qty': 2},
        ],
    }
    response = client.post('/api/stock/entry', json=payload)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == [
        {'id': 1, 'name': 'Fake Product', 'qty': 1},
        {'id': 2, 'name': 'Fake Product 2', 'qty': 2},
    ]
