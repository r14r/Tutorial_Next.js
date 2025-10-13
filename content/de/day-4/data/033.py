import streamlit as st
import pandas as pd
import json
from lib.helper_ollama import ollama

st.title("Multi-Source Data Fusion")

st.write("Lade verschiedene Datenquellen und lasse sie von der KI intelligent kombinieren.")

# Verschiedene Datentypen
col1, col2 = st.columns(2)

with col1:
    st.subheader("Strukturierte Daten")
    csv_file = st.file_uploader("CSV-Datei", type="csv")
    
with col2:
    st.subheader("Unstrukturierte Daten")
    text_file = st.file_uploader("Text-Datei", type="txt")

# JSON-Eingabe
json_text = st.text_area("JSON-Daten (optional):")

# Kombinationsanalyse
if csv_file or text_file or json_text:
    sources = []
    
    if csv_file:
        df = pd.read_csv(csv_file)
        csv_summary = f"CSV-Daten:\nShape: {df.shape}\nSpalten: {df.columns.tolist()}\nStatistik:\n{df.describe().to_string()}"
        sources.append(csv_summary)
        st.write("**CSV geladen:**", df.shape)
    
    if text_file:
        text_content = text_file.read().decode()
        text_summary = f"Text-Daten:\nLänge: {len(text_content)} Zeichen\nInhalt (Auszug): {text_content[:500]}..."
        sources.append(text_summary)
        st.write("**Text geladen:**", len(text_content), "Zeichen")
    
    if json_text:
        try:
            json_data = json.loads(json_text)
            json_summary = f"JSON-Daten:\nStruktur: {json.dumps(json_data, indent=2)[:500]}..."
            sources.append(json_summary)
            st.write("**JSON geparst:** ✅")
        except:
            st.warning("JSON nicht valid")
    
    # Fusion und Analyse
    if st.button("Daten fusionieren und analysieren") and sources:
        fusion_prompt = f"""Analysiere und kombiniere diese verschiedenen Datenquellen intelligent:

{chr(10).join(sources)}

Aufgaben:
1. Identifiziere Verbindungen zwischen den Datenquellen
2. Finde Muster und Trends
3. Erkenne Widersprüche oder Anomalien
4. Gib zusammenfassende Insights
5. Empfehle weitere Analyseschritte

Antwort als strukturierter Bericht:"""
        
        result = ollama.generate(fusion_prompt)
        st.subheader("Fusionsanalyse")
        st.write(result)
        
        # Zusätzlich: Spezifische Fragen stellen
        custom_question = st.text_input("Spezifische Frage zu den kombinierten Daten:")
        if st.button("Frage stellen") and custom_question:
            question_prompt = f"Beantworte diese Frage basierend auf allen Datenquellen:\n\n{chr(10).join(sources)}\n\nFrage: {custom_question}"
            answer = ollama.generate(question_prompt)
            st.write("**Antwort:**", answer)
