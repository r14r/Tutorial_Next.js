import streamlit as st
import pandas as pd
from lib.helper_ollama import ollama

st.title("Competitive Content Analysis")
st.write("Analysiere Inhalte von bis zu 3 Konkurrenten")

konkurrenten = []
for i in range(3):
    name = st.text_input(f"Konkurrent {i+1} Name:")
    content = st.text_area(f"Content von {name if name else f'Konkurrent {i+1}'}:")
    if name and content:
        konkurrenten.append({"Name": name, "Content": content})

if st.button("Analysieren") and konkurrenten:
    ergebnisse = []
    
    for k in konkurrenten:
        prompt = f"""Analysiere den folgenden Marketing-Content:
1. Hauptbotschaft
2. Zielgruppe
3. Tonalität/Stil
4. Stärken
5. Verbesserungsvorschläge

Content: {k['Content']}"""
        
        analyse = ollama.generate(prompt)
        ergebnisse.append({
            "Konkurrent": k["Name"],
            "Analyse": analyse
        })
    
    # Vergleichstabelle
    df = pd.DataFrame(ergebnisse)
    st.dataframe(df)
    
    # Strategische Empfehlungen
    if st.button("Strategische Empfehlungen"):
        alle_analysen = "\n\n".join([f"{e['Konkurrent']}: {e['Analyse']}" for e in ergebnisse])
        strategie_prompt = f"Basierend auf diesen Konkurrenzanalysen, gib strategische Empfehlungen für die eigene Content-Strategie:\n{alle_analysen}"
        empfehlungen = ollama.generate(strategie_prompt)
        st.write("**Strategische Empfehlungen:**", empfehlungen)
