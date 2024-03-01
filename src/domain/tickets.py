from enum import Enum

from pydantic import Field

from src.infrastructure.application import InternalEntity


class TicketStatusEnum(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"


class TicketUncommited(InternalEntity):
    title: str = Field(description="The title of the ticket")
    description: str | None = Field(
        default=None,
        description=(
            "The description is going to be optimized or even generated with OpenAI"
        ),
    )
    status: TicketStatusEnum


class Ticket(TicketUncommited):
    id: int
