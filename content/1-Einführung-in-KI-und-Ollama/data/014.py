import streamlit as st
import requests

st.title("Dokument-Zusammenfassung mit Ollama")
file = st.file_uploader("Textdatei hochladen", type=["txt"])

if file:
    text = file.read().decode()
    prompt = f"Fasse den folgenden Text in 5 Sätzen zusammen:\n\n{text}"
    response = requests.post("http://localhost:11434/api/generate",
                             json={"model": "llama2", "prompt": prompt})
    summary = response.json()["response"]
    st.subheader("Zusammenfassung")
    st.write(summary)
