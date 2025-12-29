# AI Recruiter Interview Simulation

This project simulates a real interview experience for the position of Junior Java Developer using artificial intelligence. The application facilitates interaction between a virtual recruiter and a candidate, providing a realistic interview environment.

## Project Structure

```
ai-recruiter-interview
├── src
│   ├── app.py                # Entry point of the application
│   ├── recruiter
│   │   └── interviewer.py     # Simulates the recruiter's behavior
│   ├── candidate
│   │   └── responses.py       # Simulates the candidate's responses
│   ├── utils
│   │   └── ai_engine.py       # Processes natural language and generates questions
│   └── types
│       └── interview_types.py  # Contains types and constants for the interview process
├── requirements.txt           # Lists project dependencies
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-recruiter-interview
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

To start the AI interview simulation, run the following command:
```
python src/app.py
```

The application will initiate an interactive session where the virtual recruiter will ask questions, and the candidate can respond accordingly.

## Overview of Components

- **app.py**: The main entry point that initializes the interview simulation and manages interactions.
- **interviewer.py**: Contains the `Interviewer` class responsible for asking questions and evaluating candidate responses.
- **responses.py**: Contains the `CandidateResponses` class that generates responses based on the interview questions.
- **ai_engine.py**: Implements the `AIEngine` class for processing natural language and generating interview questions and feedback.
- **interview_types.py**: Defines various types and constants related to the interview process, such as question types and response formats.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.