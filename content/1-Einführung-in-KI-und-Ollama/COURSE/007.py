r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": "Zähle von 1 bis 5"},
                  stream=True)

for line in r.iter_lines():
    if line:
        print(line.decode(), end="")
