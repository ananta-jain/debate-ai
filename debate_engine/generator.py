from transformers import pipeline

class ArgumentGenerator:
    def __init__(self):
        self.generator = pipeline("text-generation", model="gpt2")

    def generate_argument(self, topic, stance):
        prompt = f"""Debate Topic: {topic}
Argue {stance}:
Claim:
Reason:
Evidence:"""
        response = self.generator(prompt, max_length=150, temperature=0.7)
        return response[0]['generated_text']
 
