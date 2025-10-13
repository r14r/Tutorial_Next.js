# Datei: einheit42_streamlit_app.py
import streamlit as st
import pandas as pd
from lib.helper_ollama import ollama

file = st.file_uploader("CSV hochladen", type="csv")
if file:
    df = pd.read_csv(file)
    frage = st.text_input("Frage:")
    if frage:
        stats = df.describe().to_string()
        prompt = f"{frage}\nDaten:\n{stats}"
        result = ollama.generate(prompt)
        st.write("Antwort:", result)
