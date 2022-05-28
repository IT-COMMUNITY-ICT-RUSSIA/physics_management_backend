from fastapi import APIRouter, Depends
from modules.auth.dependencies import get_user_data
from modules.auth.models import GenericResponse, UserInformation

from modules.board.models import BoardOut


router = APIRouter()


BOARD = {i: [None for _ in range(6)] for i in range(4)}


@router.get("/board")
async def get_board() -> BoardOut:
    return BoardOut(board=BOARD)


@router.post("/board")
async def add_user_to_board(
    col: int,
    row: int,
    user: UserInformation = Depends(get_user_data),
) -> GenericResponse:
    try:
        BOARD[col][row] = user
    except Exception as e:
        return GenericResponse(status=500, details=f"Ошибка! {e}")
