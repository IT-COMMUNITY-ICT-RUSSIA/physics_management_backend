import requests
from fastapi import APIRouter
from requests import Response

from modules.board.models import GenericResponse

IP = "192.168.192.126:1880"

router = APIRouter()


@router.get("/oscilloscope/status")
async def setupCommand(
    channel: str # Value of this parameter is only "1" or "2"
):
    try:
        link = f"http://{IP}/oscilloscope/status?channel={channel}"
        request = requests.get(link)
        return request.json()
    except Exception as e:
        return GenericResponse(status=500, details=f"Ошибка! {e}")


@router.get("/oscilloscope/command")
async def setupCommand(
    action: str,
    channel: str,  # Value of this parameter is only "1" or "2"
    display: str | None = None  # Value of this parameter is only "ON" or "OFF"
):
    try:
        request: Response
        link = f"http://{IP}/generator/command?"
        match action:
            case "display":
                request = requests.get(f"{link}channel={channel}&display={display}")
            case "autoset":
                request = requests.get(f"{link}autoset")
            case _:
                return GenericResponse(status=400, details="Неправильный запрос")
        return request.json()
    except Exception as e:
        return GenericResponse(status=500, details=f"Ошибка! {e}")
