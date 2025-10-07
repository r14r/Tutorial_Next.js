import streamlit as st
import requests

st.title("Prompt Playground")
model = st.selectbox("Modell wählen", ["llama2", "mistral"])
prompt = st.text_area("Prompt eingeben")

if st.button("Start") and prompt:
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": model, "prompt": prompt})
    st.markdown(r.json()["response"])
