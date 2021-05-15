from fastapi import APIRouter

from app.routes.web import auth_router, main_router
from app.routes.api import app_router, messages_router, tg_router

router = APIRouter()

router.include_router(auth_router.router, tags=["web"], prefix="")
router.include_router(main_router.router, tags=["web"], prefix="")

router.include_router(app_router.router, tags=["api"], prefix="/api")
router.include_router(messages_router.router, tags=["api"], prefix="/api")
router.include_router(tg_router.router, tags=["api"], prefix="/api")
