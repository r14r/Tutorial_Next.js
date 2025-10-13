# 📘 Day 1 — Introduction to AI & Ollama basics

## 📅 ​​Schedule 09:00 - 15:00

### Overview

The day offers a practical introduction to artificial intelligence and working with Ollama. Each unit consists of a short explanation followed by examples and practical exercises.

---

### Schedule

| time | Unit / Content | Duration |
|-----------------|---------------------------------------------------------------------------------|---------|
| **09:00 – 09:20** | Introduction & Overview of AI, ML, LLMs - Motivation, Goals of the Day | 20 mins |
| **09:20 – 09:50** | **Unit 1.1:** What is Artificial Intelligence? - Concept, examples, exercises | 30 mins |
| **09:50 – 10:20** | **Unit 1.2:** Getting started with Ollama - installation, first test, exercises | 30 mins |
| **10:20 – 10:50** | **Unit 1.3:** Ollama in the command line - CLI commands, dialog, exercises | 30 mins |
| **10:50 – 11:05** | ☕ **Break** | 15 mins |
| **11:05 – 11:35** | **Unit 1.4:** Ollama API with cURL - REST API, requests, exercises | 30 mins |
| **11:35 – 12:05** | **Unit 1.5:** Access via the API with Python - Requests, Chat, Exercises | 30 mins |
| **12:05 – 12:35** | **Unit 1.6:** Using the Ollama SDKs - Python SDK, streaming, exercises | 30 mins |
| **12:35 – 1:35 pm** | 🍽️ **Lunch break** | 60 mins |
| **1:35 p.m. – 2:05 p.m.** | **Unit 1.7:** Basics of working with LLMs - how they work, summary, exercises | 30 mins |
| **14:05 – 14:35** | **Unit 1.8:** Prompt Engineering Basics - Prompts, Playground, Exercises | 30 mins |
| **14:35 – 15:00** | **Summary & Mini Project** - Small AI app with Ollama and Streamlit | 25 mins |

---

## Unit expiry

- **Explanation:** approx. 10-15 min
- **Examples:** approx. 10 min
- **Exercises:** approx. 10-15 min  
    → Exercises are carried out directly in Jupyter, VS Code or Streamlit.

---

## Mini Project (2:35 p.m. - 3:00 p.m.)

At the end of the day, a small AI app is developed that combines the following functions:

- **Input:** Text field for prompts
- **Processing:** Request to Ollama (local LLM)
- **Output:** Show answer and summarize if necessary

---

## Unit 1 — What is Artificial Intelligence (AI)?

### 📖 Background

Artificial intelligence (AI) is the field of computer science that develops systems that can perform tasks that normally require human intelligence. This includes:

- Problem solving (e.g. playing chess)
- Language understanding (e.g. chatbots)
- Pattern recognition (e.g. face recognition)
- Make decisions (e.g. recommendation systems)

An important sub-discipline is machine learning (ML). Systems do not learn through fixed rules, but rather from data. Modern AI is based on neural networks (deep learning). Particularly important are Large Language Models (LLMs) such as GPT, Llama or Mistral, which were trained on large amounts of text and can process language.

### 💻 Code examples

```python
# KI-Begriff einfach erklärt
print("KI = Maschinen, die wie Menschen denken und handeln können.")
print("ML = Maschinen, die aus Daten lernen.")
```
#### Demonstrate AI applications with ollama

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
### 📝 Exercises

1. Name three real-world applications of AI in everyday life.
2. Explain the difference between AI and ML.

### ✅ Solutions

- Voice assistants (Siri, Alexa), recommendation systems (Netflix, Amazon), self-driving cars.
- AI = umbrella term; ML = subfield that enables learning from data.

---

## Unit 2 — Getting into Ollama

### 📖 Background

Ollama is an open source platform that allows large language models to be run locally. Models can be downloaded (`ollama pull`). You can interact with them via an API or the Python library. Advantage: Data protection (everything runs locally), no API costs, can be used offline. This makes Ollama ideal for rapid prototyping of AI apps.

### 💻 Code examples

#### Streamlit app: Chat with Ollama (with ollama)

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
#### API Health Check with ollama

```python
from lib.helper_ollama import ollama

try:
    result = ollama.generate("Test")
    print("✅ Ollama API läuft!", result[:50])
except Exception as e:
    print("❌ Verbindung fehlgeschlagen:", e)
```
#### Installation notice

```sh
# macOS
brew install ollama

# Modelle laden
ollama pull llama2

# Server starten
ollama serve
```
### 📝 Exercises

1. Install Ollama locally and load the llama2 model.
2. Write a Python script that says “Hello, AI!” to Ollama and outputs the response.

### ✅ Solutions

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

## Unit 3 — Ollama in the command line (CLI)

### 📖 Background

Ollama comes with its own command line tool. This allows models to be downloaded, listed and executed directly - without Python.

- `ollama pull <model>` → Download model
- `ollama list` → show available models
- `ollama run <model>` → Start model and interact with prompts

### 💻 Examples

```sh
# 1. Modell herunterladen
ollama pull llama2

# 2. Alle installierten Modelle anzeigen
ollama list

# 3. Direkt mit einem Modell chatten
ollama run llama2
```
#### Dialog in the CLI

```shell
>>> Was ist Python?
Python ist eine Programmiersprache, die für ihre Einfachheit und Vielseitigkeit bekannt ist.
```
#### Direct prompt from the shell

```sh
echo "Schreibe ein Haiku über KI." | ollama run llama2
```
### 📝 Exercises

1. Download the mistral model.
2. List all models and check if mistral is installed.
3. Run 'ollama run mistral' and ask: "Tell me three applications of AI."

### ✅ Solutions

```sh
ollama pull mistral
ollama list
ollama run mistral
```
Answer example:

- Voice assistants
- Image classification
- Fraud detection

---

## Unit 4 — Ollama API with the command line (cURL)

### 📖 Background

Ollama runs on port 11434 by default and offers a REST API. With `curl` you can make requests directly from the shell - ideal for testing.

### 💻 Examples

```sh
# 1. Gesundheitscheck
curl http://localhost:11434

# 2. Einfacher Chat mit llama2
curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Nenne drei Programmiersprachen"
}'
```
Response example (JSON):

```json
{"response": "Python, Java, C++"}
```
#### Chat API example

```sh
curl http://localhost:11434/api/chat -d '{
  "model": "llama2",
  "messages": [{"role": "user", "content": "Erkläre maschinelles Lernen in einfachen Worten."}]
}'
```
### 📝 Exercises

1. Use curl to get a list of all models from the API (`/api/tags`).
2. Use curl to send a prompt: “Write a poem about programmers.”

### ✅ Solutions

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

## Unit 5 — Access via the API with Python (Requests)

### 📖 Background

For AI apps, we mostly use Python to call the API. This can be done with the `requests` library. Advantage: Read JSON, error handling possible, integration into Streamlit.

### 💻 Examples

```python
from lib.helper_ollama import ollama

# Einfacher Prompt mit ollama
result = ollama.generate("Was ist KI?")
print(result)
```
#### Multiple messages (chat) with ollama

```python
from lib.helper_ollama import ollama

messages = [
    {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
    {"role": "user", "content": "Erkläre neuronale Netze kurz."}
]

result = ollama.chat(messages)
print(result)
```
#### Streaming answers

```python
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": "Zähle von 1 bis 5"},
                  stream=True)

for line in r.iter_lines():
    if line:
        print(line.decode(), end="")
```
### 📝 Exercises

1. Write a Python script that asks Ollama a question and outputs the JSON answer.
2. Implement a function `chat(prompt)` that returns a response from the model.

### ✅ Solutions

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

## Unit 6 — Using the Ollama SDKs

### 📖 Background

In addition to the API, Ollama offers SDKs (e.g. for Python or Node.js). These simplify communication and often offer more convenient methods than pure HTTP requests.

### 💻 Examples

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
#### Multiple messages

```python
history = [
    {"role": "system", "content": "Du bist ein Tutor."},
    {"role": "user", "content": "Was ist Maschinelles Lernen?"}
]

response = ollama.chat(model="llama2", messages=history)
print(response["message"]["content"])
```
#### List of models

```python
response = ollama.list()
for m in response.models:
    print("Modell:", m["model"])
```
#### Streaming in SDK

```python
response = ollama.chat(
    model="llama2",
    messages=[{"role": "user", "content": "Zähle von 1 bis 5"}],
    stream=True
)

for chunk in response:
    print(chunk["message"]["content"], end="", flush=True)
```
### 📝 Exercises

1. Use the SDK to output a list of all installed models.
2. Write a small chat script that allows a looped conversation.

### ✅ Solutions

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

## Unit 7 — Basics of working with LLMs

### 📖 Background

Large Language Models (LLMs) are AI models trained on billions of texts. You learn to predict the next word in a sentence. This allows them to generate texts, answer questions and summarize. Typical models: GPT-4, Llama-2, Mistral. Ollama enables these models to be used locally. Use in AI apps: chatbots, text summaries, code helpers.

### 💻 Code examples

#### Text summarizer with ollama

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
### 📝 Exercises

1. Explain why LLMs do not always give correct answers (hallucinations).
2. Write a script that asks Ollama a question and prints the answer.

### ✅ Solutions

- LLMs are based on probabilities and sometimes invent plausible but false content → “hallucinations”.

```python
import requests
frage = "Was ist die Hauptstadt von Frankreich?"
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": frage})
print("Antwort:", r.json()["response"])
```
---

## Unit 8 — Prompt Engineering Basics

### 📖 Background

Prompt engineering = the art of formulating good input for a language model. Different formulations lead to different results. A good prompt contains:

- clear instructions
- Context
- desired format

Example: “Summarize the text” vs. “Summarize the text in 3 bullet points”.

### 💻 Code examples

#### Prompt Playground with ollama

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
### 📝 Exercises

1. Create three different prompts that summarize the same text but with different styles (short, detailed, bullet points).
2. Use Ollama to test how the results differ.

### ✅ Solutions

- Prompt 1: “Summarize this article in 1 sentence.”
- Prompt 2: “Write a detailed summary in 5 sentences.”
- Prompt 3: “Summarize the article in bullet points.”

---

## Unit 9 — Summary

After this day, students can:

- explain what AI, ML and LLMs are,
- Install Ollama locally and use the first models,
- Operate Ollama via the CLI (`pull`, `list`, `run`),
- Access Ollama via the REST API with `curl`,
- Integrate Ollama into Python apps with `requests`,
- Use Ollama conveniently via the SDK (including streaming),
- build simple AI apps with Streamlit and Ollama,
- Formulate prompts specifically to get better results.

---

## Unit 10 — Mini Projects

### Mini Project 1: AI chatbot with personality

**Task:** Build a chatbot that behaves like a friendly tutor.

**Solution:**

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
### Mini Project 2: Text Classification (Sentiment Analysis)

**Task:** Classify texts as positive, neutral or negative.

**Solution:**

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
### Mini Project 3: Creative Text Generator

**Task:** Generate creative texts based on a theme and style.

**Solution:**

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
### Mini Project 4: FAQ bot with knowledge base

**Task:** Upload an FAQ file and answer questions about it.

**Solution:**

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
### Mini Project 5: Language Translator

**Task:** Translate texts between different languages.

**Solution:**

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
