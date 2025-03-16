from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    """
    Base schema for users.
    """
    username: str
    email: str


class UserCreate(UserBase):
    """
    Schema for user registration.
    """
    password: str


class UserUpdate(BaseModel):
    """
    Schema for updating user data.
    """
    username: Optional[str] = None
    email: Optional[str] = None


class UserResponse(UserBase):
    """
    Schema for returning user data.
    """
    id: int

    class Config:
        orm_mode = True
