from fastapi import APIRouter

router = APIRouter()


@router.get(path='/sampling-service/isActive')
async def is_active():
    return True


@router.get(path='/sampling-service/ping')
async def ping():
    return 'pong'