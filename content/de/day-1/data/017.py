import streamlit as st
from lib.helper_ollama import ollama

st.title("Prompt Playground")
prompt = st.text_area("Prompt eingeben", height=150)

if st.button("Abschicken") and prompt:
    result = ollama.generate(prompt)
    st.subheader("Antwort")
    st.write(result)
