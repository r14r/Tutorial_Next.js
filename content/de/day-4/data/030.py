import streamlit as st
import pandas as pd
import plotly.express as px
from lib.helper_ollama import ollama

st.title("Business Intelligence Dashboard")

# Daten hochladen
uploaded_file = st.file_uploader("Geschäftsdaten (CSV) hochladen", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Grundlegende Visualisierung
    st.subheader("Datenübersicht")
    st.dataframe(df.head())
    
    # Automatische Diagramme
    if st.button("Automatische Visualisierung"):
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        if len(numeric_cols) >= 2:
            fig = px.scatter(df, x=numeric_cols[0], y=numeric_cols[1])
            st.plotly_chart(fig)
    
    # KI-basierte Analyse
    st.subheader("KI-Geschäftsanalyse")
    analyse_typ = st.selectbox("Analyse-Typ:", 
                              ["Umsatztrends", "Kundenverhalten", "Kostenoptimierung", "Marktchancen"])
    
    if st.button("Analysieren"):
        stats = df.describe().to_string()
        
        if analyse_typ == "Umsatztrends":
            prompt = f"Analysiere diese Geschäftsdaten und identifiziere Umsatztrends. Gib konkrete Empfehlungen:\n{stats}"
        elif analyse_typ == "Kundenverhalten":
            prompt = f"Analysiere das Kundenverhalten basierend auf diesen Daten:\n{stats}"
        elif analyse_typ == "Kostenoptimierung":
            prompt = f"Identifiziere Kostenoptimierungsmöglichkeiten in diesen Daten:\n{stats}"
        else:
            prompt = f"Identifiziere neue Marktchancen basierend auf diesen Daten:\n{stats}"
        
        result = ollama.generate(prompt)
        st.write("**KI-Empfehlungen:**", result)
