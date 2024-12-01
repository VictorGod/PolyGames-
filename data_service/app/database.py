from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://auth_user:secure_password@localhost/auth_service"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Получение сессии для взаимодействия с БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
