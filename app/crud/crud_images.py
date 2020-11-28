from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models.image import ImageBlobDBModel
from app.schemas.image import ImageDataCreateModel, ImageDataUpdateModel


class CRUDImages(
    CRUDBase[ImageBlobDBModel, ImageDataCreateModel, ImageDataUpdateModel]
):
    async def get_by_analysis_id(
        self, db: Session, analysis_id: int
    ) -> List[ImageBlobDBModel]:
        return db.query(ImageBlobDBModel).filter(
            ImageBlobDBModel.analysis_id == analysis_id
        )

    async def add_list(self, db: Session, data_in: List[ImageBlobDBModel]):
        db.add_all(data_in)
        db.commit()
        for obj in data_in:
            db.refresh(obj)
        return data_in


images = CRUDImages(ImageBlobDBModel)
