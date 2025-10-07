import streamlit as st
import requests

st.title("Sentiment Analyse")

text = st.text_area("Text eingeben")
if st.button("Analysieren"):
    prompt = f"Stimmung (Positiv/Negativ/Neutral): {text}"
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    st.write("Stimmung:", r.json()["response"])
