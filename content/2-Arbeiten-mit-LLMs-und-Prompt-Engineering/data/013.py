import streamlit as st
import requests

st.title("Prompt-Vergleich")

p1 = st.text_area("Prompt 1")
p2 = st.text_area("Prompt 2")
model = st.selectbox("Modell", ["llama2", "mistral"])

if st.button("Vergleichen"):
    for i, p in enumerate([p1, p2], start=1):
        if p:
            r = requests.post("http://localhost:11434/api/generate",
                              json={"model": model, "prompt": p})
            st.subheader(f"Antwort {i}")
            st.write(r.json()["response"])
