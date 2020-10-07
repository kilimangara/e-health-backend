from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_current_user, get_db
from app.db.models.user import Users
from app.schemas.allergies import AllergiaBase, AllergiaCreate

router = APIRouter()


@router.post("/create")
async def create_allergia(
        request_data: AllergiaCreate,
        current_user: Users = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    request_data = request_data.dict()
    request_data['user_id'] = current_user.id
    allergia = await crud.allergia.create(db, obj_in=request_data)
    return {"result": {"id": allergia.id}}


@router.post("/getByUser")
async def getByUser(current_user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    allergies = await crud.allergia.get_by_user_id(db, user_id=current_user.id)
    return {"result": [allergia_to_dict(el) for el in allergies]}

async def allergia_to_dict(allergia: AllergiaBase):
    return {
        'id': allergia.id,
        'user_id': allergia.user_id,
        'reaction': allergia.reaction,
        'allergen': allergia.allergen,
    }
