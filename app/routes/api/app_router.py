from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import JSONResponse

from app.db.services.messages import MessagesService


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


@router.get(
    "/zip_struct",
    name='api:get-zi-struct',
    status_code=status.HTTP_200_OK
)
async def get_zip_struct(message_id: int):
    message_service = MessagesService()
    return JSONResponse(
        {'data': await message_service.getZipFileStruct(message_id)}
    )
