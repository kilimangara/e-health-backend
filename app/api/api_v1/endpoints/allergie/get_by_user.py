from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_current_user, get_db
from app.db.models.user import UsersDBModel

router = APIRouter()


@router.post("/getByUser")
async def getByUser(
    current_user: UsersDBModel = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    allergies = await crud.allergy.get_by_user_id(db, user_id=current_user.id)
    return {"result": [el.to_dict() for el in allergies]}
