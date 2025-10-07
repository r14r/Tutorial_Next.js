import streamlit as st
import requests

st.title("Textanalyse Dashboard")

text = st.text_area("Text eingeben")

if st.button("Analysieren") and text:
    prompt = """
Analysiere diesen Text:
1. Stimmung (Positiv/Negativ/Neutral)
2. Keywords
3. Named Entities (Personen, Orte, Organisationen)
4. Zusammenfassung in 2 Sätzen
Text: %s
""" % text
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    st.subheader("Analyse-Ergebnis")
    st.write(r.json()["response"])
