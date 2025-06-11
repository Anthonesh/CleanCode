from typing import List
from sqlalchemy.orm import Session
from app.repositories.emprunt import EmpruntRepository
from app.repositories.user import UserRepository
from app.repositories.ressource import RessourceRepository
from app.schemas.emprunt import EmpruntCreate, Emprunt

class EmpruntService:
    def __init__(self, db: Session):
        self.empr_repo = EmpruntRepository(db)
        self.user_repo = UserRepository(db)
        self.res_repo = RessourceRepository(db)

    def list_emprunts(self) -> List[Emprunt]:
        all_e = self.empr_repo.list()
        return [Emprunt.from_orm(e) for e in all_e]

    def create_emprunt(self, empr_in: EmpruntCreate) -> Emprunt:
        # Validation existence
        user = self.user_repo.get(empr_in.user_id)
        if not user:
            raise ValueError("Utilisateur non trouvé")
        res = self.res_repo.get(empr_in.ressource_id)
        if not res:
            raise ValueError("Ressource non trouvée")
        if not res.disponible:
            raise ValueError("Ressource déjà empruntée")
        # Création
        e = self.empr_repo.create(empr_in)
        # Mise à jour dispo
        res.disponible = False
        # flush & commit gérés par repo.create + commit explicite si besoin
        return Emprunt.from_orm(e)

    def rendre_emprunt(self, empr_id: str) -> Emprunt:
        e = self.empr_repo.get(empr_id)
        if not e:
            raise ValueError("Emprunt non trouvé")
        # Remise à dispo
        res = self.res_repo.get(e.ressource_id)
        if res:
            res.disponible = True
        # Suppression de l’emprunt
        self.empr_repo.delete(e)
        return Emprunt.from_orm(e)
