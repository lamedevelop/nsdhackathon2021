from fastapi import APIRouter

from app.routes import api, web


router = APIRouter()
router.include_router(api.router, tags=["api"], prefix="/api")
router.include_router(web.router, tags=["web"], prefix="")
