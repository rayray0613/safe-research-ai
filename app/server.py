# app/server.py
from fastapi import FastAPI
from pydantic import BaseModel
from .main import ask_local_ai  # relative import works with __init__.py

app = FastAPI(title="Safe Research AI Web Server")

class Question(BaseModel):
    text: str
    doc_path: str  # path to the document to query

@app.post("/ask")
def ask_ai(q: Question):
    try:
        # Read document content
        with open(q.doc_path, "r") as f:
            doc_text = f.read()
    except FileNotFoundError:
        return {"error": f"File not found: {q.doc_path}"}

    # Ask your AI
    response = ask_local_ai(f"Answer based on this document:\n\n{doc_text}\n\nQuestion: {q.text}")
    return {"answer": response}

@app.get("/")
def home():
    return {"message": "Safe Research AI server is running! Use POST /ask to query the AI."}
