from pydantic import BaseModel


class QuestionOutputDto(BaseModel):
    answer: str
