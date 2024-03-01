import os
from http import client

from fastapi import APIRouter
from dotenv import load_dotenv
from openai import AsyncOpenAI
from app.dto.QuestionOutputDto import QuestionOutputDto
from app.dto.QuestionInputDto import QuestionInputDto
from app.services.DtoService import process_ai_response

router = APIRouter(
    prefix="",
    tags=['Open AI'],
)

load_dotenv()

client = AsyncOpenAI()


@router.post("/messages", response_model=QuestionOutputDto)
async def get_ai_response(question: QuestionInputDto):
    """
    OpenAI Response
    """
    response = await client.chat.completions.create(
        model=os.environ.get("MODEL"),
        messages=[
            {
                "role": "system",
                "content": (
                    "Generate description for the text as task description"
                ),
            },
            {
                "role": "user",
                "content": question.question,
            },
        ],
        stream=False,
    )

    return process_ai_response(response)
