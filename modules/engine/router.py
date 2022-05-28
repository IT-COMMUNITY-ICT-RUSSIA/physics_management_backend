from logging import exception
from fastapi import APIRouter
import requests
from models import Status
from physics_management_backend.modules.board.models import GenericResponse

router = APIRouter()


@router.get("/setup/status")
async def getStatus():
    request = requests.get("/setup/status")
    return request

@router.post("/setup/command")
async def setCoord(
    coord: int
):
    try:
        request = requests.post("/setup/command?setcoord={coord}")
        return request
    except Exception as e:
        return GenericResponse(status=500, details=f"Ошибка! {e}")


    