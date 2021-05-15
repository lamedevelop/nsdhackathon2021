from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import JSONResponse

from app.db.services.messages import MessagesService


router = APIRouter()


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
