from fastapi import APIRouter, Request
from starlette import status
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get(
    "/",
    name='web:auth',
    status_code=status.HTTP_200_OK
)
async def auth(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get(
    "/registration",
    name='web:registration',
    status_code=status.HTTP_200_OK
)
async def auth(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})


@router.get(
    "/registration/action",
    name='web:registration-action',
    status_code=status.HTTP_200_OK
)
async def auth(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})
