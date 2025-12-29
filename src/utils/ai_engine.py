class AIEngine:
    def __init__(self):
        self.questions = [
            "Por que você quer trabalhar como desenvolvedor Java?",
            "Quais são suas experiências anteriores com Java?",
            "Como você lida com prazos apertados?",
            "Você pode descrever um projeto em que trabalhou e qual foi seu papel?",
            "Como você se mantém atualizado com as novas tecnologias?"
        ]

    def get_question(self, index):
        if 0 <= index < len(self.questions):
            return self.questions[index]
        return None

    def generate_feedback(self, response):
        # Simple feedback generation based on keywords in the response
        if "experiência" in response.lower():
            return "Ótimo! A experiência prática é muito valiosa."
        elif "aprendizado" in response.lower():
            return "É importante sempre buscar aprender mais."
        else:
            return "Obrigado pela sua resposta!"