from sqlalchemy.orm import Session

from app import crud
from app.schemas import ProviderCreate


def test_create_provider(db: Session):
    name = 'Provider Name'
    provider_in = ProviderCreate(name=name)
    provider = crud.provider.create(db=db, obj_in=provider_in)
    assert provider.name == name
