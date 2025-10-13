from lib.helper_ollama import ollama

messages = [
    {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
    {"role": "user", "content": "Erkläre neuronale Netze kurz."}
]

result = ollama.chat(messages)
print(result)
