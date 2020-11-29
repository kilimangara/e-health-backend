from app.crud.base import CRUDBase
from app.db.models.analysis import AnalysisDBModel
from app.schemas.analysis import AnalysisCreateModel


class CRUDAnalysis(
    CRUDBase[AnalysisDBModel, AnalysisCreateModel, AnalysisCreateModel]
):
    pass

analysis = CRUDAnalysis(AnalysisDBModel)
