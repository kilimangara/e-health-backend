from sqlalchemy import Column, Integer, String, Date

from app.db.base import Base

# if TYPE_CHECKING:
#     from .item import Item  # noqa: F401

STATUS_CREATED = "created"
STATUS_APPROVED = "approved"


class Users(Base):
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
