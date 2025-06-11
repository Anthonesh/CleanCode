from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from .utils import gen_uuid

class Emprunt(Base):
    __tablename__ = "emprunts"

    id = Column(String, primary_key=True, default=gen_uuid)

    # on lie au pk interne du User
    user_pk = Column(
        Integer,
        ForeignKey("users.pk", ondelete="CASCADE"),
        nullable=False
    )
    # on lie au UUID de la Ressource
    ressource_id = Column(
        String,
        ForeignKey("ressources.id", ondelete="CASCADE"),
        nullable=False
    )

    date_emprunt = Column(Date, nullable=False)
    date_retour = Column(Date, nullable=False)

    user = relationship("User", back_populates="emprunts")
    ressource = relationship("Ressource", back_populates="emprunts")
