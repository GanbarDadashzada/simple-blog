from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.core.security import Authentication
from app.core.database import Session

from app.utils.exception import CustomException

from app.models.user import User

from app.schemas.registration import Registration

class LoginService:


    async def register(user_data: Registration, db: Session):

        user = db.query(User).filter(User.username == user_data.username).first()
        if user:
            raise CustomException(message="Username already exists")
        
        hashed_password = Authentication.hashing_password(user_data.password)

        user_db = User(
            username = user_data.username,
            password = hashed_password,
            email_address = user_data.email,
            name = user_data.name,
            surname = user_data.surname
        )
        db.add(user_db)
        db.commit()

        return {"message": "User registered successfully"}


    async def login(data: OAuth2PasswordRequestForm, db: Session):
        
        user = db.query(User).filter(User.username == data.username).first()
        if not user:
            raise CustomException(message="Invalid username")

        password_check = Authentication.password_verification(data.password, user.password)
        if not password_check:
            raise CustomException(message="Invalid password")

        access_token = Authentication.token_create(data={"sub": data.username})

        return {"access_token": access_token, "token_type": "bearer"}
