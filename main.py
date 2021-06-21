from fastapi import FastAPI

from app import db
from app.db.session import engine

db.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post('/stocks/entry/')
async def create_stock_entry():
    return
