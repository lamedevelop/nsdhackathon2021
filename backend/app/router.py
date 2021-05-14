from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import JSONResponse


router = APIRouter()


@router.get(
    "/hello",
    name='basic:hello',
    status_code=status.HTTP_200_OK
)
async def hello():
    return JSONResponse(
            {'response': "HELLO FROM ORKS!"},
            status_code=status.HTTP_200_OK,
        )


@router.get(
    "/",
    name='basic:default',
    status_code=status.HTTP_200_OK
)
async def hello():
    return JSONResponse(
            {'response': "default"},
            status_code=status.HTTP_200_OK,
        )
