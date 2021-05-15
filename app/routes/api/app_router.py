from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import JSONResponse


router = APIRouter()


@router.get(
    "/hello",
    name='api:hello',
    status_code=status.HTTP_200_OK
)
async def hello():
    return JSONResponse(
        {'response': "HELLO FROM ORKS!"}
    )


@router.get(
    "/auth",
    name='api:auth',
    status_code=status.HTTP_200_OK
)
async def auth():
    return JSONResponse(
        {'response': "HELLO FROM ORKS!"}
    )
