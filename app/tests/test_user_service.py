import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.user_model import Base, User
from app.services.user_service import create_user, get_user_by_id, update_user, delete_user
from app.schemas.user_schema import UserCreate, UserUpdate

# Create an in-memory SQLite database for the tests
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Fixture for base and session creation
@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)  # Create tables
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)  # Delete tables after tests


def test_create_user(db_session):
    user_data = UserCreate(username="testuser", email="test@example.com", password="password123")
    user = create_user(db_session, user_data)

    assert user.id is not None
    assert user.username == "testuser"
    assert user.email == "test@example.com"


def test_get_user_by_id(db_session):
    user_data = UserCreate(username="testuser", email="test@example.com", password="password123")
    user = create_user(db_session, user_data)

    retrieved_user = get_user_by_id(db_session, user.id)
    assert retrieved_user is not None
    assert retrieved_user.id == user.id


def test_update_user(db_session):
    user_data = UserCreate(username="testuser", email="test@example.com", password="password123")
    user = create_user(db_session, user_data)

    update_data = UserUpdate(username="updateduser", email="updated@example.com")
    updated_user = update_user(db_session, user.id, update_data)

    assert updated_user.username == "updateduser"
    assert updated_user.email == "updated@example.com"


def test_delete_user(db_session):
    user_data = UserCreate(username="testuser", email="test@example.com", password="password123")
    user = create_user(db_session, user_data)

    delete_user(db_session, user.id)
    deleted_user = get_user_by_id(db_session, user.id)

    assert deleted_user is None
