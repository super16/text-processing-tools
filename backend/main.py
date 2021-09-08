from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from exceptions import AlreadyExistsException, DoesNotExistException
from routers import corpora
from models import Base
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

# Basic API settings

api = FastAPI()

origins = [
    "http://localhost:8080",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

# v1 API settings

tags_metadata = [
    {
        "name": "corpora",
        "description": "Corpora endpoints",
    }
]

v1 = FastAPI(
    title="Text Processing Tools API",
    description="Backend API",
    version="0.0.1",
    openapi_tags=tags_metadata
)

api.mount("/api/v1", v1)

@v1.get("/")
async def root():
    return {"message": "Hello World"}

# Routers

v1.include_router(corpora.router)

# Exceptions

@v1.exception_handler(AlreadyExistsException)
async def already_exists_exception_handler(
    request: Request,
    exc: AlreadyExistsException):
    return JSONResponse(
        status_code=400,
        content={"error": f"{exc.title} already exists"},
    )

@v1.exception_handler(DoesNotExistException)
async def does_not_exists_exception_handler(
    request: Request, 
    exc: DoesNotExistException):
    return JSONResponse(
        status_code=404,
        content={"error": "Requested object does not exist"},
    )
