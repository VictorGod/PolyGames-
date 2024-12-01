from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(database.get_db)):
    return crud.create_review(db, user_id=review.user_id, game_id=review.game_id, rating=review.rating, text=review.text)

@router.get("/{review_id}", response_model=schemas.Review)
def get_review(review_id: int, db: Session = Depends(database.get_db)):
    db_review = crud.get_review(db, review_id)
    if db_review:
        return db_review
    raise HTTPException(status_code=404, detail="Review not found")

@router.get("/game/{game_id}", response_model=list[schemas.Review])
def get_reviews_by_game(game_id: int, db: Session = Depends(database.get_db)):
    return crud.get_reviews_by_game(db, game_id)

@router.get("/rating/{rating}", response_model=list[schemas.Review])
def get_reviews_by_rating(rating: int, db: Session = Depends(database.get_db)):
    return crud.get_reviews_by_rating(db, rating)

@router.delete("/{review_id}")
def delete_review(review_id: int, db: Session = Depends(database.get_db)):
    db_review = crud.delete_review(db, review_id)
    if db_review:
        return {"detail": "Review deleted successfully"}
    raise HTTPException(status_code=404, detail="Review not found")
