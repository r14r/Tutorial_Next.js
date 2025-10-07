for i in range(3):
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": "Rechne 37+45 Schritt für Schritt."})
    print(r.json()["response"])
