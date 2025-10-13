import streamlit as st
from lib.helper_ollama import ollama

st.title("Dokument-Zusammenfassung mit Ollama")
file = st.file_uploader("Textdatei hochladen", type=["txt"])

if file:
    text = file.read().decode()
    prompt = f"Fasse den folgenden Text in 5 Sätzen zusammen:\n\n{text}"
    summary = ollama.generate(prompt)
    st.subheader("Zusammenfassung")
    st.write(summary)
