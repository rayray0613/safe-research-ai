# app/embeddings.py
from langchain.embeddings import OpenAIEmbeddings

def create_embeddings(documents):
    """
    Convert a list of text documents into embeddings
    """
    embeddings = OpenAIEmbeddings()
    doc_vectors = [embeddings.embed_query(doc) for doc in documents]
    return doc_vectors
