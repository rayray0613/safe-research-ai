# app/retrieval.py
# Dummy embeddings for local testing
class DummyEmbeddings:
    def embed_documents(self, texts):
        # Return a list of zero vectors (length 1536)
        return [[0.0]*1536 for _ in texts]
    
    def embed_query(self, text):
        # Return a single zero vector for the query
        return [0.0]*1536

from langchain_chroma import Chroma

# Initialize Chroma vector store with dummy embeddings
vector_store = Chroma(persist_directory="vector_db", embedding_function=DummyEmbeddings())

def store_documents(documents):
    """Add documents to the vector store"""
    vector_store.add_texts(documents)

def retrieve(query, k=1):
    """Retrieve top-k relevant documents semantically"""
    results = vector_store.similarity_search(query, k=k)
    return [r.page_content for r in results]
