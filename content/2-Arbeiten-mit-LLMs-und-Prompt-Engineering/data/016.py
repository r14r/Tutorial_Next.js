prompt = "Was ist die Hauptstadt von Frankreich in Afrika?"
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": prompt})
print(r.json()["response"])
# → Beispiel für Halluzination
