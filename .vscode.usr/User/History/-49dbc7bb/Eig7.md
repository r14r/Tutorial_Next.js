st.title("Chat mit Ollama (lokales LLM)")
---
# � Tag 1 — Einführung in KI & Ollama Grundlagen

## Einheiten-Index

- [Einheit 1.1 — Was ist Künstliche Intelligenz (KI)?](./units/einheit-1-1.md)
- [Einheit 1.2 — Einstieg in Ollama](./units/einheit-1-2.md)
- [Einheit 1.3 — Ollama in der Kommandozeile (CLI)](./units/einheit-1-3.md)
- [Einheit 1.4 — Ollama API mit der Kommandozeile (cURL)](./units/einheit-1-4.md)
- [Einheit 1.5 — Zugriff über die API mit Python (Requests)](./units/einheit-1-5.md)
- [Einheit 1.6 — Nutzung der Ollama SDKs](./units/einheit-1-6.md)
- [Einheit 1.7 — Grundlagen der Arbeit mit LLMs](./units/einheit-1-7.md)
- [Einheit 1.8 — Prompt Engineering Grundlagen](./units/einheit-1-8.md)

### 📖 Hintergrund

Ollama bringt ein eigenes Kommandozeilen-Tool mit. Damit können Modelle heruntergeladen, gelistet und direkt ausgeführt werden – ohne Python.

- `ollama pull <modell>` → Modell herunterladen
- `ollama list` → verfügbare Modelle anzeigen
- `ollama run <modell>` → Modell starten und mit Prompts interagieren

### 💻 Beispiele

- Modell herunterladen
```sh
ollama pull llama2
```

# 2. Alle installierten Modelle anzeigen
```
ollama list
```

# 3. Direkt mit einem Modell chatten
```
ollama run llama2
```

#### Dialog in der CLI

```
>>> Was ist Python?
Python ist eine Programmiersprache, die für ihre Einfachheit und Vielseitigkeit bekannt ist.
```

#### Direkter Prompt von der Shell aus

```sh
echo "Schreibe ein Haiku über KI." | ollama run llama2
```

### 📝 Übungen

1. Lade das Modell mistral herunter.
2. Liste alle Modelle und überprüfe, ob mistral installiert ist.
3. Führe `ollama run mistral` aus und frage nach: „Nenne mir drei Anwendungen von KI.“

### ✅ Lösungen

```sh
ollama pull mistral
ollama list
ollama run mistral
```

Antwortbeispiel:

- Sprachassistenten
- Bildklassifikation
- Betrugserkennung

---

## Einheit 1.4 — Ollama API mit der Kommandozeile (cURL)

### 📖 Hintergrund

Ollama läuft standardmäßig auf Port 11434 und bietet eine REST-API. Mit `curl` lassen sich Requests direkt aus der Shell stellen – ideal zum Testen.

### 💻 Beispiele

```sh
# 1. Gesundheitscheck
curl http://localhost:11434

# 2. Einfacher Chat mit llama2
curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Nenne drei Programmiersprachen"
}'
```

Antwort-Beispiel (JSON):

```json
{"response": "Python, Java, C++"}
```

#### Chat-API Beispiel

```sh
curl http://localhost:11434/api/chat -d '{
  "model": "llama2",
  "messages": [{"role": "user", "content": "Erkläre maschinelles Lernen in einfachen Worten."}]
}'
```

### 📝 Übungen

1. Nutze curl, um eine Liste aller Modelle von der API abzurufen (`/api/tags`).
2. Sende mit curl einen Prompt: „Schreibe ein Gedicht über Programmierer.“

### ✅ Lösungen

```sh
# 1. Modell-Liste
curl http://localhost:11434/api/tags

# 2. Gedicht
curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Schreibe ein Gedicht über Programmierer."
}'
```

---

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

## Einheit 1.7 — Grundlagen der Arbeit mit LLMs

### 📖 Hintergrund

Large Language Models (LLMs) sind KI-Modelle, die auf Milliarden von Texten trainiert wurden. Sie lernen, das nächste Wort in einem Satz vorherzusagen. Dadurch können sie Texte generieren, Fragen beantworten, zusammenfassen. Typische Modelle: GPT-4, Llama-2, Mistral. Ollama ermöglicht, diese Modelle lokal zu nutzen. Einsatz in KI-Apps: Chatbots, Textzusammenfassungen, Code-Helfer.

### 💻 Code-Beispiele

#### Text-Zusammenfasser mit Ollama

```python
import streamlit as st
import requests

st.title("Dokument-Zusammenfassung mit Ollama")
file = st.file_uploader("Textdatei hochladen", type=["txt"])

if file:
    text = file.read().decode()
    prompt = f"Fasse den folgenden Text in 5 Sätzen zusammen:\n\n{text}"
    response = requests.post("http://localhost:11434/api/generate",
                             json={"model": "llama2", "prompt": prompt})
    summary = response.json()["response"]
    st.subheader("Zusammenfassung")
    st.write(summary)
```

### 📝 Übungen

1. Erkläre, warum LLMs nicht immer richtige Antworten geben (Halluzinationen).
2. Schreibe ein Skript, das eine Frage an Ollama stellt und die Antwort ausgibt.

### ✅ Lösungen

- LLMs basieren auf Wahrscheinlichkeiten und erfinden manchmal plausible, aber falsche Inhalte → „Halluzinationen“.

```python
import requests
frage = "Was ist die Hauptstadt von Frankreich?"
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": frage})
print("Antwort:", r.json()["response"])
```

---

## Einheit 1.8 — Prompt Engineering Grundlagen

### 📖 Hintergrund

Prompt Engineering = die Kunst, gute Eingaben für ein Sprachmodell zu formulieren. Unterschiedliche Formulierungen führen zu anderen Ergebnissen. Ein guter Prompt enthält:

- klare Anweisung
- Kontext
- gewünschtes Format

Beispiel: „Fasse den Text zusammen“ vs. „Fasse den Text in 3 Bullet Points zusammen“.

### 💻 Code-Beispiele

#### Prompt Playground in Streamlit

```python
import streamlit as st
import requests

st.title("Prompt Playground")
prompt = st.text_area("Prompt eingeben", height=150)

if st.button("Abschicken") and prompt:
    response = requests.post("http://localhost:11434/api/generate",
                             json={"model": "llama2", "prompt": prompt})
    st.subheader("Antwort")
    st.write(response.json()["response"])
```

### 📝 Übungen

1. Erstelle drei verschiedene Prompts, die denselben Text zusammenfassen, aber mit unterschiedlichem Stil (kurz, ausführlich, Bulletpoints).
2. Teste mit Ollama, wie sich die Ergebnisse unterscheiden.

### ✅ Lösungen

- Prompt 1: „Fasse diesen Artikel in 1 Satz zusammen.“
- Prompt 2: „Schreibe eine detaillierte Zusammenfassung in 5 Sätzen.“
- Prompt 3: „Fasse den Artikel in Bulletpoints zusammen.“

---

## 🎯 Zusammenfassung Tag 1 (erweitert)

Nach diesem Tag können die Studierenden:

- erklären, was KI, ML und LLMs sind,
- Ollama lokal installieren und erste Modelle nutzen,
- Ollama über die CLI bedienen (`pull`, `list`, `run`),
- Ollama über die REST-API mit `curl` ansprechen,
- Ollama in Python-Apps mit `requests` einbinden,
- Ollama komfortabel über das SDK nutzen (inkl. Streaming),
- einfache KI-Apps mit Streamlit und Ollama bauen,
- Prompts gezielt formulieren, um bessere Ergebnisse zu erhalten.
