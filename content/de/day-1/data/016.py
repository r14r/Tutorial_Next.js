import requests
frage = "Was ist die Hauptstadt von Frankreich?"
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": frage})
print("Antwort:", r.json()["response"])
