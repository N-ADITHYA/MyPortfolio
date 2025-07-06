import datetime

from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    name: str
    email: EmailStr
    message: str

    class Config:
        from_attributes = True

class PostCreate(CreateUser):
    id: int
    timestamp: datetime.datetime

    class Config:
        from_attributes = True