from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_current_user, get_db
from app.db.models.user import UsersDBModel, STATUS_APPROVED
from app.schemas.user import UserUpdateModel


router = APIRouter()


@router.post("/update")
async def update(
    request_data: UserUpdateModel,
    current_user: UsersDBModel = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Обноления пользователя"""
    if current_user.name is None and request_data.name is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Name is required"
        )

    request_data = request_data.dict(exclude_unset=True)
    if current_user.status != STATUS_APPROVED:
        request_data.update({"status": STATUS_APPROVED})

    await crud.user.update(db, db_obj=current_user, obj_in=request_data)
    return {"result": {"user_id": current_user.id}}
