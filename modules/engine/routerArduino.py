import requests
from fastapi import APIRouter
from requests import Response

from modules.board.models import GenericResponse

IP = "192.168.192.126:1880"

router = APIRouter()


@router.get("/setup/status")
async def getStatus():
    try:
        request = requests.get(f"http://{IP}/setup/status")
        return request.json()
    except Exception as e:
        return GenericResponse(status=500, details=f"Ошибка! {e}")


@router.get("/setup/start")
async def getStatus():
    try:
        request = requests.get(f"http://{IP}/setup/start")
        return request.json()
    except Exception as e:
            return GenericResponse(status=500, details=f"Ошибка! {e}")


@router.get("/setup/stop")
async def getStatus():
    try:
        request = requests.get(f"http://{IP}/setup/stop")
        return request.json()
    except Exception as e:
        return GenericResponse(status=500, details=f"Ошибка! {e}")


@router.get("/setup/music")
async def getStatus():
    try:
        request = requests.get(f"http://{IP}/setup/music")
        return request.json()
    except Exception as e:
        return GenericResponse(status=500, details=f"Ошибка! {e}")


@router.get("/setup/command")
async def setupCommand(
    action: str,
    coord: int | None = None,  # Value of this parameter is only between 0 and 230
    capacity1: int | None = None,  # Value of this parameter is only "1" or "2"
    capacity2: int | None = None  # Value of this parameter is only "1" or "2" or "3"
):
    try:
        request: Response
        match action:
            case "setCapacity":
                request = requests.get(f"http://{IP}/setup/command?{action}&setСapacity1={capacity1}&setСapacity2={capacity2}")
            case "setCoord":
                request = requests.get(f"http://{IP}/setup/command?{action}={coord}")
            case _:
                return GenericResponse(status=400, details="Неправильный запрос")
        return request.json()
    except Exception as e:
        return GenericResponse(status=500, details=f"Ошибка! {e}")
