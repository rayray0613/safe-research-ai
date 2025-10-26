# app/main.py
from safety import safety_check
from retrieval import load_document
from embeddings import create_embedding
from audit_log import log

# Optional: if using OpenAI GPT
import openai

# Set your API key (replace with your own)
# openai.api_key = "YOUR_OPENAI_API_KEY"

def ask_ai(document_text, query):
    if not safety_check(query):
        return "Query blocked: unsafe content detected."
    
    # For demo purposes, we'll just simulate GPT response
    # In future: use OpenAI API call here
    # Example:
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[{"role": "system", "content": document_text},
    #               {"role": "user", "content": query}]
    # )
    # answer = response.choices[0].message.content
    
    # Minimal demo: return a snippet from document containing keyword
    keyword = query.split()[0].lower()
    for line in document_text.splitlines():
        if keyword in line.lower():
            answer = line
            break
    else:
        answer = "No relevant information found in document."
    
    log(query, answer)
    return answer

if __name__ == "__main__":
    file_path = input("Enter path to text document: ")
    doc = load_document(file_path)
    
    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() == "exit":
            break
        answer = ask_ai(doc, query)
        print("AI Answer:", answer)
