from fastapi import APIRouter

from text_processing_tools.api.routers import corpora_router


api: APIRouter = APIRouter(prefix="/api")


api.include_router(corpora_router)
