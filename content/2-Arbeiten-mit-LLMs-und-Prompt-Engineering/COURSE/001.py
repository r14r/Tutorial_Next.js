import requests

prompt = "Erkläre Maschinelles Lernen in einfachen Worten."
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": prompt})
print(r.json()["response"])
