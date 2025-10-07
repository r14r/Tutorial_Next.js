# 1. Funktion
def classify(text, labels):
    prompt = f"Klassifiziere den Text '{text}' in eine dieser Kategorien: {', '.join(labels)}"
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    return r.json()["response"]

print(classify("Messi schoss ein Tor.", ["Sport", "Politik", "Technologie"]))

# 3. CSV-App
import pandas as pd
import streamlit as st

file = st.file_uploader("Nachrichten CSV", type="csv")
if file:
    df = pd.read_csv(file)
    for row in df["Text"]:
        st.write(row, "→", classify(row, ["Sport", "Politik", "Technologie"]))
