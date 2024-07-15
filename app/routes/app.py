from fastapi import  APIRouter

router = APIRouter()


@router.get("/")
async def is_live():
    return {"is_live": "The API is currently live"}
