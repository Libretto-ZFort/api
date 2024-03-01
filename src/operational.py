"""
The operational (aka application) layer is basically
the highest level of the operation abstraction.

If the logic becomes quick huge or includes multiple integrations
this is the right place to outline the flow :)
"""


from gotrue import User
from supabase._async.client import AsyncClient

from src.domain.tickets import Ticket, TicketUncommited
from src.infrastructure.openai import description_generation, description_optimization
from src.infrastructure.supabase import (
    response_validator as supabase_response_validator,
)


@supabase_response_validator
async def ticket_create(
    supabase_client: AsyncClient, schema: TicketUncommited, user: User
) -> Ticket:
    # Generate or optimize the description
    schema.description = (
        await description_generation(schema.title)
        if schema.description is None
        else (await description_optimization(schema.description))
    )

    # Save the ticket to the database
    response = (
        await supabase_client.table("tickets")
        .insert({**schema.model_dump(), "user_id": user.id})
        .execute()
    )

    return Ticket(**response.data[0])


@supabase_response_validator
async def tickets_list(supabase_client: AsyncClient, user: User) -> list[Ticket]:
    response = (
        await supabase_client.table("tickets")
        .select("*")
        .eq("user_id", user.id)
        .execute()
    )

    return [Ticket(**item) for item in response.data]


@supabase_response_validator
async def ticket_retrieve(
    supabase_client: AsyncClient, user: User, ticket_id: int
) -> Ticket:
    response = (
        await supabase_client.table("tickets")
        .select("*")
        .eq("id", ticket_id)
        .eq("user_id", user.id)
        .execute()
    )
    return Ticket(**response.data[0])


@supabase_response_validator
async def ticket_update(
    supabase_client: AsyncClient, user: User, ticket_id: int, schema: TicketUncommited
) -> Ticket:
    response = (
        await supabase_client.table("tickets")
        .update({**schema.model_dump()})
        .eq("id", ticket_id)
        .eq("user_id", user.id)
        .execute()
    )

    return Ticket(**response.data[0])


@supabase_response_validator
async def ticket_delete(
    supabase_client: AsyncClient, user: User, ticket_id: int
) -> bool:
    response = (
        await supabase_client.table("tickets")
        .delete()
        .eq("id", ticket_id)
        .eq("user_id", user.id)
        .execute()
    )

    return bool(response.data)
