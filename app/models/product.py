from sqlalchemy import Column, Integer, String, ForeignKey

from app.db import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    qty = Column(Integer, nullable=False)
    provider_id = Column(Integer, ForeignKey('providers.id'))
