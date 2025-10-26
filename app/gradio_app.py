# app/gradio_app.py
import gradio as gr
from main import ask_local_ai  # Make sure this function takes a string and returns a string

# Function to handle chat
def chat_with_ai(user_input, chat_history):
    if not chat_history:
        chat_history = []
    answer = ask_local_ai(user_input)  # Call your AI
    chat_history.append((user_input, answer))
    return chat_history, chat_history

# Build Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## 🧠 Safe Research AI Chatbot\nAsk questions about your research or study materials!")
    
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(label="Type your question here and press Enter")
    
    user_input.submit(chat_with_ai, [user_input, chatbot], [chatbot, chatbot])

# Launch locally or on Hugging Face Spaces
demo.launch()
