from app.crud.base import CRUDBase
from app.models import Provider
from app.schemas import ProviderCreate, ProviderUpdate


class CRUDProvider(CRUDBase[Provider, ProviderCreate, ProviderUpdate]):
    pass


provider = CRUDProvider(Provider)
