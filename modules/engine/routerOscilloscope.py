import requests
from fastapi import APIRouter
from requests import Response

from modules.board.models import GenericResponse

IP = "192.168.192.126:1880"

router = APIRouter()


@router.get("/setup/command2")
async def setupCommand(
    action: str,
    variable1: int,
    variable2: int | None = None
):
    try:
        request: Response
        match action:
            case "setcapacity":
                request = requests.get(f"http://{IP}/setup/command?{action}&setcapacity1={variable1}&setcapacity2={variable2}")
            case "setcoord":
                request = requests.get(f"http://{IP}/setup/command?{action}={variable1}")
            case _:
                return GenericResponse(status=400, details="Wrong request")
        return request.json()
    except Exception as e:
        return GenericResponse(status=500, details=f"Ошибка! {e}")
