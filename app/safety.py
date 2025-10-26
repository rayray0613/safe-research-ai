def safety_check(query: str) -> bool:
    forbidden_keywords = [
        "synthesize", "explosive", "weapon", "hack", "virus",
        "personal data", "PII", "social security", "phishing"
    ]
    return not any(word in query.lower() for word in forbidden_keywords)