from fastapi import APIRouter, Depends, HTTPException, Request, status
from gotrue import User
from pydantic import PositiveInt
from supabase._async.client import AsyncClient

from src import operational as op
from src.domain.tickets import Ticket, TicketUncommited
from src.infrastructure.security import verify_token
from src.infrastructure.supabase import client_factory as supabase_client_factory

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.post("", status_code=status.HTTP_201_CREATED)
async def tickets_create(
    request: Request,
    schema: TicketUncommited,
    supabase_client: AsyncClient = Depends(supabase_client_factory),
) -> Ticket:
    """Create a new Ticket."""

    user: User = await verify_token(supabase_client, request)
    ticket: Ticket = await op.ticket_create(supabase_client, schema, user)

    return ticket


@router.get("", status_code=status.HTTP_200_OK)
async def tickets_list(
    request: Request,
    supabase_client: AsyncClient = Depends(supabase_client_factory),
) -> list[Ticket]:
    user: User = await verify_token(supabase_client, request)
    tickets: list[Ticket] = await op.tickets_list(supabase_client, user)

    return tickets


@router.get("/{ticket_id}", status_code=status.HTTP_200_OK)
async def ticket_retrieve(
    request: Request,
    ticket_id: PositiveInt,
    supabase_client: AsyncClient = Depends(supabase_client_factory),
) -> Ticket:
    user: User = await verify_token(supabase_client, request)
    ticket: Ticket = await op.ticket_retrieve(supabase_client, user, ticket_id)

    return ticket


@router.put("/{ticket_id}", status_code=status.HTTP_200_OK)
async def ticket_update(
    request: Request,
    ticket_id: PositiveInt,
    schema: TicketUncommited,
    supabase_client: AsyncClient = Depends(supabase_client_factory),
) -> Ticket:
    user: User = await verify_token(supabase_client, request)
    ticket: Ticket = await op.ticket_update(supabase_client, user, ticket_id, schema)

    return ticket


@router.delete("/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
async def ticket_delete(
    request: Request,
    ticket_id: PositiveInt,
    supabase_client: AsyncClient = Depends(supabase_client_factory),
):
    user: User = await verify_token(supabase_client, request)
    if not (_deleted := (await op.ticket_delete(supabase_client, user, ticket_id))):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found"
        )
