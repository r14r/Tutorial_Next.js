# Datei: einheit42_einfache_abfrage.py
import pandas as pd
df = pd.read_csv("kunden.csv")
frage = "Wie viele Kunden sind älter als 30?"
antwort = len(df[df["Alter"] > 30])
print(antwort)
