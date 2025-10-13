# Datei: einheit43_llm_kommentar.py
import pandas as pd
from lib.helper_ollama import ollama

df = pd.read_csv("sales.csv")
stats = df.describe().to_string()
prompt = f"Erkläre die wichtigsten Trends:\n{stats}"
result = ollama.generate(prompt)
print(result)
