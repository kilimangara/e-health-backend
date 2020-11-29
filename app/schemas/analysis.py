from typing import List, Optional

from pydantic import BaseModel


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
