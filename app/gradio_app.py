# app/gradio_app.py
import gradio as gr
from main import ask_local_ai  # Make sure this matches your main.py function

def chat_with_ai(user_input, chat_history):
    """Handles the chatbot interaction"""
    answer = ask_local_ai(user_input)  # Call your AI function
    chat_history.append((user_input, answer))
    return chat_history, chat_history

# Build Gradio interface
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Ask a question:", placeholder="Type your question here...")
    msg.submit(chat_with_ai, [msg, chatbot], [chatbot, chatbot])

demo.launch(server_name="0.0.0.0", server_port=7860)  # Required for Hugging Face Spaces
