from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserResponse
from typing import Optional
from passlib.context import CryptContext

# Password hashing settings
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# In-memory storage (replace with database)
fake_users_db = {}


def get_user(username: str) -> Optional[User]:
    """
    Retrieve a user from the database (mocked storage).
    """
    return fake_users_db.get(username)


def create_user(user_data: UserCreate) -> UserResponse:
    """
    Create a new user with a hashed password.
    """
    hashed_password = pwd_context.hash(user_data.password)
    new_user = User(username=user_data.username, password_hash=hashed_password)

    # Save user (mocked)
    fake_users_db[user_data.username] = new_user

    return UserResponse(username=new_user.username)


def authenticate_user(username: str, password: str) -> Optional[UserResponse]:
    """
    Authenticate a user by verifying the password.
    """
    user = get_user(username)
    if not user or not pwd_context.verify(password, user.password_hash):
        return None
    return UserResponse(username=user.username)
