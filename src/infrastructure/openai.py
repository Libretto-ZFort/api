"""
This module represents the integration with the OpenAI service.
"""
from functools import wraps

from fastapi import HTTPException, status
from openai import AsyncOpenAI

from src.config import settings

client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key=settings.open_ai.api_key
)


def poor_openai_error_handler(coro):
    @wraps(coro)
    async def inner(*args, **kwargs) -> str:
        try:
            return await coro(*args, **kwargs)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_424_FAILED_DEPENDENCY,
                detail="OpenAI response error",
            )

    return inner


@poor_openai_error_handler
async def description_optimization(source: str) -> str:
    """Optimized the description based on the incomming description."""

    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Please optimize the next ticket description: '{source}'",
            }
        ],
        model="gpt-3.5-turbo",
    )

    if content := chat_completion.choices[0].message.content:
        return content
    else:
        raise NotImplementedError


@poor_openai_error_handler
async def description_generation(title: str) -> str:
    """Generate the description based on the specified title."""

    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Please generate the ticket description based on the title: '{title}'",
            }
        ],
        model="gpt-3.5-turbo",
    )

    if content := chat_completion.choices[0].message.content:
        return content
    else:
        raise NotImplementedError
