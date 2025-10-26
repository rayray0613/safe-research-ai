from langchain_community.vectorstores.chroma import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings


# Initialize Chroma vector store
vector_store = Chroma(persist_directory="vector_db", embedding_function=OpenAIEmbeddings())

def store_documents(documents):
    """Add documents to the vector store"""
    vector_store.add_texts(documents)

def retrieve(query, k=1):
    """Retrieve top-k relevant documents semantically"""
    results = vector_store.similarity_search(query, k=k)
    return [r.page_content for r in results]
