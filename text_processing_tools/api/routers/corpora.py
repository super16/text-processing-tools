from typing import Optional, TYPE_CHECKING

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse, Response
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

if TYPE_CHECKING:
    from sqlalchemy.engine import Result

from text_processing_tools.models import Corpus
from text_processing_tools.api.schemas import (
    Corpora,
    CorpusBase,
    CorpusItem,
)
from text_processing_tools.api.exceptions import (
    AlreadyExistsException,
    DoesNotExistException,
)
from text_processing_tools.database.connections import database_conn


corpora_router = APIRouter(prefix="/corpora", tags=["Corpora"])


@corpora_router.get(
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
async def all_corpora(
    session: AsyncSession = Depends(database_conn.create_session),
) -> ORJSONResponse:
    async with session.begin():
        result: Result = await session.execute(select(Corpus))
        corpora_items = [item for item in result.scalars()]
    return ORJSONResponse(content=corpora_items)


@corpora_router.post(
    "",
    summary="Add new corpus",
    response_model=CorpusItem,
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
async def add_corpus(
    new_corpus: CorpusBase,
    session: AsyncSession = Depends(database_conn.create_session),
) -> ORJSONResponse:
    async with session.begin():
        try:
            result: Result = await session.execute(
                insert(Corpus).values(
                    title=new_corpus.title
                ).returning(Corpus),
            )
            created_corpus: Optional[Corpus] = result.scalar()
        except IntegrityError:
            raise AlreadyExistsException(new_corpus.title)

    return ORJSONResponse(content=created_corpus)


@corpora_router.get(
    "/{corpus_id}",
    summary="Get corpus",
    description="Get corpus by its id value",
    response_model=CorpusItem,
    responses={
        200: {
            "description": "Corpus with title has been changed"
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
async def get_corpus(
    corpus_id: int,
    session: AsyncSession = Depends(database_conn.create_session),
):
    async with session.begin():
        result: Result = await session.execute(
            select(Corpus).where(Corpus.id == corpus_id)
        )
        corpus: Optional[Corpus] = result.scalar()

        if not corpus:
            raise DoesNotExistException()

    return ORJSONResponse(content=corpus)


@corpora_router.patch(
    "/{corpus_id}",
    summary="Edit corpus",
    description="Update corpus' title",
    response_model=CorpusItem,
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
    corpus_id: int,
    corpus: CorpusBase,
    session: AsyncSession = Depends(database_conn.create_session),
):
    async with session.begin():
        try:
            result: Result = await session.execute(
                update(Corpus).where(
                    Corpus.id == corpus_id
                ).values(title=corpus.title).returning(Corpus)
            )
            updated_corpus: Optional[Corpus] = result.scalar()
        except IntegrityError:
            raise AlreadyExistsException(corpus.title)

        if not updated_corpus:
            raise DoesNotExistException()

    return ORJSONResponse(content=updated_corpus)


@corpora_router.delete(
    "/{corpus_id}",
    summary="Delete corpus",
    description="Delete corpus by its id",
    responses={
        204: {
            "description": "Corpus with title has been changed"
        },
    },
)
async def delete_corpus(
    corpus_id: int,
    session: AsyncSession = Depends(database_conn.create_session),
):
    async with session.begin():
        await session.execute(
            delete(Corpus).where(Corpus.id == corpus_id)
        )
    return Response(status_code=204)
