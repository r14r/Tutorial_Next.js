import requests
stats = df.describe().to_string()
prompt = f"Analysiere die Verkaufsdaten:\n{stats}"
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": prompt})
print(r.json()["response"])
