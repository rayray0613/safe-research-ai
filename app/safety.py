# app/safety.py
def safety_check(query: str) -> bool:
    """
    Returns True if the query is safe to process.
    Filters out unsafe topics (e.g., hacking, explosives, personal data)
    """
    unsafe_keywords = ["hack", "explosive", "terrorist", "password"]
    query_lower = query.lower()
    for word in unsafe_keywords:
        if word in query_lower:
            return False
    return True
