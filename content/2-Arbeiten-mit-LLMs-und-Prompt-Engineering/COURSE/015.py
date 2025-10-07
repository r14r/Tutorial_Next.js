import requests

models = ["llama2", "mistral"]
prompt = "Erkläre den Unterschied zwischen Python und Java."

for m in models:
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": m, "prompt": prompt})
    print(m, ":", r.json()["response"])
