# app/main.py
import os
from safety import safety_check
from retrieval import store_documents, retrieve
from audit_log import log
from langchain_openai import ChatOpenAI
from langchain_core.prompts.prompt import PromptTemplate  # Updated import

def ask_ai(query):
    if not safety_check(query):
        return "Query blocked: unsafe content detected."
    
    # Retrieve top 3 relevant documents
    context = retrieve(query, k=3)
    
    if not context:
        answer = "No relevant information found in document."
    else:
        # Create prompt for GPT
        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="Use the following context to answer the question.\nContext: {context}\nQuestion: {question}\nAnswer:"
        )
        final_prompt = prompt.format(context="\n".join(context), question=query)
        
        # Call GPT
        llm = ChatOpenAI(temperature=0)
        answer = llm.predict(final_prompt)
    
    log(query, answer)
    return answer

if __name__ == "__main__":
    file_path = input("Enter path to text document: ")
    file_path = os.path.expanduser(file_path)  # <-- this expands '~' automatically
    
    # Load document
    with open(file_path, "r") as f:
        doc_text = f.read()
    
    # Store in vector database
    store_documents([doc_text])
    
    print("\nAI ready! Ask questions about the document (type 'exit' to quit).")
    
    while True:
        query = input("\nYour question: ")
        if query.lower() == "exit":
            break
        answer = ask_ai(query)
        print("AI Answer:", answer)
