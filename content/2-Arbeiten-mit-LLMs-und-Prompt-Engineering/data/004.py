messages = [
    {"role": "system", "content": "Du bist ein freundlicher Lehrer."},
    {"role": "user", "content": "Erkläre neuronale Netze in einfachen Worten."}
]

r = requests.post("http://localhost:11434/api/chat",
                  json={"model": "llama2", "messages": messages})
print(r.json()["message"]["content"])
