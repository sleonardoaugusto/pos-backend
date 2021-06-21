from fastapi import APIRouter

from app import schemas

router = APIRouter()


@router.post('/stocks/entry/', response_model=schemas.Provider)
async def create_stock_entry():
    return
