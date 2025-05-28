from App.database import SessionLocal, engine
from App import models
import uuid

models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

# -------------------------------
# 1. DÉCLARATION DES DONNÉES
# -------------------------------

users_data = [
    {"nom": "Dupont", "prenom": "Jean", "mail": "jean.dupont@mail.com", "numero_telephone": "+33601020304", "nationalite": "Française"},
    {"nom": "Martin", "prenom": "Alice", "mail": "alice.martin@mail.com", "numero_telephone": "+32477112233", "nationalite": "Belge"},
    {"nom": "Garcia", "prenom": "Pablo", "mail": "pablo.garcia@mail.com", "numero_telephone": "+34911223344", "nationalite": "Espagnole"},
    {"nom": "Smith", "prenom": "Emily", "mail": "emily.smith@mail.com", "numero_telephone": "+447700900123", "nationalite": "Anglaise"},
    {"nom": "Nguyen", "prenom": "Minh", "mail": "minh.nguyen@mail.com", "numero_telephone": "+84912345678", "nationalite": "Vietnamienne"},
    {"nom": "Kowalski", "prenom": "Anna", "mail": "anna.kowalski@mail.com", "numero_telephone": "+48221122334", "nationalite": "Polonaise"},
    {"nom": "Dubois", "prenom": "Lucas", "mail": "lucas.dubois@mail.com", "numero_telephone": "+33698765432", "nationalite": "Française"},
    {"nom": "Schmidt", "prenom": "Sophie", "mail": "sophie.schmidt@mail.com", "numero_telephone": "+4915112345678", "nationalite": "Allemande"},
    {"nom": "Rossi", "prenom": "Marco", "mail": "marco.rossi@mail.com", "numero_telephone": "+393491234567", "nationalite": "Italienne"},
    {"nom": "Fernandez", "prenom": "Lucia", "mail": "lucia.fernandez@mail.com", "numero_telephone": "+34611223344", "nationalite": "Espagnole"}
]

livres_data = [
    {"titre": "1984", "auteur": "George Orwell"},
    {"titre": "Le Seigneur des Anneaux", "auteur": "J.R.R. Tolkien"},
    {"titre": "Harry Potter à l'école des sorciers", "auteur": "J.K. Rowling"},
    {"titre": "Fahrenheit 451", "auteur": "Ray Bradbury"},
    {"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry"},
    {"titre": "L'Étranger", "auteur": "Albert Camus"},
    {"titre": "Les Misérables", "auteur": "Victor Hugo"},
    {"titre": "La Peste", "auteur": "Albert Camus"},
    {"titre": "Le Comte de Monte-Cristo", "auteur": "Alexandre Dumas"},
    {"titre": "Orgueil et Préjugés", "auteur": "Jane Austen"},
]

films_data = [
    {"titre": "Inception", "auteur": "Christopher Nolan"},
    {"titre": "Le Parrain", "auteur": "Francis Ford Coppola"},
    {"titre": "Pulp Fiction", "auteur": "Quentin Tarantino"},
    {"titre": "Interstellar", "auteur": "Christopher Nolan"},
    {"titre": "Forrest Gump", "auteur": "Robert Zemeckis"},
    {"titre": "La Liste de Schindler", "auteur": "Steven Spielberg"},
    {"titre": "Fight Club", "auteur": "David Fincher"},
    {"titre": "Le Fabuleux Destin d'Amélie Poulain", "auteur": "Jean-Pierre Jeunet"},
    {"titre": "Matrix", "auteur": "Les Wachowski"},
    {"titre": "Parasite", "auteur": "Bong Joon-ho"},
]

jeux_data = [
    {"titre": "The Witcher 3", "auteur": "CD Projekt"},
    {"titre": "The Legend of Zelda: Breath of the Wild", "auteur": "Nintendo"},
    {"titre": "Minecraft", "auteur": "Mojang"},
    {"titre": "Red Dead Redemption 2", "auteur": "Rockstar Games"},
    {"titre": "God of War", "auteur": "Santa Monica Studio"},
    {"titre": "Hollow Knight", "auteur": "Team Cherry"},
    {"titre": "Celeste", "auteur": "Matt Makes Games"},
    {"titre": "Super Mario Odyssey", "auteur": "Nintendo"},
    {"titre": "Dark Souls III", "auteur": "FromSoftware"},
    {"titre": "Overwatch", "auteur": "Blizzard Entertainment"},
]

# -------------------------------
# 2. INSERTION EN BASE
# -------------------------------

for u in users_data:
    user = models.User(
        id=str(uuid.uuid4()),
        nom=u["nom"],
        prenom=u["prenom"],
        mail=u["mail"],
        numero_telephone=u["numero_telephone"],
        nationalite=u["nationalite"]
    )
    db.add(user)

for l in livres_data:
    ressource = models.Ressource(
        id=str(uuid.uuid4()),
        titre=l["titre"],
        type="Livre",
        auteur=l["auteur"],
        disponible=True
    )
    db.add(ressource)

for f in films_data:
    ressource = models.Ressource(
        id=str(uuid.uuid4()),
        titre=f["titre"],
        type="Film",
        auteur=f["auteur"],
        disponible=True
    )
    db.add(ressource)

for j in jeux_data:
    ressource = models.Ressource(
        id=str(uuid.uuid4()),
        titre=j["titre"],
        type="Jeu",
        auteur=j["auteur"],
        disponible=True
    )
    db.add(ressource)

db.commit()
db.close()

print("Fixtures créées avec 10 users, 10 livres, 10 films, 10 jeux vidéo.")
