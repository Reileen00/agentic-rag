
---

## evaluate.py
```python
from pipeline import retrieve, store

store("User likes finance")
store("User prefers short answers")

hits = retrieve("What should I read?")
print("Retrieved memory:", hits)

print("Memory recall success:", len(hits) > 0)
