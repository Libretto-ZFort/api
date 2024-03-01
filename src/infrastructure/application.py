from collections.abc import Iterable

from fastapi import APIRouter, FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict

from src.config import settings


class InternalEntity(BaseModel):
    model_config = ConfigDict(
        use_enum_values=True,
        validate_assignment=True,
        arbitrary_types_allowed=True,
        from_attributes=True,
    )


async def base_error_handler(_: Request, exception: Exception) -> JSONResponse:
    """This function handles all errors that are inherited from Exception."""

    # logging
    print(f"ERROR: {exception}")

    return JSONResponse(
        {"message": "Unhandled error"},
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


def factory(*_, rest_routers: Iterable[APIRouter]) -> FastAPI:
    """The application factory using FastAPI framework."""

    # Initialize the base FastAPI application
    app = FastAPI(
        title=settings.api_title,
        exception_handlers={
            Exception: base_error_handler,
        },
    )

    # Include REST API routers
    for router in rest_routers:
        app.include_router(router)

    # NOTE: Basically CORS settings must be included to the
    #   environment configurations but for the simplicity they are just
    #   hardcoded in the factory
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
