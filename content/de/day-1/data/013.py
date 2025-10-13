response = ollama.chat(
    model="llama2",
    messages=[{"role": "user", "content": "Zähle von 1 bis 5"}],
    stream=True
)

for chunk in response:
    print(chunk["message"]["content"], end="", flush=True)
