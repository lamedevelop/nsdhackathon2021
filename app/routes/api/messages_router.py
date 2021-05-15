import os
from typing import List

from fastapi import APIRouter, Request, UploadFile, File
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse

from app.db.services.messages import MessagesService


router = APIRouter()


@router.post(
    "/send",
    name='api:send-message',
    status_code=status.HTTP_200_OK
)
async def get_unread(file: UploadFile = File(...)):
    print(file.file)
    os.mkdir("images")
    file_name = os.getcwd() + "/images/" + file.filename + "123"
    with open(file_name, 'wb+') as f:
        f.write(file.file.read())
        f.close()

    return {"filename": file_name}


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
