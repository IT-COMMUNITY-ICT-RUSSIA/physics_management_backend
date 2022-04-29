import datetime
import os
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import parse_obj_as

from modules.auth.models import User, UserInformation, UserPassword

SECRET_KEY = os.environ.get("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bool(pwd_context.verify(plain_password, hashed_password))


async def get_password_hash(password: str) -> str:
    return str(pwd_context.hash(password))


async def create_access_token(
    data: dict[str, datetime | str],
    expires_delta: datetime.timedelta = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    remember: bool = False,
) -> str:
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + expires_delta
    to_encode.update({"rem": remember})
    to_encode.update({"exp": expire})

    encoded_jwt: str = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def authenticate_user(user: UserPassword) -> str:
    # TODO: Fetch user data from database
    user_data = None
    if not user_data:
        return None
    if not verify_password(user.password, user_data.hashed_password):
        return None
    return user_data


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise ValueError("Username not provided")

        user: UserPassword = UserPassword()

    except JWTError:
        raise ValueError("Failed to decode jwt token")

    except Exception as e:
        raise HTTPException(404, str(e))

    user_dict = user.dict(exclude={"hashed_password"})
    return parse_obj_as(User, user_dict)


async def get_user_data(user=Depends(get_current_user)) -> UserInformation:
    # TODO: fetch user info from db
    return UserInformation()
