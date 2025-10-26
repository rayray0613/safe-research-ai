from fastapi import FastAPI
from pydantic import BaseModel
from main import ask_local_ai

app = FastAPI()

class Question(BaseModel):
    text: str
    doc_path: str

@app.post("/ask")
def ask_ai(q: Question):
    with open(q.doc_path, "r") as f:
        doc_text = f.read()
    prompt = f"Answer based on this document:\n\n{doc_text}\n\nQuestion: {q.text}"
    response = ask_local_ai(prompt)
    return {"answer": response}
