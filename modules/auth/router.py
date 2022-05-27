from fastapi import APIRouter, Depends

from modules.auth.models import GenericResponse, Token, UserInformation, UserInformationOut, UserPassword
from modules.auth.dependencies import create_access_token, get_user_data, auth_user


router = APIRouter()


@router.get("/me", response_model=UserInformationOut | GenericResponse)
async def get_user(user: UserInformation = Depends(get_user_data)) -> None:
    """Получение данных пользователя по токену"""
    return UserInformationOut(user=user)


@router.post("/auth", response_model=Token | GenericResponse)
async def login(user: UserPassword = Depends(auth_user)):
    return Token(token=await create_access_token(data={"login": user.username, "pass": user.password}))
