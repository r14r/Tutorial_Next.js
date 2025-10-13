import streamlit as st
import json
from lib.helper_ollama import ollama

st.title("JSON-Datenextraktor")
text = st.text_area("Text eingeben (z.B. Produktbeschreibung):")

if st.button("Daten extrahieren") and text:
    json_prompt = f"""
Extrahiere die wichtigsten Informationen aus dem folgenden Text und gib sie im JSON-Format zurück:

Text: {text}

Gib die Antwort nur als valides JSON zurück mit folgender Struktur:
{{
    "hauptthema": "...",
    "wichtige_punkte": ["...", "..."],
    "stimmung": "positiv/neutral/negativ",
    "sprache": "..."
}}

JSON:"""
    
    result = ollama.generate(json_prompt)
    st.write("**Extrahierte Daten:**")
    st.code(result, language='json')
    
    try:
        parsed = json.loads(result)
        st.write("**Strukturiert:**")
        st.json(parsed)
    except:
        st.warning("JSON konnte nicht geparst werden.")
