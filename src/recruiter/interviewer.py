class Interviewer:
    def __init__(self):
        self.questions = [
            "Pode me falar sobre sua experiência com Java?",
            "Quais frameworks Java você já utilizou?",
            "Como você lida com prazos apertados?",
            "Você já trabalhou em equipe? Como foi essa experiência?",
            "O que você faz para se manter atualizado sobre novas tecnologias?"
        ]

    def ask_question(self, question_index):
        if 0 <= question_index < len(self.questions):
            return self.questions[question_index]
        else:
            return "Índice de pergunta inválido."

    def evaluate_response(self, response):
        # Simulação de avaliação de resposta
        if len(response) > 20:
            return "Resposta satisfatória."
        else:
            return "Resposta precisa ser mais elaborada."