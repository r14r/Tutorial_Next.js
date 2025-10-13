import streamlit as st
import pandas as pd
import sqlite3
from lib.helper_ollama import ollama

st.title("Smart Data Query Interface")

# Daten laden
uploaded_file = st.file_uploader("CSV-Datei hochladen", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("**Datenvorschau:**")
    st.dataframe(df.head())
    
    # Spaltennamen anzeigen
    st.write("**Verfügbare Spalten:**", ", ".join(df.columns.tolist()))
    
    # Natürlichsprachliche Abfrage
    st.subheader("Stelle eine Frage zu den Daten")
    question = st.text_input("Frage (z.B. 'Was ist der Durchschnittswert der Spalte X?'):")
    
    if st.button("Abfrage ausführen") and question:
        # Erst KI nach SQL-Query fragen
        schema_info = f"Tabelle mit Spalten: {', '.join(df.columns)}\nDatentypen: {df.dtypes.to_string()}"
        
        sql_prompt = f"""Konvertiere diese natürlichsprachliche Frage in eine SQL-Query:

Schema: {schema_info}
Frage: {question}

Gib nur die SQL-Query zurück, ohne Erklärung:"""
        
        sql_query = ollama.generate(sql_prompt).strip()
        st.write("**Generierte SQL-Query:**", sql_query)
        
        try:
            # SQL ausführen (vereinfacht mit pandas)
            # In Realität würde man eine echte SQL-Engine verwenden
            conn = sqlite3.connect(':memory:')
            df.to_sql('data', conn, index=False)
            
            result_df = pd.read_sql_query(sql_query.replace('data', 'data'), conn)
            st.write("**Ergebnis:**")
            st.dataframe(result_df)
            
        except Exception as e:
            st.error(f"Fehler bei SQL-Ausführung: {e}")
            
            # Fallback: Direkte Antwort von KI
            fallback_prompt = f"""Beantworte diese Frage basierend auf den Daten:

Datenstatistik: {df.describe().to_string()}
Spalten: {df.columns.tolist()}
Frage: {question}"""
            
            fallback_result = ollama.generate(fallback_prompt)
            st.write("**KI-Antwort:**", fallback_result)
