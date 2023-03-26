from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from text_processing_tools.api.exceptions import (
    AlreadyExistsException,
    DoesNotExistException,
    already_exists_handler,
    does_not_exist_handler,
)
from text_processing_tools.api.main import api
from text_processing_tools.tags import tags_metadata


app: FastAPI = FastAPI(
    title="text-processing-tools",
    description="Application for NLP in web interface",
    version="0.1.0",
    openapi_tags=tags_metadata,
)

# ==========
# Exceptions
# ==========

app.add_exception_handler(AlreadyExistsException, already_exists_handler)
app.add_exception_handler(DoesNotExistException, does_not_exist_handler)


# ==========
# API Router
# ==========

app.include_router(api)


# =======================
# Static files (frontend)
# =======================

app.mount(
    "/",
    StaticFiles(
        directory="text_processing_tools/frontend/dist",
        html=True,
    ),
    name="static2"
)

app.mount(
    "/_nuxt",
    StaticFiles(
        directory="text_processing_tools/frontend/dist/_nuxt",
    ),
    name="static",
)


# =========
# Templates
# =========

@app.get("/", response_class=FileResponse, tags=["Application"])
async def index_page() -> FileResponse:
    return FileResponse("index.html")
