from fastapi.responses import ORJSONResponse


class AlreadyExistsException(Exception):

    def __init__(self, title: str):
        self.title = title


class DoesNotExistException(Exception):
    pass


async def already_exists_handler(
    _,
    exc: AlreadyExistsException,
) -> ORJSONResponse:
    """Exception when unique value is violated."""
    return ORJSONResponse(
        status_code=400,
        content={"error": f"{exc.title} already exists"},
    )


async def does_not_exist_handler(
    _,
    exc: DoesNotExistException,
) -> ORJSONResponse:
    """Exception for non-existent values."""
    return ORJSONResponse(
        status_code=404,
        content={"error": "Requested object does not exist"},
    )
