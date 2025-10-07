import streamlit as st
import requests

st.title("Prompt Playground")
prompt = st.text_area("Prompt eingeben", height=150)

if st.button("Abschicken") and prompt:
    response = requests.post("http://localhost:11434/api/generate",
                             json={"model": "llama2", "prompt": prompt})
    st.subheader("Antwort")
    st.write(response.json()["response"])
