from pydantic import BaseModel

from modules.auth.models import User, UserInformation


class GenericResponse(BaseModel):
    status: int = 200
    details: str = "Success"


class BoardOut(GenericResponse):
    board: dict[int, list[str | None]]


class BoardSlotOut(GenericResponse):
    board_slot = UserInformation
