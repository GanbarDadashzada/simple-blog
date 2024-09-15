from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.core.database import Session, get_session

from app.crud.login import LoginService

from app.schemas.registration import Registration

router = APIRouter()


@router.post("/login", tags=["Login"])
async def login(user_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)):
    return await LoginService.login(user_data, db)

@router.post("/register", tags=["Register"])
async def register(user_data: Registration, db: Session = Depends(get_session)):
    return await LoginService.register(user_data, db)