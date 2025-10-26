import faiss, pickle, openai
from embeddings import model
from safety import safety_check
from audit_log import log_query

def search(query, top_k=3):
    index = faiss.read_index("data/vector_index/index.faiss")
    with open("data/vector_index/texts.pkl", "rb") as f:
        texts = pickle.load(f)
    query_vector = model.encode([query])
    _, indices = index.search(query_vector, top_k)
    return [texts[i] for i in indices[0]]

def ask_ai(query):
    if not safety_check(query):
        return "⚠️ Sorry, that question appears unsafe or restricted."
    context = "\n".join(search(query))
    prompt = f"Answer this based on the documents below:\n{context}\n\nQuestion: {query}\n\nInclude citations."
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message["content"]
    log_query(query, answer)
    return answer