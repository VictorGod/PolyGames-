from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user:
        return db_user
    raise HTTPException(status_code=404, detail="User not found")
