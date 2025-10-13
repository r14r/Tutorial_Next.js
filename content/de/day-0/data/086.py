# streamlit-ollama.py
import streamlit as st
from lib.helper_ollama import ollama

st.title("Textzusammenfassung mit KI")
text = st.text_area("Text eingeben")
if st.button("Zusammenfassen") and text:
    prompt = f"Fasse den folgenden Text in 1 Satz zusammen:\n{text}"
    result = ollama.generate(prompt)
    st.write(result)
