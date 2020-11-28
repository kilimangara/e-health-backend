from fastapi import APIRouter, Depends

from app.api.deps import get_current_user
from app.db.models.user import UsersDBModel

router = APIRouter()


@router.post("/get")
async def get(current_user: UsersDBModel = Depends(get_current_user)):
    return {"result": current_user.to_dict()}
