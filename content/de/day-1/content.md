# 📘 Tag 1 — Einführung in KI & Ollama Grundlagen

## 📅 Zeitplan 09:00 – 15:00

### Übersicht

Der Tag bietet einen praxisnahen Einstieg in Künstliche Intelligenz und die Arbeit mit Ollama. Jede Einheit besteht aus einer kurzen Erklärung, gefolgt von Beispielen und praktischen Übungen.

---

### Zeitplan

| Zeit            | Einheit / Inhalt                                                                 | Dauer   |
|-----------------|----------------------------------------------------------------------------------|---------|
| **09:00 – 09:20** | Einführung & Überblick über KI, ML, LLMs - Motivation, Ziele des Tages | 20 min  |
| **09:20 – 09:50** | **Einheit 1.1:** Was ist Künstliche Intelligenz? - Begriff, Beispiele, Übungen | 30 min  |
| **09:50 – 10:20** | **Einheit 1.2:** Einstieg in Ollama - Installation, erster Test, Übungen | 30 min  |
| **10:20 – 10:50** | **Einheit 1.3:** Ollama in der Kommandozeile - CLI-Befehle, Dialog, Übungen | 30 min  |
| **10:50 – 11:05** | ☕ **Pause**                                                                    | 15 min  |
| **11:05 – 11:35** | **Einheit 1.4:** Ollama API mit cURL - REST-API, Requests, Übungen | 30 min  |
| **11:35 – 12:05** | **Einheit 1.5:** Zugriff über die API mit Python - Requests, Chat, Übungen | 30 min  |
| **12:05 – 12:35** | **Einheit 1.6:** Nutzung der Ollama SDKs - Python SDK, Streaming, Übungen | 30 min  |
| **12:35 – 13:35** | 🍽️ **Mittagspause**                                                            | 60 min  |
| **13:35 – 14:05** | **Einheit 1.7:** Grundlagen der Arbeit mit LLMs - Funktionsweise, Zusammenfassung, Übungen | 30 min  |
| **14:05 – 14:35** | **Einheit 1.8:** Prompt Engineering Grundlagen - Prompts, Playground, Übungen | 30 min  |
| **14:35 – 15:00** | **Zusammenfassung & Mini-Projekt** - Kleine KI-App mit Ollama und Streamlit | 25 min  |

---

## Ablauf der Einheiten

- **Erklärung:** ca. 10–15 min
- **Beispiele:** ca. 10 min
- **Übungen:** ca. 10–15 min  
    → Übungen werden direkt in Jupyter, VS Code oder Streamlit durchgeführt.

---

## Mini-Projekt (14:35–15:00)

Am Ende des Tages wird eine kleine KI-App entwickelt, die folgende Funktionen kombiniert:

- **Eingabe:** Textfeld für Prompts
- **Verarbeitung:** Anfrage an Ollama (lokales LLM)
- **Ausgabe:** Antwort anzeigen und ggf. zusammenfassen

---

## Einheit 1 — Was ist Künstliche Intelligenz (KI)?

### 📖 Hintergrund

Künstliche Intelligenz (KI) ist der Bereich der Informatik, der Systeme entwickelt, die Aufgaben ausführen können, die normalerweise menschliche Intelligenz erfordern. Dazu gehören:

- Problemlösen (z. B. Schach spielen)
- Sprachverstehen (z. B. Chatbots)
- Mustererkennung (z. B. Gesichtserkennung)
- Entscheidungen treffen (z. B. Empfehlungssysteme)

Eine wichtige Unterdisziplin ist das Maschinelle Lernen (ML). Dabei lernen Systeme nicht durch feste Regeln, sondern aus Daten. Moderne KI basiert auf Neuronalen Netzen (Deep Learning). Besonders wichtig sind Large Language Models (LLMs) wie GPT, Llama oder Mistral, die auf großen Textmengen trainiert wurden und Sprache verarbeiten können.

### 💻 Code-Beispiele

```python
# KI-Begriff einfach erklärt
print("KI = Maschinen, die wie Menschen denken und handeln können.")
print("ML = Maschinen, die aus Daten lernen.")
```

#### KI-Anwendungen demonstrieren mit ollama

```python
import streamlit as st
from lib.helper_ollama import ollama

st.title("KI-Anwendungen Demo")
anwendung = st.selectbox("Wähle eine KI-Anwendung:", 
                        ["Textgenerierung", "Übersetzung", "Zusammenfassung"])

if anwendung == "Textgenerierung":
    prompt = "Schreibe ein kurzes Gedicht über Künstliche Intelligenz"
elif anwendung == "Übersetzung":
    prompt = "Übersetze 'Hello World' ins Deutsche"
else:
    prompt = "Erkläre Maschinelles Lernen in einem Satz"

if st.button("KI ausführen"):
    result = ollama.generate(prompt)
    st.write("KI-Antwort:", result)
```

### 📝 Übungen

1. Nenne drei reale Anwendungen von KI im Alltag.
2. Erkläre den Unterschied zwischen KI und ML.

### ✅ Lösungen

- Sprachassistenten (Siri, Alexa), Empfehlungssysteme (Netflix, Amazon), selbstfahrende Autos.
- KI = Überbegriff; ML = Untergebiet, das Lernen aus Daten ermöglicht.

---

## Einheit 2 — Einstieg in Ollama

### 📖 Hintergrund

Ollama ist eine Open-Source-Plattform, die es ermöglicht, große Sprachmodelle lokal auszuführen. Modelle können heruntergeladen werden (`ollama pull`). Man kann mit ihnen über eine API oder die Python-Bibliothek interagieren. Vorteil: Datenschutz (alles läuft lokal), keine API-Kosten, offline nutzbar. Das macht Ollama ideal für schnelles Prototyping von KI-Apps.

### 💻 Code-Beispiele

#### Streamlit-App: Chat mit Ollama (mit ollama)

```python
import streamlit as st
from lib.helper_ollama import ollama

st.title("Chat mit Ollama (lokales LLM)")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("Du:", "")

if st.button("Senden") and user_input:
    reply = ollama.generate(user_input)
    st.session_state['chat_history'].append(("Du", user_input))
    st.session_state['chat_history'].append(("Ollama", reply))

for sender, msg in st.session_state['chat_history']:
    st.write(f"**{sender}:** {msg}")
```

#### API Health Check mit ollama

```python
from lib.helper_ollama import ollama

try:
    result = ollama.generate("Test")
    print("✅ Ollama API läuft!", result[:50])
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

---

## Einheit 3 — Ollama in der Kommandozeile (CLI)

### 📖 Hintergrund

Ollama bringt ein eigenes Kommandozeilen-Tool mit. Damit können Modelle heruntergeladen, gelistet und direkt ausgeführt werden – ohne Python.

- `ollama pull <modell>` → Modell herunterladen
- `ollama list` → verfügbare Modelle anzeigen
- `ollama run <modell>` → Modell starten und mit Prompts interagieren

### 💻 Beispiele

```sh
# 1. Modell herunterladen
ollama pull llama2

# 2. Alle installierten Modelle anzeigen
ollama list

# 3. Direkt mit einem Modell chatten
ollama run llama2
```

#### Dialog in der CLI

```shell
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

## Einheit 4 — Ollama API mit der Kommandozeile (cURL)

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

## Einheit 5 — Zugriff über die API mit Python (Requests)

### 📖 Hintergrund

Für KI-Apps nutzen wir meistens Python, um die API aufzurufen. Das geht mit der Bibliothek `requests`. Vorteil: JSON einlesen, Fehlerbehandlung möglich, Integration in Streamlit.

### 💻 Beispiele

```python
from lib.helper_ollama import ollama

# Einfacher Prompt mit ollama
result = ollama.generate("Was ist KI?")
print(result)
```

#### Mehrere Nachrichten (Chat) mit ollama

```python
from lib.helper_ollama import ollama

messages = [
    {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
    {"role": "user", "content": "Erkläre neuronale Netze kurz."}
]

result = ollama.chat(messages)
print(result)
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

## Einheit 6 — Nutzung der Ollama SDKs

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

## Einheit 7 — Grundlagen der Arbeit mit LLMs

### 📖 Hintergrund

Large Language Models (LLMs) sind KI-Modelle, die auf Milliarden von Texten trainiert wurden. Sie lernen, das nächste Wort in einem Satz vorherzusagen. Dadurch können sie Texte generieren, Fragen beantworten, zusammenfassen. Typische Modelle: GPT-4, Llama-2, Mistral. Ollama ermöglicht, diese Modelle lokal zu nutzen. Einsatz in KI-Apps: Chatbots, Textzusammenfassungen, Code-Helfer.

### 💻 Code-Beispiele

#### Text-Zusammenfasser mit ollama

```python
import streamlit as st
from lib.helper_ollama import ollama

st.title("Dokument-Zusammenfassung mit Ollama")
file = st.file_uploader("Textdatei hochladen", type=["txt"])

if file:
    text = file.read().decode()
    prompt = f"Fasse den folgenden Text in 5 Sätzen zusammen:\n\n{text}"
    summary = ollama.generate(prompt)
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

## Einheit 8 — Prompt Engineering Grundlagen

### 📖 Hintergrund

Prompt Engineering = die Kunst, gute Eingaben für ein Sprachmodell zu formulieren. Unterschiedliche Formulierungen führen zu anderen Ergebnissen. Ein guter Prompt enthält:

- klare Anweisung
- Kontext
- gewünschtes Format

Beispiel: „Fasse den Text zusammen“ vs. „Fasse den Text in 3 Bullet Points zusammen“.

### 💻 Code-Beispiele

#### Prompt Playground mit ollama

```python
import streamlit as st
from lib.helper_ollama import ollama

st.title("Prompt Playground")
prompt = st.text_area("Prompt eingeben", height=150)

if st.button("Abschicken") and prompt:
    result = ollama.generate(prompt)
    st.subheader("Antwort")
    st.write(result)
```

### 📝 Übungen

1. Erstelle drei verschiedene Prompts, die denselben Text zusammenfassen, aber mit unterschiedlichem Stil (kurz, ausführlich, Bulletpoints).
2. Teste mit Ollama, wie sich die Ergebnisse unterscheiden.

### ✅ Lösungen

- Prompt 1: „Fasse diesen Artikel in 1 Satz zusammen.“
- Prompt 2: „Schreibe eine detaillierte Zusammenfassung in 5 Sätzen.“
- Prompt 3: „Fasse den Artikel in Bulletpoints zusammen.“

---

## Einheit 9 — Zusammenfassung

Nach diesem Tag können die Studierenden:

- erklären, was KI, ML und LLMs sind,
- Ollama lokal installieren und erste Modelle nutzen,
- Ollama über die CLI bedienen (`pull`, `list`, `run`),
- Ollama über die REST-API mit `curl` ansprechen,
- Ollama in Python-Apps mit `requests` einbinden,
- Ollama komfortabel über das SDK nutzen (inkl. Streaming),
- einfache KI-Apps mit Streamlit und Ollama bauen,
- Prompts gezielt formulieren, um bessere Ergebnisse zu erhalten.

---

## Einheit 10 — Mini-Projekte

### Mini-Projekt 1: KI-Chatbot mit Persönlichkeit

**Aufgabe:** Baue einen Chatbot, der sich wie ein freundlicher Tutor verhält.

**Lösung:**

```python
## miniapp-01
import streamlit as st
from lib.helper_ollama import ollama

st.title("KI-Tutor Chatbot")
if 'chat' not in st.session_state:
    st.session_state.chat = []
    
user_input = st.text_input("Frage den KI-Tutor:")
if st.button("Senden") and user_input:
    messages = [
        {"role": "system", "content": "Du bist ein freundlicher, geduldiger Tutor."},
        {"role": "user", "content": user_input}
    ]
    antwort = ollama.chat(messages)
    st.session_state.chat.append(("Du", user_input))
    st.session_state.chat.append(("Tutor", antwort))
    
for sprecher, text in st.session_state.chat:
    st.write(f"**{sprecher}:** {text}")
```

### Mini-Projekt 2: Textklassifikation (Sentiment-Analyse)

**Aufgabe:** Klassifiziere Texte als positiv, neutral oder negativ.

**Lösung:**

```python
## miniapp-02
import streamlit as st
from lib.helper_ollama import ollama

st.title("Sentiment-Analyse mit KI")
text = st.text_area("Text eingeben")
if st.button("Analysieren") and text:
    prompt = f"Klassifiziere den Sentiment des folgenden Textes als 'positiv', 'neutral' oder 'negativ': {text}"
    result = ollama.generate(prompt)
    
    if "positiv" in result.lower():
        st.success(f"Positiv: {result}")
    elif "negativ" in result.lower():
        st.error(f"Negativ: {result}")
    else:
        st.info(f"Neutral: {result}")
```

### Mini-Projekt 3: Kreativer Textgenerator

**Aufgabe:** Generiere kreative Texte basierend auf einem Thema und Stil.

**Lösung:**

```python
## miniapp-03
import streamlit as st
from lib.helper_ollama import ollama

st.title("Kreativer Textgenerator")
thema = st.text_input("Thema eingeben")
stil = st.selectbox("Stil wählen", ["Gedicht", "Kurzgeschichte", "Haiku", "Limerick"])

if st.button("Generieren") and thema:
    prompt = f"Schreibe ein {stil} über das Thema '{thema}'"
    result = ollama.generate(prompt)
    st.write("**Generierter Text:**")
    st.write(result)
```

### Mini-Projekt 4: FAQ-Bot mit Wissensbasis

**Aufgabe:** Lade eine FAQ-Datei hoch und beantworte Fragen dazu.

**Lösung:**

```python
## miniapp-04
import streamlit as st
from lib.helper_ollama import ollama

st.title("FAQ-Bot")
faq_file = st.file_uploader("FAQ-Datei hochladen (txt)", type="txt")
frage = st.text_input("Stelle eine Frage")

if faq_file and frage:
    faq_content = faq_file.read().decode()
    prompt = f"Beantworte die folgende Frage basierend auf dieser FAQ:\n\nFAQ:\n{faq_content}\n\nFrage: {frage}"
    
    if st.button("Antworten"):
        antwort = ollama.generate(prompt)
        st.write("**Antwort:**", antwort)
```

### Mini-Projekt 5: Sprachübersetzer

**Aufgabe:** Übersetze Texte zwischen verschiedenen Sprachen.

**Lösung:**

```python
## miniapp-05
import streamlit as st
from lib.helper_ollama import ollama

st.title("KI-Sprachübersetzer")
text = st.text_area("Text zum Übersetzen")
von_sprache = st.selectbox("Von Sprache", ["Deutsch", "Englisch", "Französisch", "Spanisch"])
zu_sprache = st.selectbox("Zu Sprache", ["Englisch", "Deutsch", "Französisch", "Spanisch"])

if st.button("Übersetzen") and text and von_sprache != zu_sprache:
    prompt = f"Übersetze den folgenden Text von {von_sprache} zu {zu_sprache}: {text}"
    result = ollama.generate(prompt)
    st.write("**Übersetzung:**")
    st.write(result)
```
