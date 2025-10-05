from fastapi import FastAPI
from search_engine import semantic_search

app = FastAPI()

@app.get("/search")
def search(query: str):
    results = semantic_search(query)
    return {"results": [{"title": r[0], "score": round(r[1], 3)} for r in results]}