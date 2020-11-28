from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_current_user, get_db
from app.db.models.user import UsersDBModel
from app.schemas.allergies import AllergyCreateModel

router = APIRouter()


@router.post("/create")
async def create_allergia(
    request_data: AllergyCreateModel,
    current_user: UsersDBModel = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    request_data = request_data.dict()
    request_data["user_id"] = current_user.id
    allergy = await crud.allergy.create(db, obj_in=request_data)
    return {"result": {"id": allergy.id}}
