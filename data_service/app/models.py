from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"  
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)
    hashed_password = Column(String) 

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    games_participated = Column(String)
    achievements = Column(Text)
    bio = Column(Text)

    user = relationship("User", back_populates="profile")

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    genre = Column(String)
    platform = Column(String)
    download_link = Column(String)
    jam_participant = Column(Boolean)
    jam_winner = Column(Boolean)
    creator_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User")
    reviews = relationship("Review", back_populates="game")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    game_id = Column(Integer, ForeignKey("games.id"))
    rating = Column(Integer)
    review_text = Column(Text)

    user = relationship("User", back_populates="reviews")
    game = relationship("Game", back_populates="reviews")
