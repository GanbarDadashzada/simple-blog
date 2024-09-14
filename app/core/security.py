from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY_FOR_TOKEN = "your_secret_key_here"
TOKEN_ALGORITHM = "HS256"

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
