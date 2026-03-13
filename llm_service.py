import requests




OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3"

SYSTEM_PROMPT = """
You are a helpful assistant.
Always answer using up-to-date information when possible.
"""

def get_llm_response(message: str):

    prompt = f"""
{SYSTEM_PROMPT}

User: {message}
Assistant:
"""

    payload = {
    "model": MODEL,
    "prompt": prompt,
    "stream": False,
    "options": {
        "num_predict": 80,
        "temperature": 0.7
    }
}

    response = requests.post(OLLAMA_URL, json=payload)

    return response.json()["response"]