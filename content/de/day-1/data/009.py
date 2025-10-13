# 1. Einfaches Skript
import requests
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": "Nenne 5 Länder in Europa"})
print(r.json())

# 2. Funktion
def chat(prompt):
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    return r.json()["response"]

print(chat("Was ist Python?"))
