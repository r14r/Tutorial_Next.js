# upload-ollama.py
import pandas as pd
import streamlit as st
from lib.helper_ollama import ollama

st.title("CSV-Upload & KI-Zusammenfassung")
file = st.file_uploader("CSV hochladen", type="csv")
if file:
    df = pd.read_csv(file)
    st.dataframe(df)
    stats = df.describe().to_string()
    prompt = f"Fasse die wichtigsten Erkenntnisse aus diesen Daten zusammen:\n{stats}"
    result = ollama.generate(prompt)
    st.write(result)
