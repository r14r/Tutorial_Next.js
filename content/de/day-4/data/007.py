# Datei: einheit41_filterung.py
import pandas as pd
df = pd.read_csv("sales.csv")
kunden = df[df["Country"] == "Germany"]
print(kunden)
