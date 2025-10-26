import json, datetime, os

def log_query(query, answer):
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "query": query,
        "answer_preview": answer[:100]
    }
    os.makedirs("data/logs", exist_ok=True)
    with open("data/logs/audit_log.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")