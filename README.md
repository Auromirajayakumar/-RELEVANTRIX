# RELEVANTRIX : Real-Time Semantic Search Engine

RELEVANTRIX is a modular search engine that ingests real-time news articles via RSS feeds and ranks them using semantic similarity. Built for scale, clarity, and production-grade relevance.

## 🔧 Features
- Real-time ingestion from NYT, BBC, Hacker News
- Semantic search using sentence-transformer embeddings
- REST API with FastAPI
- Optional UI with Streamlit
- Clean architecture for caching, feedback, and analytics

## 🚀 Tech Stack
- Python
- Sentence Transformers (`all-MiniLM-L6-v2`)
- FastAPI
- Streamlit
- RSS via `feedparser`

## 📁 Project Structure
RELEVANTRIX/ ├── data/                 # Ingested articles (docs.json) ├── rss_ingestor.py       # RSS ingestion ├── search_engine.py      # Semantic search logic ├── api.py                # REST API ├── app.py                # Streamlit UI ├── requirements.txt      # Dependencies └── README.md             # Documentation

## 🧪 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
### 2. Ingest articles
python rss_ingestor.py
### 3.Run semantic search
python
>>> from search_engine import semantic_search
>>> semantic_search("artificial intelligence")
### 4. Start API
uvicorn api:app --reload
### 5. Launch UI
streamlit run app.py
