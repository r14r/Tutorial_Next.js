## miniapp-04
import streamlit as st
from lib.helper_ollama import ollama

st.title("FAQ-Bot")
faq_file = st.file_uploader("FAQ-Datei hochladen (txt)", type="txt")
frage = st.text_input("Stelle eine Frage")

if faq_file and frage:
    faq_content = faq_file.read().decode()
    prompt = f"Beantworte die folgende Frage basierend auf dieser FAQ:\n\nFAQ:\n{faq_content}\n\nFrage: {frage}"
    
    if st.button("Antworten"):
        antwort = ollama.generate(prompt)
        st.write("**Antwort:**", antwort)
