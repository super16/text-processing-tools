# text-processing-tools

Application with NLP tools in the web interface.

## Development

Requires [poetry](https://python-poetry.org/).

### Install dependencies

```shell
poetry install
```

## Lint

```shell
poetry run flake8
poetry run mypy text_processing_tools/
```

### Run

```shell
poetry run uvicorn text_processing_tools:app
```
