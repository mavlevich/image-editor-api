from pydantic import BaseModel


class UserBase(BaseModel):
    """
    Base schema for users.
    """
    username: str


class UserCreate(UserBase):
    """
    Schema for user registration.
    """
    password: str


class UserResponse(UserBase):
    """
    Schema for returning user data.
    """
    id: int

    class Config:
        orm_mode = True
