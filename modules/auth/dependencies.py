from calendar import c
import os
from fastapi import Depends, HTTPException

from jose import JWTError, jwt
from pydantic import parse_obj_as

from modules.auth.models import User, UserInformation, UserPassword

SECRET_KEY = "testing"
ALGORITHM = "HS256"


async def verify_password(plain_password: str) -> bool:
    return bool(plain_password == "testing")


async def create_access_token(
    data: dict[str, str],
) -> str:
    to_encode = data.copy()
    to_encode.update({"login": data["login"]})
    to_encode.update({"pass": data["pass"]})

    encoded_jwt: str = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def auth_user(username: str, password: str) -> UserPassword:
    if await verify_password(password):
        return UserPassword(username=username, password=password)
    raise HTTPException(status_code=403, detail="Failed to verify password")


async def get_current_user(token: str) -> UserPassword:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("login")

        if username is None:
            raise ValueError("Username not provided")

        user: User = User(username=username)

    except JWTError:
        raise ValueError("Failed to decode jwt token")

    except Exception as e:
        raise HTTPException(404, str(e))
    return parse_obj_as(User, user.dict())


async def get_user_data(user: User = Depends(get_current_user)) -> UserInformation:
    full_name = "Неизвестный пользователь"
    group = None
    match user.username:
        case "307526":
            full_name = "Тимофеев Н.А."
            group = "K3241"
        case "313103":
            full_name = "Барышева З.А."
            group = "K3241"
        case "309506":
            full_name = "Береза Н."
            group = "K3241"
        case "137820":
            full_name = "Капитонов А.А."

    return UserInformation(username=user.username, full_name=full_name, group=group)
