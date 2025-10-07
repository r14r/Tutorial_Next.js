doc = open("info.txt").read()
prompt = f"""Verwende CSV + Dokument:
CSV: {df.describe().to_string()}
Dokument: {doc}
Frage: Welche Erkenntnisse gibt es?"""
