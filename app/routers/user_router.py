from fastapi import APIRouter, Depends
from app.services.user_service import authenticate_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/login/")
async def login(username: str, password: str):
    """
    Authenticate user and return a token.
    """
    return authenticate_user(username, password)
