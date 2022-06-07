from pydantic import BaseModel


class GenericResponse(BaseModel):
    status: int = 200
    details: str = "Success"

