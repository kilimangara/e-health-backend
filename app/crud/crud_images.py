from typing import List

from sqlalchemy import text
from sqlalchemy.engine import ResultProxy
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

    async def check_count_by_keys(self, db: Session, user_id: int, keys: List[int]):
        result: ResultProxy = db.execute(
            text(
                """
                SELECT count(*)
                FROM image_blob
                WHERE user_id=:user_id
                  AND id IN :keys
                  AND analysis_id IS NULL;
            """
            ),
            {"user_id": user_id, "keys": tuple(keys)},
        )
        return result.fetchone()[0] == len(keys)

    async def link_to_analysis(self, db: Session, analysis_id: int, keys: List[int]):
        db.execute(
            text(
                """
                UPDATE image_blob
                SET analysis_id=:an_id
                WHERE id IN :keys
                  AND analysis_id IS NULL;
            """
            ),
            {"an_id": analysis_id, "keys": tuple(keys)},
        )
        db.commit()


images = CRUDImages(ImageBlobDBModel)
