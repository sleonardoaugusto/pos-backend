from fastapi import FastAPI

from app import db
from app.api import api_router
from app.db.session import engine

db.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(api_router, prefix='/api')
