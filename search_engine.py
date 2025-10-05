import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load documents
with open("data/docs.json", encoding="utf-8") as f:
    documents = json.load(f)

doc_ids = list(documents.keys())
doc_texts = list(documents.values())

# Load model and encode
model = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = model.encode(doc_texts)

def semantic_search(query, top_k=5):
    query_embedding = model.encode([query])[0]
    scores = cosine_similarity([query_embedding], doc_embeddings).flatten()
    ranked = sorted(zip(doc_ids, scores), key=lambda x: x[1], reverse=True)
    return ranked[:top_k]