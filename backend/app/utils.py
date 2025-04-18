import requests
from config import Config

HF_API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"



headers = {
    "Authorization": f"Bearer {Config.HF_API_KEY}",
    "Content-Type": "application/json"
}

def ask_openai(message):
    prompt = (
        f"Act like a financial advisor. User asks: '{message}'. "
        f"Respond with a numbered list of 3 helpful budgeting tips."
    )

    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.5,
            "max_new_tokens": 100,
            "top_p": 0.9,
            "repetition_penalty": 1.3
        }
    }

    response = requests.post(HF_API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"

    generated = response.json()
    if isinstance(generated, list) and "generated_text" in generated[0]:
        return generated[0]["generated_text"].strip()
    else:
        return "(No valid response from model)"

