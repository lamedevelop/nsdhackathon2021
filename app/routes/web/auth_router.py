import time

from fastapi import APIRouter, Request, Form
from starlette import status
from fastapi.templating import Jinja2Templates

from app.db.models.user import User, UserRegistration
from app.db.services.users import UsersService

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
    "/login",
    name='web:login-page',
    status_code=status.HTTP_200_OK
 )
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post(
    "/login",
    name='web:login-action',
    status_code=status.HTTP_200_OK
 )
async def login_post(
        request: Request,
        email: str = Form(...),
        password: str = Form(...),
):
    user_service = UsersService()
    auth_status = await user_service.login(email, password)

    if auth_status == user_service.STATUS_AUTH_OK:
        return templates.TemplateResponse("main.html", {"request": request})
    else:
        return templates.TemplateResponse("login.html", {"request": request})


@router.get(
    "/registration",
    name='web:registration-page',
    status_code=status.HTTP_200_OK
)
async def registration(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})


@router.post(
    "/registration",
    name='web:registration-action',
    status_code=status.HTTP_200_OK
)
async def registration_action(
        request: Request,
        name: str = Form(...),
        phone: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
):
    user_service = UsersService()
    name = name.split()
    if len(name) < 2:
        name.append("")

    auth_status = await user_service.register(
        UserRegistration(
            first_name=name[0],
            last_name=name[1],
            password_hash=password,
            phone=phone,
            email=email,
            registration_date=int(time.time())
        )
    )

    if auth_status == user_service.STATUS_AUTH_OK:
        return templates.TemplateResponse("login.html", {"request": request})
    else:
        return templates.TemplateResponse("registration.html", {"request": request})
