from pydantic import BaseModel


class ProviderBase(BaseModel):
    name: str


class ProviderCreate(ProviderBase):
    pass


class ProviderUpdate(ProviderBase):
    pass


class ProviderInDBBase(ProviderBase):
    id: int

    class Config:
        orm_mode = True


class Provider(ProviderInDBBase):
    pass
