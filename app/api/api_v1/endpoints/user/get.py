from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.crud import user
from app.db.models.user import UsersDBModel
from app.utils.aws import generate_download_url

router = APIRouter()


@router.post("/get")
async def get(
    current_user: UsersDBModel = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    current_user = await user.get_user_by_id_with_avatar(db, current_user.id)
    avatar_filename = current_user.pop('filename')
    avatar_content_type = current_user.pop('content_type')
    current_user.update(
        {"avatar_url": generate_download_url(avatar_filename, avatar_content_type)}
    )
    return {"result": current_user}
