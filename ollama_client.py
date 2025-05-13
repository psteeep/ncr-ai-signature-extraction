import os
import requests

OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'http://localhost:11434')

def generate_signature_prompt(prompt: str) -> str:
    response = requests.post(
        f"{OLLAMA_HOST}/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )
    response.raise_for_status()
    return response.json().get("response", "").strip()
