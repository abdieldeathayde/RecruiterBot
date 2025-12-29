import random
from recruiter.interviewer import Interviewer
from candidate.responses import CandidateResponses
from utils.ai_engine import AIEngine

def main():
    print("Iniciando a simulação de entrevista...")
    
    interviewer = Interviewer()
    candidate_responses = CandidateResponses()
    ai_engine = AIEngine()

    questions = interviewer.prepare_questions()
    
    for question in questions:
        print(f"Entrevistador: {question}")
        response = candidate_responses.generate_response(question)
        print(f"Candidato: {response}")
        feedback = ai_engine.evaluate_response(question, response)
        print(f"Feedback: {feedback}")

if __name__ == "__main__":
    main()