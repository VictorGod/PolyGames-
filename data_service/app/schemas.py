from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    game_id: int
    rating: int
    text: str

class ReviewCreate(ReviewBase):
    user_id: int

class Review(ReviewBase):
    id: int
    user: User

    class Config:
        orm_mode = True

class GameBase(BaseModel):
    title: str
    description: str

class GameCreate(GameBase):
    creator_id: int

class Game(GameBase):
    id: int
    creator: Optional[User]

    class Config:
        orm_mode = True

class ProfileBase(BaseModel):
    bio: str

class ProfileCreate(ProfileBase):
    user_id: int

class Profile(ProfileBase):
    id: int
    user: User

    class Config:
        orm_mode = True
