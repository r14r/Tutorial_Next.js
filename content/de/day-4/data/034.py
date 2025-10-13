import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
from lib.helper_ollama import ollama

st.title("Predictive Analytics Interface")

uploaded_file = st.file_uploader("Zeitreihen-Daten (CSV) hochladen", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Datenvorschau")
    st.dataframe(df.head())
    
    # Spalten für Analyse auswählen
    date_col = st.selectbox("Datums-Spalte:", df.columns)
    value_col = st.selectbox("Wert-Spalte:", df.select_dtypes(include=['float64', 'int64']).columns)
    
    if date_col and value_col:
        # Daten vorbereiten
        try:
            df[date_col] = pd.to_datetime(df[date_col])
            df_sorted = df.sort_values(date_col)
            
            # Visualisierung
            fig = px.line(df_sorted, x=date_col, y=value_col, title="Zeitreihen-Verlauf")
            st.plotly_chart(fig)
            
            # Vorhersage-Parameter
            col1, col2 = st.columns(2)
            with col1:
                prediction_days = st.slider("Vorhersage für X Tage:", 1, 90, 30)
            with col2:
                confidence_level = st.selectbox("Konfidenz-Level:", ["Niedrig", "Mittel", "Hoch"])
            
            if st.button("Vorhersage generieren"):
                # Datenanalyse für KI
                recent_data = df_sorted.tail(20)
                data_summary = f"""
Letzte 20 Datenpunkte:
{recent_data[[date_col, value_col]].to_string()}

Statistiken:
- Mittelwert: {df[value_col].mean():.2f}
- Standardabweichung: {df[value_col].std():.2f}
- Trend (letzte 5 vs vorherige 5): {recent_data[value_col].tail(5).mean() - recent_data[value_col].head(5).mean():.2f}
- Min: {df[value_col].min():.2f}
- Max: {df[value_col].max():.2f}
"""
                
                prediction_prompt = f"""Analysiere diese Zeitreihen-Daten und gib eine Vorhersage für die nächsten {prediction_days} Tage:

{data_summary}

Aufgaben:
1. Identifiziere Trends und Muster
2. Schätze wahrscheinliche Werte für die nächsten {prediction_days} Tage
3. Erkenne Saisonalität oder Zyklen
4. Bewerte Risiken und Unsicherheiten
5. Gib konkrete Zahlenwerte als Prognose

Konfidenz-Level: {confidence_level}

Format die Antwort als:
- Trend-Analyse
- Vorhersage (numerische Werte)
- Konfidenz-Bewertung
- Einflussfaktoren
- Empfehlungen"""
                
                prediction = ollama.generate(prediction_prompt)
                
                st.subheader(f"Vorhersage für {prediction_days} Tage")
                st.write(prediction)
                
                # Zusätzlich: What-If Szenarien
                st.subheader("What-If Analyse")
                scenario = st.text_input("Beschreibe ein Szenario (z.B. '20% Umsatzsteigerung'):")
                
                if st.button("Szenario analysieren") and scenario:
                    scenario_prompt = f"""Analysiere dieses What-If Szenario basierend auf den historischen Daten:

Historische Daten: {data_summary}
Szenario: {scenario}

Wie würde sich das auf die Vorhersage auswirken? Gib konkrete Zahlen und Wahrscheinlichkeiten."""
                    
                    scenario_result = ollama.generate(scenario_prompt)
                    st.write("**Szenario-Analyse:**", scenario_result)
                    
        except Exception as e:
            st.error(f"Fehler bei der Datenverarbeitung: {e}")
