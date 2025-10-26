# app/main.py
import subprocess
import os

def ask_local_ai(prompt: str) -> str:
    """
    Send a prompt to the local Ollama model and return its response.
    """
    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def ask_document_ai(doc_text: str, query: str) -> str:
    """
    Combine document text with user question and return AI response.
    """
    full_prompt = (
        f"Answer the following question based on this document:\n\n"
        f"--- DOCUMENT START ---\n{doc_text}\n--- DOCUMENT END ---\n\n"
        f"Question: {query}\nAnswer clearly and concisely:"
    )
    return ask_local_ai(full_prompt)

# Optional helper to load a document from a path
def load_document(file_path: str) -> str:
    """
    Load a document from the given file path.
    Expands ~ and checks existence.
    """
    if file_path.startswith("~"):
        file_path = os.path.expanduser(file_path)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found: {file_path}")

    with open(file_path, "r") as f:
        return f.read()
