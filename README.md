RELEVANTRIX : Real-Time Semantic Search Engine

RELEVANTRIX is a modular search engine that ingests real-time news articles via RSS feeds and ranks them using semantic similarity.
Built for scale, clarity, and production-grade relevance.

🔧 Features

📡 Real-time ingestion from NYT, BBC, Hacker News

🧠 Semantic search using sentence-transformer embeddings

⚡ REST API with FastAPI

🖥️ Optional UI with Streamlit

🗂️ Clean architecture for caching, feedback, and analytics

🚀 Tech Stack

Python

Sentence Transformers
 (all-MiniLM-L6-v2)

FastAPI

Streamlit

feedparser (RSS ingestion)

📁 Project Structure
RELEVANTRIX/
├── data/                # Ingested articles (docs.json)
├── rss_ingestor.py      # RSS ingestion
├── search_engine.py     # Semantic search logic
├── api.py               # REST API
├── app.py               # Streamlit UI
├── requirements.txt     # Dependencies
└── README.md            # Documentation

🧪 How to Run

Install dependencies

pip install -r requirements.txt


Ingest articles

python rss_ingestor.py


Run semantic search

from search_engine import semantic_search
print(semantic_search("artificial intelligence"))


Start API

uvicorn api:app --reload


Launch UI

streamlit run app.py


👉 Example Query:

semantic_search("climate change impact")


🔎 Returns top 5 most relevant real-time news articles ranked by semantic similarity.
