from transformers import pipeline

class RebuttalEngine:
    def __init__(self):
        self.generator = pipeline("text-generation", model="gpt2")

    def generate_rebuttal(self, counterargument):
        prompt = f"""Counterargument: {counterargument}
Respond with a rebuttal:"""
        response = self.generator(prompt, max_length=100, temperature=0.7)
        return response[0]['generated_text']
