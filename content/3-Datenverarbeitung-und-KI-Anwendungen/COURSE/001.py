import requests

text = "Ich liebe dieses neue Produkt, es ist fantastisch!"
prompt = f"Analysiere die Stimmung: {text}"

r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": prompt})
print(r.json()["response"])
