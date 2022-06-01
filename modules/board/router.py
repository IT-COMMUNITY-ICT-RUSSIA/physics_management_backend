from loguru import logger
from fastapi import APIRouter, Depends
from modules.auth.dependencies import get_user_data
from modules.auth.models import GenericResponse, UserInformation

from modules.board.models import BoardOut
from modules.database import BoardWrapper


router = APIRouter()


BOARD = BoardWrapper()


@router.get("/board")
async def get_board() -> BoardOut:
    logger.info(await BOARD.get_board())
    return BoardOut(board=await BOARD.get_board())


@router.post("/board")
async def add_user_to_board(
    col: int,
    row: int,
    user: UserInformation = Depends(get_user_data),
) -> GenericResponse:
    try:
        logger.info(user)
        await BOARD.update_slot(row=row, col=col, user=user)
        logger.info(await BOARD.get_board())
        return GenericResponse(status=200, details=f"OK")
    except Exception as e:
        return GenericResponse(status=500, details=f"Ошибка! {e}")


@router.delete("/board")
async def remove_user_from_board(col: int,row: int) -> GenericResponse:
    try:
        await BOARD.clear_slot(row=row, col=col)
        return GenericResponse(status=200, details=f"OK")
    except Exception as e:
        return GenericResponse(status=500, details=f"Ошибка! {e}")
