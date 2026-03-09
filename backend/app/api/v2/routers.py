from fastapi import APIRouter, Depends, HTTPException
from app.api.v2.endpoints import user

router = APIRouter()
router.include_router(user.router, prefix="/users", tags=["users"])
