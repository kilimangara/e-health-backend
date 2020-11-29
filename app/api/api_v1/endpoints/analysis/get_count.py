from fastapi import APIRouter, Depends
from fastapi.logger import logger
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.crud import analysis
from app.db.models.user import UsersDBModel

router = APIRouter()


@router.post("/getCount")
async def get(
    current_user: UsersDBModel = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    result = await analysis.get_count_by_category(db, current_user.id)
    logger.info(result)
    return {"result": result}
