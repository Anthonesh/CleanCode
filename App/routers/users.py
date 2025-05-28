from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from App import schemas, crud, database

USER_NOT_FOUND = "Utilisateur non trouvé"

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[schemas.User])
def list_users(skip: int = 0, limit: int = Query(100, le=1000), db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)

@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=USER_NOT_FOUND)
    return user

@router.put("/{user_id}", response_model=schemas.User)
def update_user(user_id: str, user: schemas.UserCreate, db: Session = Depends(get_db)):
    updated = crud.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail=USER_NOT_FOUND)
    return updated

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=USER_NOT_FOUND)
