from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from app.db.services.tg_notifications import TgNotificationsService


router = APIRouter()


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
    tg_service = TgNotificationsService()
    user = await tg_service.checkUserExist(tg_id)
    if user:
        return JSONResponse(
            {'data': True}
        )
    else:
        return JSONResponse(
            {'data': False}
        )
