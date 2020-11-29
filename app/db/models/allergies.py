from sqlalchemy import Column, Integer, String, DateTime

from app.db.base import Base
from datetime import datetime


class AllergyDBModel(Base):
    __tablename__ = "allergies"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    allergen = Column(String, nullable=False)
    reaction = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())

    def to_dict(self):
        """Приведение объекта к словарю."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "reaction": self.reaction,
            "allergen": self.allergen,
        }
