p1 = "Fasse den Text kurz zusammen."
p2 = "Erstelle eine ausführliche Zusammenfassung in 5 Sätzen."

for p in [p1, p2]:
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": p})
    print("Prompt:", p)
    print("Antwort:", r.json()["response"])
