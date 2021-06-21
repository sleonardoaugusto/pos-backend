from sqlalchemy import Integer, Column, String

from app.db import Base


class Provider(Base):
    __tablename__ = 'providers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
