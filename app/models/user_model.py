from sqlalchemy import Column, Integer, String
from app.db.database import Base


class User(Base):
    """
    Database model for users.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
