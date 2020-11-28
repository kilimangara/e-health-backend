from typing import List

from pydantic import BaseModel


class CreateUrlsModel(BaseModel):
    images: List["ImageDataCreateModel"]


class ImageDataCreateModel(BaseModel):
    content_type: str
    byte_size: int
    check_sum: str
    position: int


CreateUrlsModel.update_forward_refs()


class ImageDataUpdateModel(BaseModel):
    analysis_id: int
