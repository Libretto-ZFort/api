from fastapi import HTTPException, Request, status
from gotrue import User, UserResponse
from gotrue.errors import AuthApiError
from supabase._async.client import AsyncClient


async def verify_token(supabase_client: AsyncClient, request: Request) -> User:
    """Token verification includes the Supabase in-place integration."""

    if not (token := request.headers.get("Authorization")):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Supabase token is not valid",
        )
    try:
        jwt = token.split(" ")[1]

        user_response: UserResponse | None = await supabase_client.auth.get_user(jwt)

        if not user_response:
            raise HTTPException(
                status_code=status.HTTP_424_FAILED_DEPENDENCY,
                detail="Supabase can not validate token",
            )
    except (AuthApiError, IndexError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Supabase token is not valid",
        )

    return user_response.user
