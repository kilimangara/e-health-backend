from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
from sqlalchemy import text

from app.crud.base import CRUDBase
from app.db.models.user import UsersDBModel
from app.schemas.user import UserCreateModel, UserUpdateModel


class CRUDUser(CRUDBase[UsersDBModel, UserCreateModel, UserUpdateModel]):
    async def get_by_phone(self, db: Session, phone: str) -> Optional[UsersDBModel]:
        return db.query(UsersDBModel).filter(UsersDBModel.phone == phone).first()

    async def get_user_by_id_with_avatar(self, db: Session, user_id: int):
        result = db.execute(
            text("""
                SELECT u.*,
                       im.filename,
                       im.content_type
                FROM users AS u
                LEFT JOIN image_blob AS im ON u.id = im.user_id
                AND im.is_avatar = TRUE
                WHERE u.id=:user_id;
            """),
            {"user_id": user_id}
        ).fetchone()

        return {key: val for key, val in result.items()}

    async def get_users_by_parent_id_with_avatar(self, db: Session, user_id: int):
        result = db.execute(
            text("""
                SELECT u.*,
                       im.filename,
                       im.content_type
                FROM users AS u
                LEFT JOIN image_blob AS im ON u.id = im.user_id
                AND im.is_avatar = TRUE
                WHERE u.id=:user_id or u.parent_user_id=:user_id;
            """),
            {"user_id": user_id}
        ).fetchall()

        return [{key: val for key, val in el.items()} for el in result]

    async def registrate(self, db: Session, obj_in: UserCreateModel) -> UsersDBModel:
        """Создание пользователя по номеру телефона."""
        db_obj = UsersDBModel(phone=obj_in.phone, status="created")
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    async def create_sub_user(self, db: Session, parent_user_id: int) -> int:
        result = db.execute(
            text("""
                INSERT INTO users (parent_user_id) VALUES (:parent_user_id) RETURNING id;
            """),
            {"parent_user_id": parent_user_id}
        )
        db.commit()

        return result.fetchone()[0]

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
