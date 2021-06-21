from pydantic import BaseModel


class ProviderBase(BaseModel):
    name: str


class Provider(ProviderBase):
    pass


class ProviderCreate(ProviderBase):
    pass


class ProviderUpdate(ProviderBase):
    pass
