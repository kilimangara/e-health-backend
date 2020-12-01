from typing import Dict, List

from fastapi import APIRouter, Depends, logger
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.crud import analysis
from app.db.models.user import UsersDBModel
from app.schemas.analysis import AnalysisGetModel
from app.utils.aws import generate_download_url

router = APIRouter()


@router.post("/get")
async def get(
    request_data: AnalysisGetModel,
    current_user: UsersDBModel = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    analysis_data = await analysis.get_by_user_with_images(
        db, current_user.id, request_data
    )
    return {"result": list(process_data(analysis_data).values())}


def process_data(analysis_data: List[Dict]) -> Dict:
    data = {}
    for el in analysis_data:
        el = {key: val for key, val in el.items()}
        if el["analysis_id"] not in data:
            data[el["analysis_id"]] = {
                "comment": el["comment"],
                "created_at": el["created_at"],
                "images": [],
            }

        data[el["analysis_id"]]["images"].append(
            {
                "position": el["position"],
                "url": generate_download_url(el["filename"], el["content_type"]),
            }
        )

    return data
