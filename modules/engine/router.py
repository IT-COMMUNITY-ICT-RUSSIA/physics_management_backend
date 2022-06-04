from logging import exception
from fastapi import APIRouter
import requests
from models import Status
from physics_management_backend.modules.board.models import GenericResponse

IP = "192.168.192.126"
PORT = "1880"

router = APIRouter()


@router.get("/setup/status")
async def getStatus():
    request = requests.get("{IP}{PORT}/setup/status")
    return request

@router.get("/setup/music")
async def getStatus():
    request = requests.get("{IP}{PORT}/setup/music")
    return request

@router.post("/setup/command")
async def setCoord(
    coord: int
):
    try:
        request = requests.post("{IP}{PORT}/setup/command?setcoord={coord}")
        return request
    except Exception as e:
        return GenericResponse(status=500, details=f"Ошибка! {e}")

@router.post("/setup/command")
async def setCapacity(
    action: str,
    capacity1: int,
    capacity2: int
):
    try:
        request = requests.post("{IP}{PORT}/setup/command?{action}&setcapacity1={capacity1}&setcapacity2={capacity2}")
        return request
    except Exception as e:
        return GenericResponse(status=500, details=f"Ошибка! {e}")