messages = [
    {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
    {"role": "user", "content": "Erkläre neuronale Netze kurz."}
]

r = requests.post("http://localhost:11434/api/chat",
                  json={"model": "llama2", "messages": messages})
print(r.json()["message"]["content"])
