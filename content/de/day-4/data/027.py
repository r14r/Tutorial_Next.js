# Datei: einheit45_csv_faq.py
import pandas as pd
from lib.helper_ollama import ollama

df = pd.read_csv("kunden.csv")
faq = "Q: Was ist KI? A: Maschinen, die wie Menschen denken."
stats = df.describe().to_string()
prompt = f"Beantworte die Frage basierend auf diesen Quellen:\nFAQ: {faq}\nCSV-Daten: {stats}\nFrage: Was ist das Durchschnittsalter?"
result = ollama.generate(prompt)
print(result)
