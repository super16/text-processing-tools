from fastapi import APIRouter, Depends, Request

from sqlalchemy.orm import Session

from exceptions import AlreadyExistsException, DoesNotExistException
from crud import BaseCRUDL
from models import Corpus
from schemas.corpora import Corpora, CorpusCreate, CorpusBase, CorpusItem


router = APIRouter(prefix="/corpora", tags=["corpora"])


# Dependency

def get_db(request: Request):
    return request.state.db


@router.get(
    "",
    description="List of all corpora",
    response_model=Corpora,
    summary="All corpora",
    responses={
        200: {
            "description": "List of all corpora"
        },
    },
)
async def all_corpora(db: Session = Depends(get_db)):
    corpora_crudl: BaseCRUDL = BaseCRUDL(db, Corpus)
    return {"data": corpora_crudl.read_items()}


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
    corpora_crudl: BaseCRUDL = BaseCRUDL(db, Corpus)
    new_corpus = corpora_crudl.read_item_by_attr('title', corpus.title)
    if new_corpus:
        raise AlreadyExistsException(title=corpus.title)
    return corpora_crudl.create_item(corpus)


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
    corpora_crudl: BaseCRUDL = BaseCRUDL(db, Corpus)
    get_corpus = corpora_crudl.read_item_by_attr('id', corpus_id)

    # Check if it's the same corpus
    same_corpus = corpora_crudl.get_item_by_id_and_title(
        corpus_id, corpus.title
    )
    if same_corpus:
        return corpora_crudl.update_item_by_attr(
            same_corpus, 'title', corpus.title
        )

    # Check if corpus with this title exists
    corpus_title_exists = corpora_crudl.read_item_by_attr(
        'title', corpus.title
    )
    if corpus_title_exists:
        raise AlreadyExistsException(title=corpus.title)

    # Check for non-existent id
    if not get_corpus:
        raise DoesNotExistException(id=corpus_id)
    return corpora_crudl.update_item_by_attr(
        get_corpus, 'title', corpus.title
    )


@router.delete(
    "/{corpus_id}",
    description="Delete corpus",
    response_model=CorpusItem,
    responses={
        200: {
            "description": "Corpus has been deleted"
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
    summary="Delete corpus",
)
async def delete_corpus(
    corpus_id: int,
    db: Session = Depends(get_db)
):
    corpora_crudl: BaseCRUDL = BaseCRUDL(db, Corpus)
    delete_corpus = corpora_crudl.delete_item(corpus_id)

    # Check for non-existent id
    if not delete_corpus:
        raise DoesNotExistException(id=corpus_id)
    return delete_corpus
