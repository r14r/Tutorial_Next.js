# 1. Liste der Modelle
import ollama
response = ollama.list()
print([m["model"] for m in response.models])

# 2. Einfacher CLI-Chat
while True:
    user = input("Du: ")
    if user.lower() == "quit":
        break
    response = ollama.chat(model="llama2",
                           messages=[{"role": "user", "content": user}])
    print("Ollama:", response["message"]["content"])
