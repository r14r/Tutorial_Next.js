def analyze(text):
    prompt = """Analysiere den Text:
1. Stimmung
2. Keywords
3. Named Entities"""
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    return r.json()["response"]
