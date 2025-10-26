from sentence_transformers import SentenceTransformer
import faiss, os, pickle

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_vector_index(doc_texts, index_path="data/vector_index"):
    os.makedirs(index_path, exist_ok=True)
    vectors = model.encode(doc_texts)
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)
    faiss.write_index(index, os.path.join(index_path, "index.faiss"))
    with open(os.path.join(index_path, "texts.pkl"), "wb") as f:
        pickle.dump(doc_texts, f)
    print(f"✅ Index built with {len(doc_texts)} documents.")