faq = open("faq.txt").read()
stats = df.describe().to_string()
frage = "Welche Stadt hat den höchsten Umsatz und wie passt das zu den FAQ-Daten?"

prompt = f"""FAQ: {faq}
CSV: {stats}
Frage: {frage}"""
