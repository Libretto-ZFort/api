"""
The API entrypoint file.
"""

from fastapi import FastAPI

from src.api.tickets import router as tickets_router
from src.infrastructure.application import factory as application_factory

app: FastAPI = application_factory(
    rest_routers=(tickets_router,),
)
