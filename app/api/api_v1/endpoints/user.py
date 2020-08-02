from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_current_user, get_db
from app.db.models.user import UserData
from app.schemas.user import UserUpdate

router = APIRouter()


@router.post("/update")
def update_user(
        request_data: UserUpdate,
        current_user: UserData = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    if current_user.name is None and request_data.name is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Name is required'
        )
    crud.user.update(db, db_obj=current_user, obj_in=request_data)
    return {"result": {"user_id": current_user.id,}}


@router.post("/get")
def get(current_user: UserData = Depends(get_current_user)):
    return {"result": current_user_to_dict(current_user)}


def current_user_to_dict(user: UserData) -> dict:
    return {
        'name': user.name,
        'phone': user.phone,
        'blood_type': user.blood_type,
        'birth_date': user.birth_date,
        'last_name': user.last_name,
        'weight': user.weight,
        'height': user.height,
    }
