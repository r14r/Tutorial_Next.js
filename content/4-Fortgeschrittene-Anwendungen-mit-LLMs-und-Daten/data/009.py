# Anzahl Städte
print(df["Stadt"].nunique())

# Funktion
def answer_question(df, frage):
    stats = df.describe().to_string()
    prompt = f"Frage: {frage}\nDaten:\n{stats}"
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    return r.json()["response"]

print(answer_question(df, "Was ist der Durchschnitt des Alters?"))

# Pandas-Lösung
print(df.loc[df["Einkommen"].idxmax()])
