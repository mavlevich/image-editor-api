from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from passlib.context import CryptContext
from typing import Optional


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user_data: UserCreate) -> UserResponse:
    """
    Create a new user with hashed password.
    """
    hashed_password = pwd_context.hash(user_data.password)
    new_user = User(username=user_data.username, email=user_data.email, password_hash=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return UserResponse(id=new_user.id, username=new_user.username, email=new_user.email)


def get_user_by_id(db: Session, user_id: int) -> Optional[UserResponse]:
    """
    Retrieve user by ID.
    """
    user = db.query(User).filter(User.id == user_id).first()
    return user if user else None


def update_user(db: Session, user_id: int, user_data: UserUpdate) -> Optional[UserResponse]:
    """
    Update user details.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    if user_data.username:
        user.username = user_data.username
    if user_data.email:
        user.email = user_data.email

    db.commit()
    db.refresh(user)

    return UserResponse(id=user.id, username=user.username, email=user.email)


def delete_user(db: Session, user_id: int) -> bool:
    """
    Delete a user from the database.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return False

    db.delete(user)
    db.commit()
    return True
