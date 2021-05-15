from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse


router = APIRouter()


@router.get(
    "/auth",
    name='api:auth',
    status_code=status.HTTP_200_OK
)
async def auth():
    return JSONResponse(
        {'response': "HELLO FROM ORKS!"}
    )
