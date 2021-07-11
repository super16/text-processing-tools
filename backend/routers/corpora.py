from fastapi import APIRouter, Depends, Request

from sqlalchemy.orm import Session

from crud import get_corpora
from schemas import Corpora

router = APIRouter(
    prefix="/corpora",
    tags=["corpora"]
)


# Dependency

def get_db(request: Request):
    return request.state.db


@router.get(
    "/",
    summary="All corpora",
    response_model=Corpora,
    description="List of all corpora"
)
async def all_corpora(db: Session = Depends(get_db)):
    corpora_list = get_corpora(db)
    return {"data": corpora_list}
