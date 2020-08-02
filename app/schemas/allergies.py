from typing import Optional

from pydantic import BaseModel


# Shared properties
class AllergiaBase(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int] = None
    allergen: Optional[str] = None
    reaction: Optional[str] = None


class AllergiaCreate(BaseModel):
    allergen: Optional[str] = None
    reaction: Optional[str] = None