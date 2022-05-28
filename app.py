from fastapi import FastAPI

from modules.auth.router import router as auth_router
from modules.board.router import router as board_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "PATCH", "DELETE", "PUT"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(board_router)
