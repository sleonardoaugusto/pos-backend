import uvicorn
from alembic.config import Config
from fastapi import FastAPI

from alembic import command
from app import db
from app.api import api_router
from app.db.session import engine

db.Base.metadata.create_all(bind=engine)

alembic_cfg = Config("alembic.ini")
command.stamp(alembic_cfg, "head")

app = FastAPI()
app.include_router(api_router, prefix='/api')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
