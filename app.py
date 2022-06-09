from fastapi import FastAPI

from modules.auth.router import router as auth_router
from modules.board.router import router as board_router
from modules.engine.routerArduino import router as arduino_router
from modules.engine.routerOscilloscope import router as oscilloscope_router
from modules.engine.routerGenerator import router as generator_router
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
app.include_router(arduino_router, tags=["Ардуино"])
app.include_router(oscilloscope_router, tags=["Осциллограф"])
app.include_router(generator_router, tags=["Генератор"])
