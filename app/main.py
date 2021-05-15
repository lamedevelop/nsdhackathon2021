from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.main import router


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    application.mount("/static", StaticFiles(directory="static"), name="static")

    return application


app = get_application()
