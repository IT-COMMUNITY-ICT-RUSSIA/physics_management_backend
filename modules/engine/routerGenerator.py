import requests
from fastapi import APIRouter
from requests import Response

from modules.board.models import GenericResponse

IP = "192.168.192.126:1880"

router = APIRouter()


@router.get("/generator/command")
async def setupCommand(
    channel: str, # Value of this parameter is only "1" or "2"
    action: str,
    launching: str | None = None,  # Value of this parameter is only "ON" or "OFF"
    vpp: float | None = None,  # Value of this parameter is only between 0.0 and 10.0
    freq: int | None = None,  # Value of this parameter is only between 0 and 2000000
    form: str | None = None  # Value of this parameter is only "SINE"/"SQUARE"/"RAMP"/"PULSE"/"NOISE"/"ARB"
):
    try:
        request: Response
        link = f"http://{IP}/generator/command?channel={channel}"
        match action:
            case "output":
                request = requests.get(f"{link}&output={launching}")
            case "vpp":
                request = requests.get(f"{link}&vpp={vpp}")
            case "freq":
                request = requests.get(f"{link}&freq={freq}")
            case "form":
                request = requests.get(f"{link}&form={form}")
            case _:
                return GenericResponse(status=400, details="Неправильный запрос")
        return request.json()
    except Exception as e:
        return GenericResponse(status=500, details=f"Ошибка! {e}")
