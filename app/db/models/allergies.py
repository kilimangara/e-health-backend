from sqlalchemy import Column, Integer, String, Date

from app.db.base import Base


class Allergies(Base):
    __tablename__ = "allergies"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    allergen = Column(String, nullable=False)
    reaction = Column(String, nullable=False)
