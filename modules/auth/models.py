from pydantic import BaseModel


class GenericResponse(BaseModel):
    status: int = 200
    details: str = "Success"


class Token(BaseModel):
    token: str


class User(BaseModel):
    username: str


class UserPassword(User):
    password: str


class UserInformation(User):
    full_name: str
    group: str | None = None


class UserInformationOut(GenericResponse):
    user: UserInformation
