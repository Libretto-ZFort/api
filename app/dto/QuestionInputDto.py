from pydantic import BaseModel


class QuestionInputDto(BaseModel):
    question: str
