from sqlalchemy import text
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models.analysis import AnalysisDBModel
from app.schemas.analysis import AnalysisCreateModel, AnalysisGetModel


class CRUDAnalysis(CRUDBase[AnalysisDBModel, AnalysisCreateModel, AnalysisCreateModel]):
    async def get_count_by_category(self, db: Session, user_id: int):
        return db.execute(
            text(
                "SELECT category_id, count(id) FROM analysis WHERE user_id=:user_id GROUP BY category_id;"
            ),
            {"user_id": user_id},
        ).fetchall()

    async def get_by_user_with_images(
        self, db: Session, user_id: int, req_data: AnalysisGetModel
    ):
        offset = req_data.page * req_data.limit - req_data.limit
        return db.execute(
            text(
                """
                SELECT an.created_at, an.comment, an.category_id, an.user_id, im.filename, im.content_type, im.position, im.analysis_id
                FROM analysis AS an
                JOIN image_blob AS im ON an.id = im.analysis_id
                WHERE an.id IN
                    (SELECT id
                     FROM analysis AS an2
                     WHERE an2.user_id=:user_id
                     ORDER BY an2.created_at DESC
                     LIMIT :limit
                     OFFSET :offset)
                ORDER BY an.created_at DESC;
            """
            ),
            {"user_id": user_id, "limit": req_data.limit, "offset": offset},
        ).fetchall()


analysis = CRUDAnalysis(AnalysisDBModel)
