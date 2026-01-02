class CandidateResponses:
    def __init__(self):
        self.responses = {
            "Fale sobre você.": "Sou recém-formado em Ciência da Computação, tenho paixão por programação e já realizei vários projetos em Java.",
            "Quais são seus pontos fortes?": "Sou rápido para aprender e tenho forte capacidade de resolução de problemas. Também trabalho bem em equipe.",
            "Quais são suas fraquezas?": "Tenho tendência ao perfeccionismo, o que às vezes me deixa mais lento, mas estou trabalhando em equilibrar qualidade e eficiência.",
            "Por que você quer trabalhar aqui?": "Admiro o compromisso da empresa com a inovação e gostaria de contribuir em projetos interessantes como Desenvolvedor Java Júnior.",
            "Onde você se vê em cinco anos?": "Daqui a cinco anos, espero ter evoluído tecnicamente e assumido mais responsabilidades, possivelmente em um cargo de liderança técnica."
        }

    def get_response(self, question):
        return self.responses.get(question, "Não sei como responder a isso.")