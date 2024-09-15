from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.database import Session, get_session

from app.models.user import User

SECRET_KEY_FOR_TOKEN = "your_secret_key_here"
TOKEN_ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Authentication:

    def hashing_password(password: str):
        return pwd_context.hash(password)

    def password_verification(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def token_create(data: dict):
        to_encode = data.copy()

        expire = datetime.now(timezone.utc) + timedelta(days=1)

        to_encode.update({"exp": expire})
        jwt_token = jwt.encode(to_encode, SECRET_KEY_FOR_TOKEN, algorithm=TOKEN_ALGORITHM)

        return jwt_token

    def token_decode(token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY_FOR_TOKEN, algorithms=[TOKEN_ALGORITHM])
            return payload
        except JWTError:
            return None


    def active_username(token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)):
        credentials_exception = HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY_FOR_TOKEN, algorithms=[TOKEN_ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise credentials_exception
        
        return user.username