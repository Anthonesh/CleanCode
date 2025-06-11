# app/api/routers/emprunt.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from app.schemas.emprunt import EmpruntCreate, Emprunt
from app.services.emprunt import EmpruntService
from app.api.dependencies import get_emprunt_service

router = APIRouter(tags=["emprunts"])

@router.post("/", response_model=Emprunt, status_code=status.HTTP_201_CREATED)
def emprunter(
    empr_in: EmpruntCreate,
    service: EmpruntService = Depends(get_emprunt_service)
) -> Emprunt:
    try:
        return service.create_emprunt(empr_in)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/", response_model=List[Emprunt])
def list_emprunts(
    skip: int = 0,
    limit: int = 100,
    service: EmpruntService = Depends(get_emprunt_service)
) -> List[Emprunt]:
    return service.list_emprunts(skip=skip, limit=limit)

@router.get("/{emprunt_id}", response_model=Emprunt)
def get_emprunt(
    empr_id: str,
    service: EmpruntService = Depends(get_emprunt_service)
) -> Emprunt:
    empr = service.get_emprunt(empr_id)
    if not empr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Emprunt non trouvé")
    return empr

@router.delete("/{emprunt_id}", status_code=status.HTTP_204_NO_CONTENT)
def rendre_emprunt(
    empr_id: str,
    service: EmpruntService = Depends(get_emprunt_service)
):
    try:
        service.rendre_emprunt(empr_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
