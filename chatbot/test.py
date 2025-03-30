import requests
import json

OLLAMA_URL = "http://localhost:11434"

def chat_with_ollama(prompt):
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={"model": "tinyllama", "prompt": prompt},
        stream=True
    )

    if response.status_code == 200:
        full_response = ""
        for line in response.iter_lines():
            if line:
                try:
                    json_data = json.loads(line.decode("utf-8"))
                    if "response" in json_data:
                        full_response += json_data["response"]  # Accumulate responses
                    if json_data.get("done", False):  # Stop when done
                        break
                except json.JSONDecodeError:
                    continue  # Skip malformed lines
        print("Final Response:", full_response.strip())  # Debugging
        return full_response.strip()
    else:
        return "Error communicating with Ollama."

# Test with a sample prompt
print(chat_with_ollama("stop"))