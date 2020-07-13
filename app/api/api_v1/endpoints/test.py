from typing import Any

from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/")
def test() -> Any:
    """
    Test route
    """
    return { 'health': 'ok' }
