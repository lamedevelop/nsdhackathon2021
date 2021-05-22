from fastapi import APIRouter, Request
from starlette import status
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get(
    "/main",
    name='web:registration',
    status_code=status.HTTP_200_OK
)
async def main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@router.get(
    "/settings",
    name='web:settings',
    status_code=status.HTTP_200_OK
)
async def settings(request: Request):
    return templates.TemplateResponse("settings.html", {"request": request})


@router.get(
    "/income",
    name='web:income',
    status_code=status.HTTP_200_OK
)
async def income(request: Request):
    return templates.TemplateResponse("income.html", {"request": request})


@router.get(
    "/outcome",
    name='web:outcome',
    status_code=status.HTTP_200_OK
)
async def outcome(request: Request):
    return templates.TemplateResponse("outcome.html", {"request": request})


@router.get(
    "/send",
    name='web:send',
    status_code=status.HTTP_200_OK
)
async def send(request: Request):
    return templates.TemplateResponse("send.html", {"request": request})


@router.post(
    "/send/action",
    name='web:send-action',
    status_code=status.HTTP_200_OK
)
async def send(request: Request):
    return templates.TemplateResponse("outcome.html", {"request": request})

