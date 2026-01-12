import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
memory = []

def store(text):
    emb = model.encode([text])
    index.add(emb)
    memory.append(text)

def retrieve(query, k=3):
    emb = model.encode([query])
    D,I = index.search(emb, k)
    return [memory[i] for i in I[0]]
