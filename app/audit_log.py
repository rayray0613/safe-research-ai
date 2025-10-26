# app/audit_log.py
import datetime

def log(query: str, response: str):
    timestamp = datetime.datetime.now().isoformat()
    with open("audit_log.txt", "a") as f:
        f.write(f"{timestamp}\nQuery: {query}\nResponse: {response}\n\n")
