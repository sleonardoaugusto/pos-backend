from sqlalchemy.orm import Session

from app import crud
from app.schemas import ProviderCreate


def test_create_provider(db: Session):
    obj = dict(name='Fake Provider')
    provider_in = ProviderCreate(**obj)
    provider = crud.provider.create(db=db, obj_in=provider_in)
    assert provider.name == obj['name']
