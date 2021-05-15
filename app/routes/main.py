from fastapi import APIRouter

from app.routes import web
from app.routes.api import app_router, messages_router, tg_router

router = APIRouter()
router.include_router(app_router.router, tags=["api"], prefix="/api")
router.include_router(messages_router.router, tags=["api"], prefix="/api")
router.include_router(tg_router.router, tags=["api"], prefix="/api")
router.include_router(web.router, tags=["web"], prefix="")
