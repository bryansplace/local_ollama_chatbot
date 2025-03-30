import gradio as gr
import requests
import os

OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

def chat_with_ollama(prompt):
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={"model": "tinyllama", "prompt": prompt,"stream": False}
    )
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Error communicating with Ollama."

iface = gr.Interface(
    fn=chat_with_ollama,
 #   type="messages",
    inputs=gr.Textbox(label="Your Message"),
    outputs=gr.Textbox(label="Ollama's Response"),
    title="Bryan's Chatbot",
    description="Talk to my AI"
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)