# app/retrieval.py
def load_document(file_path: str) -> str:
    """
    Load a text file and return its contents.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
