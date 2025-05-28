from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date
from enum import Enum


class UserBase(BaseModel):
    nom: str
    prenom: str
    mail: EmailStr
    numero_telephone: str
    nationalite: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: str

    class Config:
        orm_mode = True

class RessourceBase(BaseModel):
    titre: str
    type: str
    auteur: str

class RessourceCreate(RessourceBase):
    pass

class Ressource(RessourceBase):
    id: str
    disponible: bool

    class Config:
        orm_mode = True

class EmpruntBase(BaseModel):
    user_id: str
    ressource_id: str
    date_emprunt: date
    date_retour: date

class EmpruntCreate(EmpruntBase):
    pass

class Emprunt(EmpruntBase):
    id: str

    class Config:
        orm_mode = True
        json_encoders = {
            date: lambda v: v.strftime("%d-%m-%Y") if v else None
        }

class RessourceType(str, Enum):
    livre = "Livre"
    film = "Film"
    jeu = "Jeu"
    autre = "Autre"

class RessourceBase(BaseModel):
    titre: str
    type: RessourceType 
    auteur: str
