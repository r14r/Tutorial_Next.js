import streamlit as st
import pandas as pd
from datetime import datetime
from lib.helper_ollama import ollama

st.title("Automatischer Report Generator")

# Multiple Datenquellen
st.subheader("Datenquellen hinzufügen")
files = st.file_uploader("CSV-Dateien hochladen", type="csv", accept_multiple_files=True)

if files:
    data_summaries = []
    
    for i, file in enumerate(files):
        df = pd.read_csv(file)
        st.write(f"**Datei {i+1}: {file.name}**")
        st.write(f"Shape: {df.shape}")
        
        # Kurze Statistik
        summary = f"Datei: {file.name}\nZeilen: {df.shape[0]}\nSpalten: {df.shape[1]}\nStatistik:\n{df.describe().to_string()}"
        data_summaries.append(summary)
    
    # Report-Typ wählen
    report_typ = st.selectbox("Report-Typ:", 
                             ["Executive Summary", "Detailanalyse", "Vergleichsbericht", "Trend-Report"])
    
    if st.button("Report generieren"):
        all_data = "\n\n".join(data_summaries)
        
        prompt = f"""Erstelle einen professionellen {report_typ} basierend auf folgenden Daten:

{all_data}

Der Report soll enthalten:
1. Management Summary
2. Wichtigste Erkenntnisse
3. Empfehlungen
4. Risiken und Chancen
5. Nächste Schritte

Format: Professioneller Geschäftsbericht"""
        
        result = ollama.generate(prompt)
        
        st.subheader(f"{report_typ} - {datetime.now().strftime('%d.%m.%Y')}")
        st.write(result)
        
        # Download-Button
        st.download_button(
            label="Report als Textdatei herunterladen",
            data=result,
            file_name=f"report_{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain"
        )
