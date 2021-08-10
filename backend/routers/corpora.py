from fastapi import APIRouter, Depends, Request

from sqlalchemy.orm import Session

from crud import get_corpora, create_corpus
from schemas import Corpora, CorpusCreate

router = APIRouter(
    prefix="/corpora",
    tags=["corpora"]
)


# Dependency

def get_db(request: Request):
    return request.state.db


@router.get(
    "",
    summary="All corpora",
    response_model=Corpora,
    description="List of all corpora"
)
async def all_corpora(db: Session = Depends(get_db)):
    corpora_list = get_corpora(db)
    return {"corpora": corpora_list}


@router.post(
    "",
    summary="Add corpus",
    response_model=CorpusCreate,
    description="Send title of new corpus"
)
async def add_corpus(corpus: CorpusCreate, db: Session = Depends(get_db)):
    return create_corpus(db=db, corpus=corpus)
