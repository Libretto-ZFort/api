from fastapi import HTTPException, status
from postgrest.exceptions import APIError
from supabase._async.client import AsyncClient, create_client

from src.config import settings


async def client_factory() -> AsyncClient:
    """A Supabase async client factory."""

    supabase_client: AsyncClient = await create_client(
        settings.supabase.url, settings.supabase.api_key
    )
    return supabase_client


from functools import wraps


def response_validator(coro):
    @wraps(coro)
    async def wrapper(*args, **kwargs):
        try:
            return await coro(*args, **kwargs)
        except IndexError:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found"
            )
        except APIError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid request data",
            )

    return wrapper
