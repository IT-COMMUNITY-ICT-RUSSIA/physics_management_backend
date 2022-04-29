from fastapi import APIRouter, Depends

from modules.auth.models import GenericResponse, UserInformation, UserInformationOut
from modules.auth.dependencies import get_user_data


router = APIRouter()


@router.get("/me", response_model=UserInformationOut | GenericResponse)
async def get_user_data(user: UserInformation = Depends(get_user_data)) -> None:
    """Получение данных пользователя по токену"""
    return UserInformationOut(user=user)
