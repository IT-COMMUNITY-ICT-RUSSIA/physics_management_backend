import requests
from fastapi import APIRouter
from requests import Response

from modules.board.models import GenericResponse

IP = "192.168.192.126:1880"

router = APIRouter()


@router.get("/generator/command")
async def setupCommand(
    channel: str,
    action: str,
    launching: str | None = None,
    vpp: float | None = None,
    freq: int | None = None,
    form: str | None = None
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
                return GenericResponse(status=400, details="Wrong request")
        return request.json()
    except Exception as e:
        return GenericResponse(status=500, details=f"Ошибка! {e}")
