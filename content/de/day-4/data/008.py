# Datei: einheit41_llm_integration.py
import pandas as pd
from lib.helper_ollama import ollama

df = pd.read_csv("sales.csv")
stats = df.describe().to_string()
prompt = f"Analysiere die Verkaufsdaten:\n{stats}"
result = ollama.generate(prompt)
print(result)
