from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.db.base import Base


class AnalysisDBModel(Base):
    __tablename__ = "analysis"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now(), index=False)
    category_id = Column(Integer, index=True)
    comment = Column(String, index=False)
