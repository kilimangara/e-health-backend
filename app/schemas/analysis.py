from typing import List, Optional

from fastapi import HTTPException, status
from pydantic import BaseModel, validator


class AnalysisCreateRequestModel(BaseModel):
    category_id: int
    comment: Optional[str]
    images_to_link: List[int]

    def to_db_create_model(self, user_id):
        return AnalysisCreateModel(
            category_id=self.category_id,
            comment=self.comment,
            user_id=user_id,
        )


class AnalysisCreateModel(BaseModel):
    category_id: int
    comment: Optional[str]
    user_id: int


class AnalysisGetModel(BaseModel):
    category_id: int
    page: int = 1
    limit: int = 20

    # @validator('category_id', 'page', 'limit')
    # def validate_fields(self, value):
    #     if value < 1:
    #         raise HTTPException(
    #             status_code=status.HTTP_400_BAD_REQUEST, detail="phone_not_valid"
    #         )
    #     return value
