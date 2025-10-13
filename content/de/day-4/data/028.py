# Datei: einheit45_csv_text.py
import pandas as pd
from lib.helper_ollama import ollama

df = pd.read_csv("kunden.csv")
doc = open("info.txt").read()
prompt = f"Verwende CSV + Dokument:\nCSV: {df.describe().to_string()}\nDokument: {doc}\nFrage: Welche Erkenntnisse gibt es?"
result = ollama.generate(prompt)
print(result)
