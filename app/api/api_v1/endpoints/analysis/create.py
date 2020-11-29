from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_current_user, get_db
from app.db.models.user import UsersDBModel
from app.schemas.analysis import AnalysisCreateRequestModel

router = APIRouter()


@router.post("/create")
async def create_analysis(
    request_data: AnalysisCreateRequestModel,
    current_user: UsersDBModel = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    db_create_model = request_data.to_db_create_model(current_user.id)

    if not await crud.images.check_count_by_keys(
        db, current_user.id, request_data.images_to_link
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Images does not belong to user",
        )

    analysis = await crud.analysis.create(db, obj_in=db_create_model)
    await crud.images.link_to_analysis(db, analysis.id, request_data.images_to_link)

    return {"result": {"analysis_id": analysis.id}}
