from sqlalchemy import Column, Date, Integer, String, DateTime

from app.db.base import Base
from datetime import datetime

STATUS_CREATED = "created"
STATUS_APPROVED = "approved"


class UsersDBModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, nullable=False, index=True)
    status = Column(String, nullable=False)
    name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    blood_type = Column(String, nullable=True)
    birth_date = Column(Date, nullable=True)
    weight = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())

    def to_dict(self):
        """Преобразование объекта к словарю."""
        return {
            "name": self.name,
            "phone": self.phone,
            "blood_type": self.blood_type,
            "birth_date": self.birth_date,
            "last_name": self.last_name,
            "weight": self.weight,
            "height": self.height,
        }
