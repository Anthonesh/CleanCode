# CleanCode

# Médiathèque API – EPSI Quality Code

API REST complète pour la gestion d'une médiathèque (utilisateurs, ressources, emprunts), réalisée en **Python FastAPI** + **PostgreSQL**.

## Sommaire

- [Description](#description)
- [Fonctionnalités](#fonctionnalités)
- [Structure du projet](#structure-du-projet)
- [Guide de démarrage rapide](#guide-de-démarrage-rapide)
- [Données de démonstration (Fixtures)](#données-de-démonstration-fixtures)
- [Qualité du code & SonarQube](#qualité-du-code--sonarqube)
- [Respect du cahier des charges](#respect-du-cahier-des-charges)
- [Auteurs](#auteurs)

---

## Description

Cette API permet de :
- Gérer les utilisateurs de la médiathèque
- Gérer les ressources (livres, films, jeux vidéo, etc.)
- Permettre l'emprunt et la restitution des ressources

Toutes les entités sont identifiées par un UUID (jamais d’ID auto-incrément SQL exposé).

---

## Fonctionnalités

### 1. Gestion des utilisateurs
- Création, consultation, modification, suppression
- Champs : id (UUID), nom, prénom, mail (unique), téléphone (tous formats), nationalité

### 2. Gestion des ressources
- Création, consultation (filtrage par type/disponibilité), modification, suppression
- Champs : id (UUID), titre, type (`Livre`, `Film`, `Jeu`, `Autre`), auteur/créateur, disponible

### 3. Système d’emprunt
- Un utilisateur peut emprunter une ou plusieurs ressources disponibles
- Mise à jour de l’état de disponibilité de la ressource
- Enregistrement des dates d’emprunt et de restitution (format : **JJ-MM-AAAA**)
- Restitution (remettre à disposition et supprimer/clore l’emprunt)

### 4. Documentation interactive
- **Swagger UI** disponible sur `/docs` ([localhost:8000/docs](http://localhost:8000/docs))

---

## Structure du projet

├── App/  
│ ├── init.py  
│ ├── main.py # Point d'entrée FastAPI  
│ ├── models.py # Modèles SQLAlchemy  
│ ├── schemas.py # Schémas Pydantic  
│ ├── database.py # Connexion et session DB  
│ ├── routers/ # Dossiers pour routes users/ressources/emprunts  
│ └── fixtures.py # Remplissage de la base (données exemples)  
├── requirements.txt  
├── README.md  
├── sonar-project.properties  


---

## Guide de démarrage rapide

### Prérequis

- Python 3.10+
- PostgreSQL (ou autre DB compatible)
- [Docker](https://www.docker.com/) (pour SonarQube)

### Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/Anthonesh/CleanCode.git
cd CleanCode

# 2. Installer les dépendances
python -m venv venv
source venv/bin/activate      # ou venv\Scripts\activate sous Windows
pip install -r requirements.txt

# 3. Paramétrer la base de données (voir database.py)

# 4. Lancer la migration (si Alembic) OU créer les tables automatiquement
python -m App.models

# 5. Remplir la base avec les données d'exemple
python -m App.fixtures

# 6. Lancer l'API
uvicorn App.main:app --reload

# Accéder à l'API
[http://localhost:8000/docs] #(Swagger)
