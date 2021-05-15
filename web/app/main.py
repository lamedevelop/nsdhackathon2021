from fastapi import FastAPI

from app.router import router

from fastapi.staticfiles import StaticFiles

def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    application.mount("/static", StaticFiles(directory="static"), name="static")

    return application


app = get_application()
