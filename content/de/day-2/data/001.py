import streamlit as st
from lib.helper_ollama import ollama

st.title("Universeller Prompt-Playground")
prompt = st.text_area("Prompt eingeben", height=150)
temperature = st.slider("Temperature (Kreativität)", 0.0, 2.0, 0.7, 0.1)
max_tokens = st.slider("Max Tokens", 50, 500, 200)

if st.button("Generieren") and prompt:
    result = ollama.generate(prompt, temperature=temperature, max_tokens=max_tokens)
    st.write("**Antwort:**")
    st.write(result)
