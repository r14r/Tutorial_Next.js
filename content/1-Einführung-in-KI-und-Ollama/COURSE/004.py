# Lösung 2: Einfacher Prompt
import requests
prompt = "Hallo, KI!"
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": prompt})
print("Antwort:", r.json()["response"])
