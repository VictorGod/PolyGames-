from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Profile)
def create_profile(profile: schemas.ProfileCreate, db: Session = Depends(database.get_db)):
    return crud.create_profile(db, user_id=profile.user_id, bio=profile.bio)

@router.get("/{profile_id}", response_model=schemas.Profile)
def get_profile(profile_id: int, db: Session = Depends(database.get_db)):
    db_profile = crud.get_profile(db, profile_id)
    if db_profile:
        return db_profile
    raise HTTPException(status_code=404, detail="Profile not found")

@router.get("/", response_model=list[schemas.Profile])
def get_all_profiles(db: Session = Depends(database.get_db)):
    return crud.get_all_profiles(db)

@router.put("/{profile_id}", response_model=schemas.Profile)
def update_profile(profile_id: int, profile: schemas.ProfileBase, db: Session = Depends(database.get_db)):
    db_profile = crud.update_profile(db, profile_id, bio=profile.bio)
    if db_profile:
        return db_profile
    raise HTTPException(status_code=404, detail="Profile not found")
