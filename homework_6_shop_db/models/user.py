from pydantic import BaseModel, Field, EmailStr


class UserIn(BaseModel):
    username: str = Field(..., max_length=50)
    email: EmailStr = Field(..., min_length=5)
    password: str = Field(..., min_length=3)


class User(BaseModel):
    id: int
    username: str = Field(..., max_length=50)
    email: EmailStr = Field(..., min_length=3)