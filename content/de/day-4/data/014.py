# Datei: einheit42_llm_antwort.py
import pandas as pd
from lib.helper_ollama import ollama

df = pd.read_csv("kunden.csv")
stats = df.describe().to_string()
prompt = f"Beantworte die Frage basierend auf diesen Daten:\n{stats}\nFrage: Wie viele Kunden sind älter als 30?"
result = ollama.generate(prompt)
print(result)
