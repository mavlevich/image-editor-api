from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserLogin
from app.services.auth_service import authenticate_user
from app.db.database import get_db


router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login/")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    """
    Authenticate a user and return a token.
    """
    token = authenticate_user(db, user_data.username, user_data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"token": token}
