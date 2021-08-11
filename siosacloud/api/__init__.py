from fastapi import APIRouter
from .v1.license import license_router

router = APIRouter(
	prefix='/api/v1'
)

router.include_router(license_router)