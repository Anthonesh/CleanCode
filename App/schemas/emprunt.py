from pydantic import BaseModel
from datetime import date

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
