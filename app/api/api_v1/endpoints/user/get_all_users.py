from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.crud import user
from app.db.models.user import UsersDBModel
from app.utils.aws import generate_download_url

router = APIRouter()


@router.post("/getAllUsers")
async def get(
    current_user: UsersDBModel = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user_id = current_user.id if current_user.parent_user_id is None else current_user.parent_user_id

    users = await user.get_users_by_parent_id_with_avatar(db, user_id)
    for u in users:
        avatar_filename = u.pop('filename')
        avatar_content_type = u.pop('content_type')
        if avatar_content_type is None or avatar_filename is None:
            avatar_url = None
        else:
            avatar_url = generate_download_url(avatar_filename, avatar_content_type)
        u.update(
            {"avatar_url": avatar_url}
        )
    return {"result": users}
