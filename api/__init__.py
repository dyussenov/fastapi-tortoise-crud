from fastapi import APIRouter
from .customers import router as customers_router


router = APIRouter()
router.include_router(customers_router)