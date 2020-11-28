from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models import ImageBlob
from app.schemas.images import CreateUrls
from typing import List

class CRUDImages(CRUDBase[ImageBlob, CreateUrls, ImageBlob]):
    async def get_by_analysis_id(self, db: Session, analysis_id: int) -> List[ImageBlob]:
        return db.query(ImageBlob).filter(ImageBlob.analysis_id == analysis_id)

    async def add_list(self, db: Session, data_in: List[ImageBlob]):
        db.add_all(data_in)
        db.commit()
        for obj in data_in:
            db.refresh(obj)
        return data_in


images = CRUDImages(ImageBlob)
