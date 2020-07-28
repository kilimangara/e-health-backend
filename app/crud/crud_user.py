from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models import UserData
from app.schemas.user import UserRegistrationIn, UserUpdate


class CRUDUser(CRUDBase[UserData, UserRegistrationIn, UserUpdate]):
    def get_by_phone(self, db: Session, phone: str) -> Optional[UserData]:
        return db.query(UserData).filter(UserData.phone == phone).first()

    def registrate(self, db: Session, obj_in: UserRegistrationIn) -> UserData:
        """Создание пользователя по номеру телефона."""
        db_obj = UserData(phone=obj_in.phone, status="created")
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: UserData,
        obj_in: Union[UserUpdate, Dict[str, Any]]
    ):
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


user = CRUDUser(UserData)
