from pydantic import BaseModel

from typing import List


class CreateUrls(BaseModel):
    images: List['ImageData']

class ImageData(BaseModel):
    content_type: str
    byte_size: int
    check_sum: str
    position: int


CreateUrls.update_forward_refs()
