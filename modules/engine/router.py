from fastapi import APIRouter
import requests
from models import Status

router = APIRouter()

status = Status()

@router.get("/setup/status")
async def getStatus():
    request = requests.get("/setup/status")
    return request
