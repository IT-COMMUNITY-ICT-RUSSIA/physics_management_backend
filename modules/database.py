from modules.auth.models import UserInformation
from modules.singleton import SingletonMeta
from modules.board.models import TestUser1, TestUser2, TestUser4, TestUser3, TestUser4


class BoardWrapper(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.board = {
            0: [None, TestUser2().dict(), None, None, None, None],
            1: [None, None, None, TestUser3().dict(), None, None],
            2: [TestUser1().dict(), None, None, None, None, None],
            3: [None, None, None, None, None, TestUser4().dict()],
        }

    async def get_board(self) -> dict[str, list[UserInformation | None]]:
        return self.board

    async def update_slot(self, row: int, col: int, user: UserInformation) -> None:
        print(user)
        self.board[row][col] = user.dict()
