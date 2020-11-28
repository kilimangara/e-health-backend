from sqlalchemy import Column, Integer, String

from app.db.base import Base


class ImageBlobDBModel(Base):
    __tablename__ = "imageBlob"

    id = Column(Integer, primary_key=True)
    analysis_id = Column(Integer, index=True)
    filename = Column(String, nullable=False)
    check_sum = Column(String, nullable=False)
    content_type = Column(String, nullable=True)
    byte_size = Column(Integer, nullable=False)
    position = Column(Integer, nullable=False)
