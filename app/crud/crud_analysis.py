from sqlalchemy import text
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models.analysis import AnalysisDBModel
from app.schemas.analysis import AnalysisCreateModel


class CRUDAnalysis(CRUDBase[AnalysisDBModel, AnalysisCreateModel, AnalysisCreateModel]):
    async def get_count_by_category(self, db: Session, user_id: int):
        return db.execute(
            text(
                "SELECT category_id, count(id) FROM analysis WHERE user_id=:user_id GROUP BY category_id;"
            ),
            {"user_id": user_id},
        ).fetchall()


analysis = CRUDAnalysis(AnalysisDBModel)
