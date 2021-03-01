from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models.allergies import AllergyDBModel
from app.schemas.allergies import AllergyCreateModel, AllergyUpdateModel


class CRUDAllergia(CRUDBase[AllergyDBModel, AllergyCreateModel, AllergyUpdateModel]):
    async def get_by_user_id(
        self, db: Session, *, user_id: int
    ) -> Optional[List[AllergyDBModel]]:
        return db.query(AllergyDBModel).filter(AllergyDBModel.user_id == user_id)


allergy = CRUDAllergia(AllergyDBModel)
