from typing import List
from uuid import uuid4

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_current_user, get_db
from app.db.models.image import ImageBlobDBModel
from app.db.models.user import UsersDBModel
from app.schemas.image import CreateUrlsModel
from app.utils.aws import generate_upload_urls

router = APIRouter()


@router.post("/createList")
async def process_list(
    request_data: CreateUrlsModel,
    current_user: UsersDBModel = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    data_to_insert = process_request(current_user.id, request_data)
    images = await crud.images.add_list(db, data_to_insert)
    result = generate_upload_urls(images)

    return {"result": result}


def process_request(user_id: int, req: CreateUrlsModel) -> List[ImageBlobDBModel]:
    result = []
    for el in req.images:
        result.append(
            ImageBlobDBModel(
                filename=f"{user_id}/{str(uuid4())}",
                check_sum=el.check_sum,
                content_type=el.content_type,
                byte_size=el.byte_size,
                position=el.position,
            )
        )

    return result
