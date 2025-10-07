import ollama

# Einfacher Chat
response = ollama.chat(
    model="llama2",
    messages=[{"role": "user", "content": "Erkläre KI in 2 Sätzen"}]
)
print(response["message"]["content"])
