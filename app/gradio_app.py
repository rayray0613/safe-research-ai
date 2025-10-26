# app/gradio_app.py
import gradio as gr
from main import ask_local_ai  # Make sure this exists and returns a string

def chat_with_ai(user_input, chat_history):
    if not chat_history:
        chat_history = []
    answer = ask_local_ai(user_input)  # Your AI logic
    chat_history.append((user_input, answer))
    return chat_history, chat_history

with gr.Blocks() as demo:
    gr.Markdown("## 🧠 Safe Research AI Chatbot\nAsk questions about your research or study materials!")
    
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(label="Type your question here and press Enter")
    
    user_input.submit(chat_with_ai, [user_input, chatbot], [chatbot, chatbot])

demo.launch(server_name="0.0.0.0", server_port=7860)  # Required for Hugging Face Spaces
