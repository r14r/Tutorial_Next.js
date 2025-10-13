import streamlit as st
from lib.helper_ollama import ollama

st.title("Multi-Language Content Analyzer")
text = st.text_area("Text eingeben (beliebige Sprache)")

if text:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Spracherkennung & Analyse")
        if st.button("Analysieren"):
            prompt = f"""Analysiere den folgenden Text:
1. Erkenne die Sprache
2. Bestimme die Stimmung
3. Extrahiere Hauptthemen
4. Gib eine kurze Zusammenfassung

Text: {text}"""
            result = ollama.generate(prompt)
            st.write(result)
    
    with col2:
        st.subheader("Übersetzung")
        ziel_sprache = st.selectbox("Übersetzen zu:", 
                                   ["Deutsch", "Englisch", "Französisch", "Spanisch"])
        if st.button("Übersetzen"):
            prompt = f"Übersetze den folgenden Text zu {ziel_sprache}:\n{text}"
            result = ollama.generate(prompt)
            st.write(result)
