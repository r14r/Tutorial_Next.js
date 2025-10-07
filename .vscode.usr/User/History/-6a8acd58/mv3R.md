## Einheit 1.6 — Nutzung der Ollama SDKs

### 📖 Hintergrund

Neben der API bietet Ollama SDKs (z. B. für Python oder Node.js). Diese vereinfachen die Kommunikation und bieten oft komfortablere Methoden als reine HTTP-Requests.

### 💻 Beispiele

#### Python SDK

```python
import ollama

# Einfacher Chat
response = ollama.chat(
    model="llama2",
    messages=[{"role": "user", "content": "Erkläre KI in 2 Sätzen"}]
)
print(response["message"]["content"])
```

#### Mehrere Nachrichten

```python
history = [
    {"role": "system", "content": "Du bist ein Tutor."},
    {"role": "user", "content": "Was ist Maschinelles Lernen?"}
]

response = ollama.chat(model="llama2", messages=history)
print(response["message"]["content"])
```

#### Liste der Modelle

```python
response = ollama.list()
for m in response.models:
    print("Modell:", m["model"])
```

#### Streaming im SDK

```python
response = ollama.chat(
    model="llama2",
    messages=[{"role": "user", "content": "Zähle von 1 bis 5"}],
    stream=True
)

for chunk in response:
    print(chunk["message"]["content"], end="", flush=True)
```

### 📝 Übungen

1. Nutze das SDK, um eine Liste aller installierten Modelle auszugeben.
2. Schreibe ein kleines Chat-Skript, das eine Unterhaltung in einer Schleife ermöglicht.

### ✅ Lösungen

```python
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
```

---
