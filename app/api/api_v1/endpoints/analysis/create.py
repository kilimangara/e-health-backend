from fastapi import APIRouter, Depends
from app import crud
from sqlalchemy.orm import Session
from app.schemas.analysis import AnalysisCreateRequestModel
from app.api.deps import get_current_user, get_db
from app.db.models.user import UsersDBModel


router = APIRouter()


@router.post('/create')
async def create_analysis(
    request_data: AnalysisCreateRequestModel,
    current_user: UsersDBModel = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    db_create_model = request_data.to_db_create_model(current_user.id)
    analysis = await crud.analysis.create(db, obj_in=db_create_model)
    await crud.images.link_to_analysis(db, analysis.id, request_data.images_to_link)

    return {"result": {"analysis_id": analysis.id}}
