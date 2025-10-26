from fastapi import FastAPI
from pydantic import BaseModel
from .main import ask_local_ai  # relative import

app = FastAPI(title="Safe Research AI Web Server")

class Question(BaseModel):
    text: str
    doc_path: str  # path to the document to query

@app.get("/")
def home():
    return {"message": "Safe Research AI server is running!"}

@app.post("/ask")
def ask_ai(q: Question):
    try:
        with open(q.doc_path, "r") as f:
            doc_text = f.read()
    except FileNotFoundError:
        return {"error": f"File not found: {q.doc_path}"}

    response = ask_local_ai(f"Answer based on this document:\n\n{doc_text}\n\nQuestion: {q.text}")
    return {"answer": response}
