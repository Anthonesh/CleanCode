# app/crud.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from App import models, schemas

# ----- USERS -----

def create_user(db: Session, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.mail == user.mail).first()
    if db_user:
        raise ValueError("Email déjà enregistré")
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: str, user: schemas.UserCreate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: str):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user

# ----- RESSOURCES -----

def create_ressource(db: Session, ressource: schemas.RessourceCreate):
    new_ressource = models.Ressource(**ressource.dict(), disponible=True)
    db.add(new_ressource)
    db.commit()
    db.refresh(new_ressource)
    return new_ressource

def get_ressource(db: Session, ressource_id: str):
    return db.query(models.Ressource).filter(models.Ressource.id == ressource_id).first()

def get_ressources(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ressource).offset(skip).limit(limit).all()

def update_ressource(db: Session, ressource_id: str, ressource: schemas.RessourceCreate):
    db_ressource = get_ressource(db, ressource_id)
    if not db_ressource:
        return None
    for key, value in ressource.dict().items():
        setattr(db_ressource, key, value)
    db.commit()
    db.refresh(db_ressource)
    return db_ressource

def delete_ressource(db: Session, ressource_id: str):
    db_ressource = get_ressource(db, ressource_id)
    if not db_ressource:
        return None
    db.delete(db_ressource)
    db.commit()
    return db_ressource

# ----- EMPRUNTS -----

def create_emprunt(db: Session, emprunt: schemas.EmpruntCreate):
    # Check user and ressource existence
    user = get_user(db, emprunt.user_id)
    ressource = get_ressource(db, emprunt.ressource_id)
    if not user:
        raise ValueError("Utilisateur non trouvé")
    if not ressource:
        raise ValueError("Ressource non trouvée")
    if not ressource.disponible:
        raise ValueError("Ressource déjà empruntée")

    new_emprunt = models.Emprunt(**emprunt.dict())
    db.add(new_emprunt)
    # Update ressource availability
    ressource.disponible = False
    db.commit()
    db.refresh(new_emprunt)
    return new_emprunt

def rendre_emprunt(db: Session, emprunt_id: str):
    emprunt = db.query(models.Emprunt).filter(models.Emprunt.id == emprunt_id).first()
    if not emprunt:
        return None
    ressource = get_ressource(db, emprunt.ressource_id)
    if ressource:
        ressource.disponible = True
    db.delete(emprunt)
    db.commit()
    return emprunt

def get_emprunt(db: Session, emprunt_id: str):
    return db.query(models.Emprunt).filter(models.Emprunt.id == emprunt_id).first()

def get_emprunts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Emprunt).offset(skip).limit(limit).all()

def get_emprunts_by_user(db: Session, user_id: str):
    return db.query(models.Emprunt).filter(models.Emprunt.user_id == user_id).all()
