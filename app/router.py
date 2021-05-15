from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import JSONResponse

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get(
    "/hello",
    name='basic:hello',
    status_code=status.HTTP_200_OK
)
async def hello():
    return JSONResponse(
        {'response': "HELLO FROM ORKS!"}
    )


@router.get(
    "/",
    name='basic:default',
    status_code=status.HTTP_200_OK
)
async def hello(request: Request):
    data = {'response': "default"}
    return templates.TemplateResponse("index.html", {"request": request, "value": data})
