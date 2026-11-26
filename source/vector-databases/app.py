import chromadb

client = chromadb.Client()

collection_name = "test_collection"

collection = client.get_or_create_collection(name=collection_name)


# Text documents
documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "Hello, planet!"},
    {"id": "doc3", "text": "Goodbye, see you later!"},
]

for document in documents:
    collection.upsert(ids=[document["id"]], documents=[document["text"]])

query_text = "Hello, world!"

results = collection.query(query_texts=[query_text], n_results=3)

print(results)