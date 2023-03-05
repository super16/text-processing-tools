from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

from text_processing_tools.api.main import api


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

app.include_router(api)

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


@app.get("/", response_class=HTMLResponse)
async def index_page():
    return FileResponse("index.html")
