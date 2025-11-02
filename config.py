from datetime import datetime, timedelta
from passlib.context import CryptContext as bcrypt_context
from jose import jwt


SECRET_KEY = "b706a4ae1ae313036745e8a21712698a"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = bcrypt_context(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expiration_minutes: timedelta):
    encode = data.copy()
    expire = datetime.utcnow() + expiration_minutes
    encode.update({"exp": expire})
    token = jwt.encode(encode, SECRET_KEY, ALGORITHM)
    return token
