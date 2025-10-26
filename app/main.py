import streamlit as st
from retrieval import ask_ai

st.title("🔬 Safe Research AI Assistant")
query = st.text_input("Ask a research question:")
if st.button("Ask"):
    if query.strip():
        st.write(ask_ai(query))