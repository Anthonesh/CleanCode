from pydantic import BaseModel, EmailStr

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
