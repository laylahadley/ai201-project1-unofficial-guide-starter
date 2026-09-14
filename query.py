import os
from dotenv import load_dotenv
from groq import Groq
from retrieve import retrieve  # reuses your Milestone 4 retrieval function

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "openai/gpt-oss-120b"

SYSTEM_PROMPT = """You are a helpful assistant answering questions using ONLY the provided context documents.

Rules:
- Answer strictly using the information in the CONTEXT section below.
- Do not use any outside knowledge, even if you know the answer.
- If the context does not contain enough information to answer the question, respond exactly with: "I don't have enough information on that."
- Do not speculate or fill gaps with general knowledge.
"""


def build_context(chunks):
    parts = []
    for c in chunks:
        parts.append(f"[Source: {c['source']}]\n{c['text']}")
    return "\n\n---\n\n".join(parts)


def ask(question, k=5):
    retrieved = retrieve(question, k=k)
    context = build_context(retrieved)

    user_prompt = f"""CONTEXT:
{context}

QUESTION:
{question}

Answer using only the context above."""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.1,
    )

    answer = response.choices[0].message.content

    # Programmatic source attribution — not left to the LLM to remember
    sources = sorted(set(c["source"] for c in retrieved))

    return {
        "answer": answer,
        "sources": sources,
        "retrieved_chunks": retrieved,
    }


if __name__ == "__main__":
    # Quick CLI test before wiring up the UI
    test_questions = [
        "Which finance professors are known to be strong mentors and write good recommendation letters?",
        "What is the exact recruiting timeline according to the HUSB guide?",
        "What is the weather like in Antarctica?",  # should trigger "not enough info"
    ]
    for q in test_questions:
        result = ask(q)
        print(f"\n=== {q} ===")
        print(result["answer"])
        print("Sources:", result["sources"])
