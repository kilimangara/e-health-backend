from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.models.user import UsersDBModel
from app.schemas.user import UserCreateModel, UserUpdateModel


class CRUDUser(CRUDBase[UsersDBModel, UserCreateModel, UserUpdateModel]):
    async def get_by_phone(self, db: Session, phone: str) -> Optional[UsersDBModel]:
        return db.query(UsersDBModel).filter(UsersDBModel.phone == phone).first()

    async def registrate(self, db: Session, obj_in: UserCreateModel) -> UsersDBModel:
        """Создание пользователя по номеру телефона."""
        db_obj = UsersDBModel(phone=obj_in.phone, status="created")
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    async def update(
        self,
        db: Session,
        *,
        db_obj: UsersDBModel,
        obj_in: Union[UserUpdateModel, Dict[str, Any]]
    ):
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return await super().update(db, db_obj=db_obj, obj_in=update_data)


user = CRUDUser(UsersDBModel)
