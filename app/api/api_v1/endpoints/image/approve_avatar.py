from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_current_user_is_approved, get_db
from app.db.models.user import UsersDBModel
from app.schemas.image import ApproveAvatarModel

router = APIRouter()


@router.post("/approveAvatar")
async def process_list(
    request_data: ApproveAvatarModel,
    current_user: UsersDBModel = Depends(get_current_user_is_approved),
    db: Session = Depends(get_db),
):
    image = await crud.images.get(db, request_data.image_id)
    if not image or not image.user_id == current_user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Bad image id")
    await crud.images.approve_new_avatar(db, current_user.id, request_data.image_id)

    return {"result": "ok"}
