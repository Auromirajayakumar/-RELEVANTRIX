import streamlit as st
from search_engine import semantic_search

st.title("LiveRank: Real-Time Semantic Search")
query = st.text_input("Enter your search query:")
if query:
    results = semantic_search(query)
    for title, score in results:
        st.write(f"**{title}** — Score: {score:.2f}")