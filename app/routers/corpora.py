from fastapi import APIRouter, Depends, Request

from sqlalchemy.orm import Session

from exceptions import AlreadyExistsException, DoesNotExistException
from crud import BaseCRUD
from models import Corpus
from schemas import Corpora, CorpusCreate, CorpusBase


router = APIRouter(prefix="/corpora", tags=["corpora"])


# Dependency

def get_db(request: Request):
    return request.state.db


@router.get(
    "",
    description="List of all corpora",
    response_model=Corpora,
    summary="All corpora",
)
async def all_corpora(db: Session = Depends(get_db)):
    corpora_crud = BaseCRUD(db, Corpus)
    return {"data": corpora_crud.get_items()}


@router.post(
    "",
    description="Send title of new corpus",
    response_model=CorpusCreate,
    responses={
        200: {
            "description": "Corpus has been added"
        },
        400: {
            "description": "Corpus with this title already exists",
            "content": {
                "application/json": {
                    "example": {"error": "Brown Corpus already exists"}
                }
            },
        },
    },
    summary="Add corpus",
)
async def add_corpus(corpus: CorpusCreate, db: Session = Depends(get_db)):
    corpora_crud = BaseCRUD(db, Corpus)
    new_corpus = corpora_crud.get_item_by_title(corpus.title)
    if new_corpus:
        raise AlreadyExistsException(title=corpus.title)
    return corpora_crud.create_item(corpus)


@router.put(
    "/{corpus_id}",
    description="Change corpus title",
    response_model=CorpusBase,
    responses={
        200: {
            "description": "Corpus with title has been changed"
        },
        400: {
            "description": "Corpus with this title already exists",
            "content": {
                "application/json": {
                    "example": {"error": "Brown Corpus already exists"}
                }
            },
        },
        404: {
            "description": "Requested corpus does not exist",
            "content": {
                "application/json": {
                    "example": {"error": "Requested object does not exist"}
                }
            },
        },
    },
    summary="Edit corpus",
)
async def edit_corpus(
    corpus_id: int,
    corpus: CorpusBase,
    db: Session = Depends(get_db)
):
    corpora_crud = BaseCRUD(db, Corpus)
    get_corpus = corpora_crud.get_item_by_id(corpus_id)

    # Check if it's the same corpus
    same_corpus = corpora_crud.get_item_by_id_and_title(
        corpus_id, corpus.title
    )
    if same_corpus:
        return corpora_crud.update_item_title(same_corpus, corpus.title)

    # Check if corpus with this title exists
    corpus_title_exists = corpora_crud.get_item_by_title(corpus.title)
    if corpus_title_exists:
        raise AlreadyExistsException(title=corpus.title)

    # Check for non-existent id
    if not get_corpus:
        raise DoesNotExistException(id=corpus_id)
    return corpora_crud.update_item_title(get_corpus, corpus.title)
