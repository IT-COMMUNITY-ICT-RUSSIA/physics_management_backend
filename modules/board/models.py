import typing

from pydantic import BaseModel

from modules.auth.models import UserInformation


class GenericResponse(BaseModel):
    status: int = 200
    details: str = "Success"


class TestUser1(UserInformation):
    username: str = "307526"
    full_name: str = "Тимофеев Н.А."
    group: str | None = "K3241"


class TestUser2(UserInformation):
    username: str = "313103"
    full_name: str = "Барышева З.А."
    group: str | None = "K3241"


class TestUser3(UserInformation):
    username: str = "309506"
    full_name: str = "Береза Н."
    group: str | None = "K3241"


class TestUser4(UserInformation):
    username: str = "137820"
    full_name: str = "Капитонов А.А."
    group: str | None = None


class BoardOut(GenericResponse):
    board: dict[str, list[UserInformation | None]]


class BoardSlotOut(GenericResponse):
    board_slot = UserInformation
