from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from App import schemas, crud, database
from typing import Optional
from App.schemas import RessourceType

router = APIRouter(
    prefix="/ressources",
    tags=["ressources"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Ressource, status_code=status.HTTP_201_CREATED)
def create_ressource(ressource: schemas.RessourceCreate, db: Session = Depends(get_db)):
    return crud.create_ressource(db, ressource)

@router.get("/", response_model=list[schemas.Ressource])
def list_ressources(
    type: Optional[RessourceType] = Query(None, description="Filtrer par type de ressource"),
    disponible: Optional[bool] = Query(None, description="Filtrer par disponibilité"),
    skip: int = 0,
    limit: int = Query(100, le=1000),
    db: Session = Depends(get_db)
):
    query = db.query(crud.models.Ressource)
    if type:
        query = query.filter(crud.models.Ressource.type == type.value)
    if disponible is not None:
        query = query.filter(crud.models.Ressource.disponible == disponible)
    return query.offset(skip).limit(limit).all()

@router.get("/{ressource_id}", response_model=schemas.Ressource)
def get_ressource(ressource_id: str, db: Session = Depends(get_db)):
    ressource = crud.get_ressource(db, ressource_id)
    if not ressource:
        raise HTTPException(status_code=404, detail="Ressource non trouvée")
    return ressource

@router.put("/{ressource_id}", response_model=schemas.Ressource)
def update_ressource(ressource_id: str, ressource: schemas.RessourceCreate, db: Session = Depends(get_db)):
    updated = crud.update_ressource(db, ressource_id, ressource)
    if not updated:
        raise HTTPException(status_code=404, detail="Ressource non trouvée")
    return updated

@router.delete("/{ressource_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ressource(ressource_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_ressource(db, ressource_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Ressource non trouvée")
    return
