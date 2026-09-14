import json
import os
import numpy as np
from sentence_transformers import SentenceTransformer

CHUNKS_FILE = "chunks.json"
EMBEDDINGS_FILE = "embeddings.npy"
METADATA_FILE = "embeddings_metadata.json"

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")


def load_chunks(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def embed_and_store(chunks):
    if os.path.exists(EMBEDDINGS_FILE) and os.path.exists(METADATA_FILE):
        print("Embeddings already exist — skipping re-embed.")
        return

    documents = [c["text"] for c in chunks]
    metadatas = [{"source": c["source"], "chunk_index": c["chunk_index"], "text": c["text"]} for c in chunks]

    print(f"Embedding {len(documents)} chunks...")
    embeddings = model.encode(documents, show_progress_bar=True)

    np.save(EMBEDDINGS_FILE, embeddings)
    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(metadatas, f, indent=2, ensure_ascii=False)

    print(f"Stored {len(embeddings)} embeddings to {EMBEDDINGS_FILE}")


def cosine_distance(a, b):
    # 1 - cosine similarity, so lower = more similar (matches ChromaDB's convention)
    a_norm = a / np.linalg.norm(a)
    b_norm = b / np.linalg.norm(b, axis=1, keepdims=True)
    similarities = b_norm @ a_norm
    return 1 - similarities


def retrieve(query, k=5):
    embeddings = np.load(EMBEDDINGS_FILE)
    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        metadatas = json.load(f)

    query_embedding = model.encode([query])[0]
    distances = cosine_distance(query_embedding, embeddings)

    top_k_idx = np.argsort(distances)[:k]

    results = []
    for idx in top_k_idx:
        results.append({
            "text": metadatas[idx]["text"],
            "source": metadatas[idx]["source"],
            "chunk_index": metadatas[idx]["chunk_index"],
            "distance": float(distances[idx])
        })
    return results


def print_results(query, results):
    print(f"\n=== Query: \"{query}\" ===")
    for i, r in enumerate(results):
        print(f"\n--- Result {i+1} | Source: {r['source']} | Distance: {r['distance']:.3f} ---")
        print(r["text"])


if __name__ == "__main__":
    chunks = load_chunks(CHUNKS_FILE)
    embed_and_store(chunks)

    # Replace these with 3 of your actual 5 evaluation questions
    test_queries = [
        "Which finance professors are known to be strong mentors and write good recommendation letters?",
        "What is the recruiting timeline for finance and business students according to the HUSB guide?",
        "What resources does the HPS Center for Financial Excellence provide for Wall Street recruiting?",
    ]

    for q in test_queries:
        results = retrieve(q, k=5)
        print_results(q, results)