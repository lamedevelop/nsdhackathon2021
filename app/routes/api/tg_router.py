from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from app.db.services.users import UsersService
from app.db.services.tg_notifications import TgNotificationsService

router = APIRouter()


@router.get(
    "/user",
    name='api:get-tg-user',
    status_code=status.HTTP_200_OK
)
async def get_tg_user(tg_id: int):
    user_service = UsersService()
    return JSONResponse(
        {'data': await user_service.getUserByTgId(tg_id)}
    )


@router.get(
    "/notifications",
    name='api:get-notifications',
    status_code=status.HTTP_200_OK
)
async def get_notifications():
    tg_service = TgNotificationsService()
    return JSONResponse(
        {'data': await tg_service.getUnfinishedNotifications()}
    )


@router.get(
    "/user/exist",
    name='api:check-user-exist',
    status_code=status.HTTP_200_OK
)
async def get_notifications(tg_id: int):
    user_service = UsersService()
    user = await user_service.checkUserExist(tg_id)
    if user:
        return JSONResponse(
            {'data': True}
        )
    else:
        return JSONResponse(
            {'data': False}
        )
