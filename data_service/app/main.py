from fastapi import FastAPI
from app.endpoints import users, games, reviews, profiles
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(games.router, prefix="/games", tags=["Games"])
app.include_router(reviews.router, prefix="/reviews", tags=["Reviews"])
app.include_router(profiles.router, prefix="/profiles", tags=["Profiles"])
