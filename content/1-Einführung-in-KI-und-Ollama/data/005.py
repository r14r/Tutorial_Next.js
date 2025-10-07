import requests

# Einfacher Prompt
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": "Was ist KI?"})
print(r.json()["response"])
