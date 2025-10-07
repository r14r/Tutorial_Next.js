history = [
    {"role": "system", "content": "Du bist ein Tutor."},
    {"role": "user", "content": "Was ist Maschinelles Lernen?"}
]

response = ollama.chat(model="llama2", messages=history)
print(response["message"]["content"])
