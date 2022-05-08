from fastapi import APIRouter, Depends, Request

from sqlalchemy.orm import Session

from exceptions import AlreadyExistsException, DoesNotExistException
from crud import (
    create_corpus,
    get_corpora,
    get_corpus_by_id,
    get_corpus_by_title,
    get_corpus_by_title_and_id,
    update_corpus
)   
from schemas import Corpora, CorpusCreate, CorpusBase

router = APIRouter(
    prefix="/corpora",
    tags=["corpora"]
)


# Dependency

def get_db(request: Request):
    return request.state.db


@router.get("", summary="All corpora",
    response_model=Corpora,
    description="List of all corpora"
)
async def all_corpora(db: Session = Depends(get_db)):
    corpora_list = get_corpora(db)
    return {"corpora": corpora_list}


@router.post("", summary="Add corpus",
    response_model=CorpusCreate,
    description="Send title of new corpus",
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
)
async def add_corpus(corpus: CorpusCreate, db: Session = Depends(get_db)):
    new_corpus = get_corpus_by_title(db, corpus.title)
    if new_corpus:
        raise AlreadyExistsException(title=corpus.title)
    return create_corpus(db=db, corpus=corpus)

@router.put("/{corpusId}", summary="Edit corpus",
    response_model=CorpusBase,
    description="Change corpus title",
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
)
async def edit_corpus(
    corpusId: int, corpus: CorpusBase, db: Session = Depends(get_db)
    ):
    corpus_id = corpusId
    get_corpus = get_corpus_by_id(db, corpus_id)

    # Check if it's the same corpus
    same_corpus = get_corpus_by_title_and_id(db, corpus.title, corpus_id)
    if same_corpus:
        return update_corpus(db=db, corpus=same_corpus, new_title=corpus.title)

    # Check if corpus with this title exists
    corpus_title_exists = get_corpus_by_title(db, corpus.title)
    if corpus_title_exists:
        raise AlreadyExistsException(title=corpus.title)    

    # Check for non-existent id
    if not get_corpus:
        raise DoesNotExistException(id=corpus_id)
    return update_corpus(db=db, corpus=get_corpus, new_title=corpus.title)

        
    
        

