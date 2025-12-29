class CandidateResponses:
    def __init__(self):
        self.responses = {
            "Tell me about yourself.": "I am a recent graduate with a degree in Computer Science. I have a passion for coding and have completed several projects in Java.",
            "What are your strengths?": "I am a quick learner and have strong problem-solving skills. I also work well in a team.",
            "What are your weaknesses?": "I tend to be a perfectionist, which can slow me down at times, but I am working on balancing quality with efficiency.",
            "Why do you want to work here?": "I admire your company's commitment to innovation and would love to contribute to exciting projects as a Junior Java Developer.",
            "Where do you see yourself in five years?": "In five years, I hope to have advanced my skills and taken on more responsibilities, possibly in a lead developer role."
        }

    def get_response(self, question):
        return self.responses.get(question, "I'm not sure how to answer that.")