from pydantic import BaseModel

class Status(BaseModel):
    status = {"capacity": {"capacity1": None, "capacity2": None}, "coord": None}