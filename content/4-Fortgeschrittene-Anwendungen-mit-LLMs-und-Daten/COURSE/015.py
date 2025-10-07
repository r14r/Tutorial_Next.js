faq = "Q: Was ist KI? A: Maschinen, die wie Menschen denken."
stats = df.describe().to_string()
prompt = f"""Beantworte die Frage basierend auf diesen Quellen:
FAQ: {faq}
CSV-Daten: {stats}
Frage: Was ist das Durchschnittsalter?"""
