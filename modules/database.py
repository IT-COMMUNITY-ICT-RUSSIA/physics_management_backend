from copy import deepcopy
from loguru import logger
from modules.auth.models import UserInformation
from modules.singleton import SingletonMeta


class BoardWrapper(metaclass=SingletonMeta):
    @logger.catch
    def __init__(self) -> None:
        self._users: dict[str, bool] = {}
        self.board = {
            0: [None, None, None, None, None, None],
            1: [None, None, None, None, None, None],
            2: [None, None, None, None, None, None],
            3: [None, None, None, None, None, None],
        }

    async def get_board(self) -> dict[str, list[UserInformation | None]]:
        return deepcopy(self.board)

    async def update_slot(self, row: int, col: int, user: UserInformation) -> None:
        if self._users.get(user.username, None):
            raise ValueError("User already booked slot")
        self._users[user.username] = True
        tmp_board = deepcopy(await self.get_board()) 
        tmp_board[row][col] = user.dict()
        self.board = tmp_board

    async def clear_slot(self, row: int, col: int) -> None:
        logger.info(self.board[row][col])
        tmp_board = deepcopy(await self.get_board())
        if self.board[row][col]:
            self._users[self.board[row][col].get("username")] = False
        tmp_board[row][col] = None
        self.board = tmp_board
        logger.info(self.board[row][col])
