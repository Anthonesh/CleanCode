from fastapi import FastAPI
from App.routers import users, ressources, emprunts
from App import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Médiathèque API",
    description="API pour gérer une médiathèque (utilisateurs, ressources, emprunts)",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(ressources.router)
app.include_router(emprunts.router)
