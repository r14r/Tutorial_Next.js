## Einheit 1.5 — Zugriff über die API mit Python (Requests)

### 📖 Hintergrund

Für KI-Apps nutzen wir meistens Python, um die API aufzurufen. Das geht mit der Bibliothek `requests`. Vorteil: JSON einlesen, Fehlerbehandlung möglich, Integration in Streamlit.

### 💻 Beispiele

```python
import requests

# Einfacher Prompt
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": "Was ist KI?"})
print(r.json()["response"])
```

#### Mehrere Nachrichten (Chat)

```python
messages = [
    {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
    {"role": "user", "content": "Erkläre neuronale Netze kurz."}
]

r = requests.post("http://localhost:11434/api/chat",
                  json={"model": "llama2", "messages": messages})
print(r.json()["message"]["content"])
```

#### Streaming von Antworten

```python
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": "Zähle von 1 bis 5"},
                  stream=True)

for line in r.iter_lines():
    if line:
        print(line.decode(), end="")
```

### 📝 Übungen

1. Schreibe ein Python-Skript, das eine Frage an Ollama stellt und die JSON-Antwort ausgibt.
2. Implementiere eine Funktion `chat(prompt)`, die eine Antwort vom Modell zurückgibt.

### ✅ Lösungen

```python
# 1. Einfaches Skript
import requests
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": "Nenne 5 Länder in Europa"})
print(r.json())

# 2. Funktion
def chat(prompt):
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    return r.json()["response"]

print(chat("Was ist Python?"))
```

---
