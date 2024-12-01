from sqlalchemy.orm import Session
from app import models

# CRUD для пользователей (только чтение)
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# CRUD для игр
def create_game(db: Session, title: str, description: str, creator_id: int):
    db_game = models.Game(title=title, description=description, creator_id=creator_id)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def get_game(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()

def get_all_games(db: Session):
    return db.query(models.Game).all()

def update_game(db: Session, game_id: int, title: str, description: str):
    db_game = get_game(db, game_id)
    if db_game:
        db_game.title = title
        db_game.description = description
        db.commit()
        db.refresh(db_game)
    return db_game

def delete_game(db: Session, game_id: int):
    db_game = get_game(db, game_id)
    if db_game:
        db.delete(db_game)
        db.commit()
    return db_game

# CRUD для отзывов
def create_review(db: Session, user_id: int, game_id: int, rating: int, text: str):
    db_review = models.Review(user_id=user_id, game_id=game_id, rating=rating, text=text)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_review(db: Session, review_id: int):
    return db.query(models.Review).filter(models.Review.id == review_id).first()

def get_reviews_by_game(db: Session, game_id: int):
    return db.query(models.Review).filter(models.Review.game_id == game_id).all()

def get_reviews_by_rating(db: Session, rating: int):
    return db.query(models.Review).filter(models.Review.rating == rating).all()

def delete_review(db: Session, review_id: int):
    db_review = get_review(db, review_id)
    if db_review:
        db.delete(db_review)
        db.commit()
    return db_review

# CRUD для профилей
def create_profile(db: Session, user_id: int, bio: str):
    db_profile = models.Profile(user_id=user_id, bio=bio)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_profile(db: Session, profile_id: int):
    return db.query(models.Profile).filter(models.Profile.id == profile_id).first()

def get_all_profiles(db: Session):
    return db.query(models.Profile).all()

def update_profile(db: Session, profile_id: int, bio: str):
    db_profile = get_profile(db, profile_id)
    if db_profile:
        db_profile.bio = bio
        db.commit()
        db.refresh(db_profile)
    return db_profile
