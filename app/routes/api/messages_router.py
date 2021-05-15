from fastapi import APIRouter, UploadFile, File
from starlette import status
from starlette.responses import JSONResponse

from app.db.services.messages import MessagesService


router = APIRouter()


@router.post(
    "/send",
    name='api:send-message',
    status_code=status.HTTP_200_OK
)
async def send(file: UploadFile = File(...)):
    message_service = MessagesService()
    successful = await message_service.saveFile(file)
    if not successful:
        return JSONResponse(
            {"exception": "failed to send file"},
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    else:
        return JSONResponse({"data": True})


@router.get(
    "/income",
    name='api:income',
    status_code=status.HTTP_200_OK
)
async def income(user_id: int):
    message_service = MessagesService()
    return JSONResponse(
        {'data': await message_service.getIncomeMessages(user_id)}
    )


@router.get(
    "/outcome",
    name='api:outcome',
    status_code=status.HTTP_200_OK
)
async def outcome(user_id: int):
    message_service = MessagesService()
    return JSONResponse(
        {'data': await message_service.getOutcomeMessages(user_id)}
    )


@router.get(
    "/unread",
    name='api:get-unread',
    status_code=status.HTTP_200_OK
)
async def get_unread(user_id: int):
    message_service = MessagesService()
    return JSONResponse(
        {'data': await message_service.getNewMessages(user_id)}
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
