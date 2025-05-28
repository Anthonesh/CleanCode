from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import uuid

def gen_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=gen_uuid)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    mail = Column(String, nullable=False, unique=True)
    numero_telephone = Column(String, nullable=False)
    nationalite = Column(String, nullable=False)
    emprunts = relationship("Emprunt", back_populates="user")

class Ressource(Base):
    __tablename__ = "ressources"
    id = Column(String, primary_key=True, default=gen_uuid)
    titre = Column(String, nullable=False)
    type = Column(String, nullable=False)
    auteur = Column(String, nullable=False)
    disponible = Column(Boolean, default=True)
    emprunts = relationship("Emprunt", back_populates="ressource")

class Emprunt(Base):
    __tablename__ = "emprunts"
    id = Column(String, primary_key=True, default=gen_uuid)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    ressource_id = Column(String, ForeignKey('ressources.id'), nullable=False)
    date_emprunt = Column(Date, nullable=False)
    date_retour = Column(Date, nullable=False)
    user = relationship("User", back_populates="emprunts")
    ressource = relationship("Ressource", back_populates="emprunts")
