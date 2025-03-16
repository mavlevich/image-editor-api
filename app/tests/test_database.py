from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base


TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_test_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_test_db():
    Base.metadata.create_all(bind=engine)
