from pydantic import BaseModel
from enum import Enum

class RessourceType(str, Enum):
    livre = "Livre"
    film = "Film"
    jeu = "Jeu"
    autre = "Autre"

class RessourceBase(BaseModel):
    titre: str
    type: RessourceType
    auteur: str

class RessourceCreate(RessourceBase):
    pass

class Ressource(RessourceBase):
    id: str
    disponible: bool

    class Config:
        orm_mode = True
