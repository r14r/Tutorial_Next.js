response = ollama.list()
for m in response.models:
    print("Modell:", m["model"])
