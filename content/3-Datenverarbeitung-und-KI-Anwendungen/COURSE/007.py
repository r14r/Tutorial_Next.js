texts = [
    "Die Aktie von Tesla stieg um 5%.",
    "Lionel Messi schoss 2 Tore.",
    "Das Parlament diskutierte ein neues Gesetz."
]

for t in texts:
    prompt = f"Welches Thema? {t}"
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    print(t, "→", r.json()["response"])
