from enum import Enum

class QuestionType(Enum):
    TECHNICAL = "Technical"
    BEHAVIORAL = "Behavioral"
    HR = "HR"

class ResponseFormat(Enum):
    TEXT = "Text"
    AUDIO = "Audio"
    VIDEO = "Video"

INTERVIEW_DURATION_MINUTES = 30
MAX_QUESTIONS = 10

def get_question_types():
    return [question_type.value for question_type in QuestionType]

def get_response_formats():
    return [response_format.value for response_format in ResponseFormat]