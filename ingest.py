import os
import re
import json
import tiktoken

DATA_DIR = "data"
OUTPUT_FILE = "chunks.json"
CHUNK_SIZE = 500   # tokens
CHUNK_OVERLAP = 50 # tokens

tokenizer = tiktoken.get_encoding("cl100k_base")


def load_documents(data_dir):
    """Load all .txt files from data_dir. Returns list of (filename, raw_text)."""
    docs = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            path = os.path.join(data_dir, filename)
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                raw_text = f.read()
            docs.append((filename, raw_text))
    return docs


def clean_text(text):
    """Remove HTML tags, entities, and excess whitespace."""
    text = re.sub(r"<[^>]+>", " ", text)          # strip HTML tags
    text = re.sub(r"&nbsp;|&amp;|&#\d+;", " ", text)  # strip common HTML entities
    text = re.sub(r"\n{3,}", "\n\n", text)          # collapse excess blank lines
    text = re.sub(r"[ \t]{2,}", " ", text)          # collapse excess spaces
    return text.strip()


def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """Split text into overlapping chunks based on token count."""
    tokens = tokenizer.encode(text)
    chunks = []
    start = 0
    while start < len(tokens):
        end = start + chunk_size
        chunk_tokens = tokens[start:end]
        chunk_str = tokenizer.decode(chunk_tokens)
        chunks.append(chunk_str.strip())
        if end >= len(tokens):
            break
        start = end - overlap  # step forward, keeping overlap
    return chunks


def main():
    docs = load_documents(DATA_DIR)
    print(f"Loaded {len(docs)} documents from '{DATA_DIR}/'")

    all_chunks = []
    for filename, raw_text in docs:
        cleaned = clean_text(raw_text)
        doc_chunks = chunk_text(cleaned)
        for i, chunk in enumerate(doc_chunks):
            all_chunks.append({
                "source": filename,
                "chunk_index": i,
                "text": chunk
            })
        print(f"  {filename}: {len(doc_chunks)} chunks")

    print(f"\nTotal chunks: {len(all_chunks)}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2, ensure_ascii=False)
    print(f"Saved all chunks to {OUTPUT_FILE}")

    print("\n--- Sample chunks (first 5) ---\n")
    for c in all_chunks[:5]:
        print(f"[Source: {c['source']} | Chunk {c['chunk_index']}]")
        print(c["text"])
        print("-" * 60)


if __name__ == "__main__":
    main()
    