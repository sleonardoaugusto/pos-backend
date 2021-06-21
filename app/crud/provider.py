from app import models, schemas
from app.crud.base import CRUDBase


class CRUDProvider(
    CRUDBase[models.Provider, schemas.ProviderCreate, schemas.ProviderUpdate]
):
    pass


provider = CRUDProvider(models.Provider)
