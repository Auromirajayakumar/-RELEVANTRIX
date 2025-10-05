import feedparser
import json

feeds = [
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "https://feeds.bbci.co.uk/news/world/rss.xml",
    "https://hnrss.org/frontpage"
]

def fetch_articles():
    articles = {}
    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            articles[entry.title] = entry.summary
    return articles

def save_articles(articles, path="data/docs.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2)

if __name__ == "__main__":
    articles = fetch_articles()
    save_articles(articles)