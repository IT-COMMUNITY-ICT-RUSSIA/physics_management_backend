from loguru import logger
from modules.auth.models import UserInformation
from modules.singleton import SingletonMeta
from modules.board.models import TestUser1, TestUser2, TestUser4, TestUser3, TestUser4


class BoardWrapper(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.board = {
            0: [None, None, None, None, None, None],
            1: [None, None, None, None, None, None],
            2: [None, None, None, None, None, None],
            3: [None, None, None, None, None, None],
        }

    async def get_board(self) -> dict[str, list[UserInformation | None]]:
        return self.board

    async def update_slot(self, row: int, col: int, user: UserInformation) -> None:
        self.board[row][col] = user.dict()

    async def clear_slot(self, row: int, col: int) -> None:
        logger.info(self.board[row][col])
        self.board[row][col] = None
        logger.info(self.board[row][col])
