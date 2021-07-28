from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.routes.main import router

PREFIX = "/nsd"


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router, prefix=PREFIX)
    application.mount(f"{PREFIX}/static", StaticFiles(directory="static"), name="static")

    origins = [
        "http://localhost",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ]

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


app = get_application()