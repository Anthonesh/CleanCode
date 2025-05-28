from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from App import schemas, crud, database

router = APIRouter(
    prefix="/emprunts",
    tags=["emprunts"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Emprunt, status_code=status.HTTP_201_CREATED)
def emprunter(emprunt: schemas.EmpruntCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_emprunt(db, emprunt)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[schemas.Emprunt])
def list_emprunts(skip: int = 0, limit: int = Query(100, le=1000), db: Session = Depends(get_db)):
    return crud.get_emprunts(db, skip, limit)

@router.get("/{emprunt_id}", response_model=schemas.Emprunt)
def get_emprunt(emprunt_id: str, db: Session = Depends(get_db)):
    emprunt = crud.get_emprunt(db, emprunt_id)
    if not emprunt:
        raise HTTPException(status_code=404, detail="Emprunt non trouvé")
    return emprunt

@router.delete("/{emprunt_id}", status_code=status.HTTP_204_NO_CONTENT)
def rendre_emprunt(emprunt_id: str, db: Session = Depends(get_db)):
    rendu = crud.rendre_emprunt(db, emprunt_id)
    if not rendu:
        raise HTTPException(status_code=404, detail="Emprunt non trouvé")
    return

@router.get("/user/{user_id}", response_model=list[schemas.Emprunt])
def list_emprunts_by_user(user_id: str, db: Session = Depends(get_db)):
    return crud.get_emprunts_by_user(db, user_id)
