from fastapi import APIRouter

from .routes import routes

router = APIRouter()
router.include_router(routes.router, prefix='/routes' , tags=['Items'])