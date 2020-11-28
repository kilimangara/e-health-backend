from typing import Optional

from pydantic import BaseModel


class AllergyCreateModel(BaseModel):
    allergen: Optional[str] = None
    reaction: Optional[str] = None


class AllergyUpdateModel(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int] = None
    allergen: Optional[str] = None
    reaction: Optional[str] = None
