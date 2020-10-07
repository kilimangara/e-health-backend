from typing import Optional, List, Any

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models import Allergies
from app.schemas.allergies import AllergiaBase, AllergiaCreate


class CRUDAllergia(CRUDBase[AllergiaBase, AllergiaCreate, AllergiaBase]):
    async def get_by_user_id(self, db: Session, *, user_id: int) -> Optional[List[AllergiaBase]]:
        return db.query(Allergies).filter(Allergies.user_id == user_id)


allergia = CRUDAllergia(Allergies)
