from fastapi import APIRouter
from src.endpoints import product
from src.endpoints import users

router = APIRouter()
router.include_router(product.router)
router.include_router(users.router)
