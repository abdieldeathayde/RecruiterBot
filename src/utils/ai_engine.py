# ...existing code...
class AIEngine:
    def __init__(self):
        # ...existing code...
        pass

    def evaluate_response(self, question, response):
        # Delega para implementação existente se disponível
        if hasattr(self, "evaluate"):
            return self.evaluate(question, response)
        if hasattr(self, "assess"):
            return self.assess(question, response)

        # Fallback simples
        if response and len(response) > 20:
            return "Resposta satisfatória."
        return "Resposta precisa ser mais elaborada."
# ...existing code...