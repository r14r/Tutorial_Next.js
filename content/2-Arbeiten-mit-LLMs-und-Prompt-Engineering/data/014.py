prompt = "Schreibe eine kurze Geschichte über eine Katze und einen Roboter."

for t in [0.0, 0.7, 1.2]:
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt,
                            "options": {"temperature": t}})
    print(f"Temp={t}:", r.json()["response"])
