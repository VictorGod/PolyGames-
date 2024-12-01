from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Game)
def create_game(game: schemas.GameCreate, db: Session = Depends(database.get_db)):
    return crud.create_game(db, title=game.title, description=game.description, creator_id=game.creator_id)

@router.get("/{game_id}", response_model=schemas.Game)
def get_game(game_id: int, db: Session = Depends(database.get_db)):
    db_game = crud.get_game(db, game_id)
    if db_game:
        return db_game
    raise HTTPException(status_code=404, detail="Game not found")

@router.get("/", response_model=list[schemas.Game])
def get_all_games(db: Session = Depends(database.get_db)):
    return crud.get_all_games(db)

@router.put("/{game_id}", response_model=schemas.Game)
def update_game(game_id: int, game: schemas.GameBase, db: Session = Depends(database.get_db)):
    db_game = crud.update_game(db, game_id, title=game.title, description=game.description)
    if db_game:
        return db_game
    raise HTTPException(status_code=404, detail="Game not found")

@router.delete("/{game_id}")
def delete_game(game_id: int, db: Session = Depends(database.get_db)):
    db_game = crud.delete_game(db, game_id)
    if db_game:
        return {"detail": "Game deleted successfully"}
    raise HTTPException(status_code=404, detail="Game not found")
