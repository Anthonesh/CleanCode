from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.emprunt import Emprunt as EmpruntModel
from app.schemas.emprunt import EmpruntCreate

class EmpruntRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, emprunt_in: EmpruntCreate) -> EmpruntModel:
        em = EmpruntModel(**emprunt_in.dict())
        self.db.add(em)
        self.db.commit()
        self.db.refresh(em)
        return em

    def get(self, emprunt_id: str) -> Optional[EmpruntModel]:
        return (
            self.db
            .query(EmpruntModel)
            .filter(EmpruntModel.id == emprunt_id)
            .first()
        )

    def list(self, skip: int = 0, limit: int = 100) -> List[EmpruntModel]:
        return (
            self.db
            .query(EmpruntModel)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def delete(self, em: EmpruntModel) -> None:
        self.db.delete(em)
        self.db.commit()
