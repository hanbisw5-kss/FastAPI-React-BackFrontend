from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# from app.db.session import get_db
from app.crud.user import get_user, create_user, update_user, delete_user, get_users
from app.schemas.user import UserCreate, User, UserUpdate
from typing import List

from app.core.config import get_db

router = APIRouter()


@router.get("/", response_model=List[User])
async def read_users(db: AsyncSession = Depends(get_db)):
    # users = get_users(db)
    return  await get_users(db)


@router.post("/", response_model=User)
async def create_user_endpoint(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=User)
def update_user_endpoint(user_id: int, user: UserUpdate, db: AsyncSession = Depends(get_db)):
    return update_user(db=db, user_id=user_id, user=user)

@router.delete("/{user_id}")
def delete_user_endpoint(user_id: int, db: AsyncSession = Depends(get_db)):
    return delete_user(db=db, user_id=user_id)
