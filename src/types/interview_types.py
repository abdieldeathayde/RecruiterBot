from enum import Enum

class QuestionType(Enum):
    TECHNICAL = "Técnico"
    BEHAVIORAL = "Comportamental"
    HR = "RH"

class ResponseFormat(Enum):
    TEXT = "Texto"
    AUDIO = "Áudio"
    VIDEO = "Vídeo"

INTERVIEW_DURATION_MINUTES = 30
MAX_QUESTIONS = 10

def get_question_types():
    return [question_type.value for question_type in QuestionType]

def get_response_formats():
    return [response_format.value for response_format in ResponseFormat]