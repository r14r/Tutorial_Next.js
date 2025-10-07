def extract_keywords(text):
    prompt = f"Extrahiere Keywords als Liste: {text}"
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    return r.json()["response"]

print(extract_keywords("Microsoft investiert Milliarden in KI."))
