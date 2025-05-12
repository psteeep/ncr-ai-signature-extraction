import os
import requests

OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'http://localhost:11434')

response = requests.post(
    f"{OLLAMA_HOST}/api/generate",
    json={
        "model": "mistral",
        "prompt": "Hello, Ollama!",
        "stream": False
    }
)

print(response.json())
