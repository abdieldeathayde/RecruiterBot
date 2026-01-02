# AI Recruiter Interview Simulation

This project simulates a real interview experience for the position of Junior Java Developer using artificial intelligence. The application facilitates interaction between a virtual recruiter and a candidate, providing a realistic interview environment.

# Simulação de Entrevista com IA

Este projeto simula uma experiência de entrevista real para a vaga de Desenvolvedor Java Júnior usando inteligência artificial. A aplicação facilita a interação entre um recrutador virtual e um candidato, proporcionando um ambiente de entrevista realista.

## Estrutura do Projeto

```
ai-recruiter-interview
├── src
│   ├── app.py                # Ponto de entrada da aplicação
│   ├── recruiter
│   │   └── interviewer.py     # Simula o comportamento do recrutador
│   ├── candidate
│   │   └── responses.py       # Simula as respostas do candidato
│   ├── utils
│   │   └── ai_engine.py       # Processa linguagem natural e gera perguntas
│   └── types
│       └── interview_types.py  # Contém tipos e constantes do processo de entrevista
├── requirements.txt           # Lista dependências do projeto
└── README.md                  # Documentação do projeto
```

## Instruções de Instalação

1. Clone o repositório:
   ```bash
   git clone <repository-url>
   cd ai-recruiter-interview
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

Para iniciar a simulação de entrevista com IA, execute o seguinte comando:
```
python src/app.py
```

A aplicação iniciará uma sessão interativa onde o recrutador virtual fará perguntas e o candidato poderá responder.

## Visão Geral dos Componentes

- **app.py**: Ponto de entrada que inicializa a simulação de entrevista e gerencia as interações.
- **interviewer.py**: Contém a classe `Interviewer` responsável por fazer perguntas e avaliar respostas dos candidatos.
- **responses.py**: Contém a classe `CandidateResponses` que gera respostas baseadas nas perguntas da entrevista.
- **ai_engine.py**: Implementa a classe `AIEngine` para processamento de linguagem natural e geração de perguntas e feedback.
- **interview_types.py**: Define diversos tipos e constantes relacionados ao processo de entrevista, como tipos de perguntas e formatos de resposta.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar um pull request ou abrir uma issue com sugestões ou melhorias.