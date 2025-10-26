import subprocess
import os

def ask_local_ai(prompt):
    """Send a prompt to the local Ollama model and return its response."""
    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def main():
    file_path = input("Enter path to text document: ").strip()

    # Expand ~ to full home directory path if needed
    if file_path.startswith("~"):
        file_path = os.path.expanduser(file_path)

    # Ensure the file exists
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    # Read document content
    with open(file_path, "r") as f:
        doc_text = f.read()

    print("\n✅ AI ready! Ask questions about the document (type 'exit' to quit).\n")

    while True:
        query = input("Your question: ").strip()
        if query.lower() == "exit":
            print("👋 Goodbye!")
            break

        # Combine the doc text and the user’s question
        full_prompt = (
            f"Answer the following question based on this document:\n\n"
            f"--- DOCUMENT START ---\n{doc_text}\n--- DOCUMENT END ---\n\n"
            f"Question: {query}\nAnswer clearly and concisely:"
        )

        response = ask_local_ai(full_prompt)
        print("\n💬 " + response + "\n")

if __name__ == "__main__":
    main()
