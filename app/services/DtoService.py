from app.dto.QuestionOutputDto import QuestionOutputDto


def process_ai_response(open_ai_response):
    if open_ai_response.choices[0].finish_reason != "stop":
        return {'answer': "Something wrong with request"}
    return {'answer': open_ai_response.choices[0].message.content}
