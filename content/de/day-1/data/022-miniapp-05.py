## miniapp-05
import streamlit as st
from lib.helper_ollama import ollama

st.title("KI-Sprachübersetzer")
text = st.text_area("Text zum Übersetzen")
von_sprache = st.selectbox("Von Sprache", ["Deutsch", "Englisch", "Französisch", "Spanisch"])
zu_sprache = st.selectbox("Zu Sprache", ["Englisch", "Deutsch", "Französisch", "Spanisch"])

if st.button("Übersetzen") and text and von_sprache != zu_sprache:
    prompt = f"Übersetze den folgenden Text von {von_sprache} zu {zu_sprache}: {text}"
    result = ollama.generate(prompt)
    st.write("**Übersetzung:**")
    st.write(result)
