# app/main.py
import os
from safety import safety_check
from retrieval import store_documents, retrieve
from audit_log import log
from langchain_openai import ChatOpenAI  # real ChatGPT

def ask_ai(query):
    if not safety_check(query):
        return "Query blocked: unsafe content detected."

    context = retrieve(query, k=3)

    if not context:
        answer = "No relevant information found in document."
    else:
        # Use ChatOpenAI to answer using the document
        llm = ChatOpenAI(temperature=0)
        answer = llm.predict(
            f"Use the following context to answer the question.\n"
            f"Context: {' '.join(context)}\n"
            f"Question: {query}\nAnswer:"
        )

    log(query, answer)
    return answer

if __name__ == "__main__":
    file_path = input("Enter path to text document: ")
    file_path = os.path.expanduser(file_path)
    
    with open(file_path, "r") as f:
        doc_text = f.read()

    store_documents([doc_text])
    
    print("\nAI ready! Ask questions about the document (type 'exit' to quit).")
    
    while True:
        query = input("\nYour question: ")
        if query.lower() == "exit":
            break
        answer = ask_ai(query)
        print("AI Answer:", answer)
