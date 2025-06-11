from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.ressource import Ressource as RessourceModel
from app.schemas.ressource import RessourceCreate

class RessourceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, ressource_in: RessourceCreate) -> RessourceModel:
        res = RessourceModel(**ressource_in.dict(), disponible=True)
        self.db.add(res)
        self.db.commit()
        self.db.refresh(res)
        return res

    def get(self, ressource_id: str) -> Optional[RessourceModel]:
        return (
            self.db
            .query(RessourceModel)
            .filter(RessourceModel.id == ressource_id)
            .first()
        )

    def list(self, skip: int = 0, limit: int = 100) -> List[RessourceModel]:
        return (
            self.db
            .query(RessourceModel)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def update(self, res: RessourceModel, res_in: RessourceCreate) -> RessourceModel:
        for key, value in res_in.dict().items():
            setattr(res, key, value)
        self.db.commit()
        self.db.refresh(res)
        return res

    def delete(self, res: RessourceModel) -> None:
        self.db.delete(res)
        self.db.commit()
