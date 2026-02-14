from pydantic import BaseModel, ConfigDict
from typing import Optional


# -------------------- STUDENT SCHEMAS --------------------

class StudentBase(BaseModel):
    name: str
    email: str
    age: int
    course: str


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    course: Optional[str] = None


class StudentResponse(StudentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


# -------------------- AUTH SCHEMAS --------------------

class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

    model_config = ConfigDict(from_attributes=True)
