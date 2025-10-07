frage = "Wie viele Kunden sind älter als 30?"
antwort = len(df[df["Alter"] > 30])
print(antwort)
