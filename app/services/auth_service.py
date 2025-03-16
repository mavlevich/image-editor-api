from sqlalchemy.orm import Session
from app.models.user_model import User
from passlib.context import CryptContext
import jwt
import datetime

SECRET_KEY = "your_secret_key"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def authenticate_user(db: Session, username: str, password: str):
    """
    Verify user credentials and return JWT token.
    """
    user = db.query(User).filter(User.username == username).first()
    if not user or not pwd_context.verify(password, user.password_hash):
        return None

    payload = {"sub": user.username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return token
