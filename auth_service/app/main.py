from fastapi import FastAPI
from app.endpoints import register, login
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(register.router, prefix="/auth", tags=["Register"])
app.include_router(login.router, prefix="/auth", tags=["Login"])
