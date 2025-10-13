import streamlit as st
import pandas as pd
import time
from datetime import datetime
from lib.helper_ollama import ollama

st.title("Real-time Content Monitoring")

# Initialisiere Session State
if 'monitoring_data' not in st.session_state:
    st.session_state.monitoring_data = []

# Input für neuen Content
new_content = st.text_area("Neuen Content hinzufügen:")
source = st.text_input("Quelle (z.B. Website, Social Media):")

if st.button("Content analysieren") and new_content:
    # Analysiere Content
    prompt = f"""Analysiere diesen Content schnell:
- Sentiment (1-10)
- Kategorie (News/Marketing/Info/etc.)
- Dringlichkeit (niedrig/mittel/hoch)
- Keywords (top 3)

Content: {new_content}"""
    
    analyse = ollama.generate(prompt)
    
    # Speichere in Session State
    st.session_state.monitoring_data.append({
        "Timestamp": datetime.now().strftime("%H:%M:%S"),
        "Source": source,
        "Content": new_content[:100] + "..." if len(new_content) > 100 else new_content,
        "Analyse": analyse
    })

# Dashboard anzeigen
if st.session_state.monitoring_data:
    st.subheader("Live Dashboard")
    df = pd.DataFrame(st.session_state.monitoring_data)
    st.dataframe(df)
    
    # Statistiken
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Gesamt Inhalte", len(st.session_state.monitoring_data))
    with col2:
        st.metric("Letzte Aktualisierung", df.iloc[-1]["Timestamp"])
    with col3:
        if st.button("Dashboard leeren"):
            st.session_state.monitoring_data = []
            st.experimental_rerun()
