from logging import getLogger, Logger
from subprocess import Popen, PIPE

from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uvicorn import run

from exceptions import AlreadyExistsException, DoesNotExistException
from routers import corpora
from models import Base
from database import SessionLocal, engine


# Constants

RELOAD_EXCLUDES: list[str] = [
    "app/__pycache__",
    "app/routers/__pycache__",
    "app/templates",
    ".git",
    "env"
]


# Database binding

Base.metadata.create_all(bind=engine)

# Application

app: FastAPI = FastAPI(
    title="text-processing-tools",
    description="Application for NLP in web interface",
    version="0.1.0",
    openapi_tags=[
        {
            "name": "Application",
            "description": "Web interface pages",
        },
    ]
)

templates: Jinja2Templates = Jinja2Templates(directory="app/templates")

app.mount(
    "/static",
    StaticFiles(directory="app/templates/static"),
    name="static",
)


@app.on_event("startup")
async def startup_event():
    logger: Logger = getLogger("uvicorn.error")

    with Popen(
        ["npm", "run", "--prefix", "app/frontend", "build"],
        stdout=PIPE,
        universal_newlines=True,
    ) as proc:
        logger.info(proc.stdout.read())


@app.get("/", response_class=HTMLResponse, tags=["Application"])
async def index_page(request: Request):
    return templates.TemplateResponse(
        "index.html", {'request': request},
    )


# API

api: FastAPI = FastAPI(
    title="text-processing-tools API",
    description="JSON REST API Endpoints",
    version="0.1.0",
    openapi_tags=[
        {
            "name": "corpora",
            "description": "Corpora endpoints",
        },
    ],
)


# Middleware

@api.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency

def get_db(request: Request):
    return request.state.db


app.mount("/api", api)
api.include_router(corpora.router)


# Exceptions

@api.exception_handler(AlreadyExistsException)
async def already_exists_exception_handler(
    request: Request,
    exc: AlreadyExistsException
):
    return JSONResponse(
        status_code=400,
        content={"error": f"{exc.title} already exists"},
    )


@api.exception_handler(DoesNotExistException)
async def does_not_exists_exception_handler(
    request: Request,
    exc: DoesNotExistException
):
    return JSONResponse(
        status_code=404,
        content={"error": "Requested object does not exist"},
    )


if __name__ == "__main__":
    run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_excludes=RELOAD_EXCLUDES,
        reload_includes="*",
    )
