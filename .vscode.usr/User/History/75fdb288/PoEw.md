## Einheit 1.2 — Einstieg in Ollama

### 📖 Hintergrund

Ollama ist eine Open-Source-Plattform, die es ermöglicht, große Sprachmodelle lokal auszuführen. Modelle können heruntergeladen werden (`ollama pull`). Man kann mit ihnen über eine API oder die Python-Bibliothek interagieren. Vorteil: Datenschutz (alles läuft lokal), keine API-Kosten, offline nutzbar. Das macht Ollama ideal für schnelles Prototyping von KI-Apps.

### 💻 Code-Beispiele

#### Streamlit-App: Chat mit Ollama

```python
import streamlit as st
import requests

st.title("Chat mit Ollama (lokales LLM)")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("Du:", "")

if st.button("Senden") and user_input:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": user_input}
    )
    reply = response.json()["response"]
    st.session_state['chat_history'].append(("Du", user_input))
    st.session_state['chat_history'].append(("Ollama", reply))

for sender, msg in st.session_state['chat_history']:
    st.write(f"**{sender}:** {msg}")
```

#### API Health Check

```python
import requests

try:
    r = requests.get("http://localhost:11434")
    print("✅ Ollama API läuft!")
except Exception as e:
    print("❌ Verbindung fehlgeschlagen:", e)
```

#### Installationshinweis

```sh
# macOS
brew install ollama

# Modelle laden
ollama pull llama2

# Server starten
ollama serve
```

### 📝 Übungen

1. Installiere Ollama lokal und lade das Modell llama2.
2. Schreibe ein Python-Skript, das „Hallo, KI!“ an Ollama sendet und die Antwort ausgibt.

### ✅ Lösungen

```sh
# Lösung 1: Installation
brew install ollama
ollama pull llama2
ollama serve
```

```python
# Lösung 2: Einfacher Prompt
import requests
prompt = "Hallo, KI!"
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": prompt})
print("Antwort:", r.json()["response"])
```
