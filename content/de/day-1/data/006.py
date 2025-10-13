from lib.helper_ollama import ollama

# Einfacher Prompt mit ollama
result = ollama.generate("Was ist KI?")
print(result)
