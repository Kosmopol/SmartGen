import requests

class AIAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_text(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "Tu es un rédacteur SEO professionnel."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        completion = response.json()
        return completion["choices"][0]["message"]["content"]
