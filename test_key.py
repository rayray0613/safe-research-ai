from openai import OpenAI

client = OpenAI()  # Uses your OPENAI_API_KEY automatically

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Hello world"
)

print("API key works! Embedding length:", len(response.data[0].embedding))

