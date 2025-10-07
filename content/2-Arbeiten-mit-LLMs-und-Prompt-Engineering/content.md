# Tag 2 — Arbeiten mit LLMs & Prompt Engineering

## 📅 Zeitplan 09:00 – 15:00

### Übersicht

Der Tag bietet eine praxisnahe Einführung in Large Language Models (LLMs) und Prompt Engineering. Jede kombiniert kurze Erklärungen, Code-Beispiele und praktische Übungen.

---

### Zeitplan

| Zeit              | / Inhalt                                                                                   | Dauer   |
|-------------------|----------------------------------------------------------------------------------------------------|---------|
| **09:00 – 09:20** | Einführung & Überblick,   Was sind LLMs? Ziele des Tages                                           | 20 min  |
| **09:20 – 09:50** | **2.1:** Einführung in LLMs,   Hintergrund, Einsatzgebiete, Grenzen                        | 30 min  |
| **09:50 – 10:20** | **2.2:** Was ist ein Prompt? Prompt-Elemente, Beispiele, Übungen                           | 30 min  |
| **10:20 – 10:50** | **2.3:** Rollen im Prompting & Grundlagen,   System/User/Assistant, Prompt Engineering                                         | 30 min  |
| **10:50 – 11:05** | ☕ **Pause**                                                                                        | 15 min  |
| **11:05 – 11:35** | **2.4:** Prompting-Prinzipien ,   Zero-/Few-Shot, Chain-of-Thought, Output-Format                                   | 30 min  |
| **11:35 – 12:05** | **2.5:** Prompt-Playground & Vergleich,   Streamlit-App, Prompt-Experimente                                                 | 30 min  |
| **12:05 – 13:05** | 🍽️ **Mittagspause**                                                                                | 60 min  |
| **13:05 – 13:35** | **2.6:** Temperatur & Kreativität ,  Parameter, Temperature, Max Tokens                                                | 30 min  |
| **13:35 – 14:05** | **2.7:** Vergleich verschiedener Modelle ,   llama2, mistral, codellama                                                        | 30 min  |
| **14:05 – 14:35** | **2.8:** Fehler & Grenzen von LLMs  ,   Halluzinationen, Bias, Kontext                                                    | 30 min  |
| **14:35 – 14:55** | **2.9:** Praktische Prompt-Beispiele  ,   Zusammenfassung, Rollen, Code, JSON                                               | 20 min  |
| **14:55 – 15:00** | **Zusammenfassung & Ausblick**  ,   Wiederholung, Fragen, nächste Schritte                                            | 5 min   |

---

## Ablauf der en

- **Erklärung:** ca. 10–15 min
- **Code-Beispiele:** ca. 10 min
- **Übungen:** ca. 10–15 min  
    → Übungen werden direkt im Editor, Jupyter oder Streamlit durchgeführt.

---

## 2.1 — Einführung in Large Language Models (LLMs)

### Hintergrund

Large Language Models (LLMs) wie GPT, Llama, Mistral oder Gemma sind KI-Modelle, die auf Milliarden von Texten trainiert wurden.  
Sie lernen, das nächste Wort vorherzusagen und entwickeln dadurch erstaunliche Sprachfähigkeiten.

**Einsatzgebiete:**  

- Textgenerierung  
- Zusammenfassung  
- Übersetzung  
- Q&A  
- Codegenerierung

LLMs sind probabilistisch (nicht deterministisch), d. h. bei gleichem Prompt kann es verschiedene Antworten geben.

**Grenzen:**  

- Halluzinationen (falsche Antworten)  
- Kein echtes „Verstehen“, sondern Mustererkennung  
- Kontextlimitierungen

---

## 2.2 — Was ist ein Prompt?

### Hintergrund

Ein Prompt ist die Eingabe, die ein Mensch einem Sprachmodell (LLM) gibt.  
Man kann sich ein Prompt vorstellen wie eine Anweisung an ein sehr intelligentes, aber textbasiertes Programm.

**Elemente eines guten Prompts:**  

- Rolle – definiert, in welcher „Rolle“ das Modell antworten soll (z. B. „Du bist ein Lehrer…“)
- Kontext – liefert Hintergrundinformationen oder Daten, auf die sich die Antwort beziehen soll
- Aufgabe – die eigentliche Anweisung („Fasse den Text zusammen“, „Schreibe ein Gedicht“)
- Format – gewünschte Ausgabeform (z. B. Bulletpoints, JSON, Tabellenform)

### Code-Beispiele

```python
import requests

prompt = "Erkläre Maschinelles Lernen in einfachen Worten."
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": prompt})
print(r.json()["response"])
```

**Prompt mit Rolle & Format:**

```python
prompt = """Du bist ein Universitätsprofessor für Informatik.
Erkläre den Begriff 'Maschinelles Lernen' in 3 Bulletpoints für Studierende im ersten Semester."""
```

**Prompt mit Kontext:**

```python
text = "Python ist eine Programmiersprache, die 1991 von Guido van Rossum entwickelt wurde."
prompt = f"Fasse den folgenden Text in 2 Sätzen zusammen:\n\n{text}"
```

### Übungen

1. Nenne drei typische Anwendungen von LLMs.
2. Erkläre, warum LLMs manchmal halluzinieren.

### Lösungen

- Chatbots, Textzusammenfassungen, Programmierhilfe.
- Sie basieren auf Wahrscheinlichkeiten, nicht auf „Wissen“.

---

## 2.3 — Rollen im Prompting & Prompt Engineering: Grundlagen

### Hintergrund

Prompt Engineering bezeichnet die Kunst, Eingaben (Prompts) so zu formulieren, dass das Modell bestmögliche Ergebnisse liefert.

In modernen APIs (z. B. Ollama, OpenAI) bestehen Prompts aus Nachrichten mit Rollen:

- **system** – definiert die Identität des Modells („Du bist ein hilfreicher Tutor…“)
- **user** – enthält die Anfrage des Nutzers
- **assistant** – (optional) vorherige Antworten des Modells, um Konversationen fortzuführen
- **tool/function** – (in erweiterten Frameworks) spezielle Funktionsaufrufe

Ein Prompt enthält:

- Aufgabe („Fasse zusammen…“)
- Kontext („Der Text ist ein Artikel über…“)
- Format („in Bulletpoints“)

Unterschiedliche Formulierungen → unterschiedliche Ergebnisse.

### Code-Beispiele

**Prompt mit Rollen:**

```python
messages = [
    {"role": "system", "content": "Du bist ein freundlicher Lehrer."},
    {"role": "user", "content": "Erkläre neuronale Netze in einfachen Worten."}
]

r = requests.post("http://localhost:11434/api/chat",
                  json={"model": "llama2", "messages": messages})
print(r.json()["message"]["content"])
```

**Vergleich zweier Prompts:**

```python
p1 = "Fasse den Text kurz zusammen."
p2 = "Erstelle eine ausführliche Zusammenfassung in 5 Sätzen."

for p in [p1, p2]:
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": p})
    print("Prompt:", p)
    print("Antwort:", r.json()["response"])
```

### Übungen

1. Formuliere drei Prompts, die denselben Text unterschiedlich zusammenfassen.
2. Experimentiere: Welche Formulierung liefert die besten Ergebnisse?

### Lösungen

- Prompt 1: „Fasse in 1 Satz zusammen.“
- Prompt 2: „Fasse in 5 Sätzen zusammen.“
- Prompt 3: „Fasse in Bulletpoints zusammen.“

---

## 2.4 — Prompting-Prinzipien

### Hintergrund

Um bessere Ergebnisse zu erzielen, gibt es verschiedene Strategien:

- **Zero-Shot Prompting** – Aufgabe ohne Beispiele
- **Few-Shot Prompting** – Aufgabe mit Beispielen
- **Role Prompting** – Modell in eine Rolle versetzen
- **Chain-of-Thought (CoT)** – Modell auffordern, Schritt-für-Schritt zu denken
- **Self-Consistency** – mehrere Antworten generieren und vergleichen
- **Output-Format Prompting** – Antwort in bestimmtem Format anfordern

### Beispiele

**Zero-Shot Prompting:**

```python
prompt = "Übersetze folgenden Satz ins Französische: 'Ich liebe KI.'"
```

**Few-Shot Prompting:**

```python
prompt = """Übersetze ins Französische:

Deutsch: Hallo → Französisch: Bonjour
Deutsch: Danke → Französisch: Merci
Deutsch: Ich liebe KI → Französisch:"""
```

**Role Prompting:**

```python
prompt = """Du bist ein Arzt.
Erkläre die Symptome einer Grippe für einen Patienten in einfacher Sprache."""
```

**Chain-of-Thought Prompting:**

```python
prompt = """Löse die Aufgabe Schritt für Schritt:
Frage: Ein Apfel kostet 2€, eine Orange 3€. Wie viel kostet es, 4 Äpfel und 2 Orangen zu kaufen?"""
```

**Self-Consistency:**

```python
for i in range(3):
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": "Rechne 37+45 Schritt für Schritt."})
    print(r.json()["response"])
```

**Output-Format Prompting (JSON):**

```python
prompt = """Antworte nur im folgenden JSON-Format:
{
  "Name": "<string>",
  "Alter": <int>
}
Frage: Person heißt Alice und ist 30 Jahre alt."""
```

---

## 2.5 — Prompt-Playground & Prompt-Vergleich (Streamlit-App)

### Hintergrund

Ein Prompt-Playground ist eine kleine App, in der man Prompts eingeben und sofort sehen kann, wie das Modell reagiert.  
Hilfreich zum Experimentieren.  
Ideal, um zu verstehen, wie kleine Änderungen den Output beeinflussen.

Man kann eine App bauen, die zwei Prompts nebeneinander testet – sehr nützlich zum Prompt Engineering.

### Code-Beispiele

**Prompt Playground:**

```python
import streamlit as st
import requests

st.title("Prompt Playground")
model = st.selectbox("Modell wählen", ["llama2", "mistral"])
prompt = st.text_area("Prompt eingeben")

if st.button("Start") and prompt:
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": model, "prompt": prompt})
    st.markdown(r.json()["response"])
```

**Prompt-Vergleich:**

```python
import streamlit as st
import requests

st.title("Prompt-Vergleich")

p1 = st.text_area("Prompt 1")
p2 = st.text_area("Prompt 2")
model = st.selectbox("Modell", ["llama2", "mistral"])

if st.button("Vergleichen"):
    for i, p in enumerate([p1, p2], start=1):
        if p:
            r = requests.post("http://localhost:11434/api/generate",
                              json={"model": model, "prompt": p})
            st.subheader(f"Antwort {i}")
            st.write(r.json()["response"])
```

### Übungen

1. Erweitere den Playground um ein Dropdown-Menü zur Auswahl verschiedener Modelle.
2. Füge eine Option hinzu, die die Antwort in Markdown darstellt.

---

## 2.6 — Temperatur & Steuerung der Kreativität

### Hintergrund

LLMs haben Parameter, die das Verhalten beeinflussen:

- **Temperature:** 0 = deterministisch, 1 = kreativ, >1 = chaotisch
- **Max Tokens:** begrenzt die Länge der Antwort
- **Top-k / Top-p:** steuern die Auswahlwahrscheinlichkeit von Wörtern

### Code-Beispiel

```python
prompt = "Schreibe eine kurze Geschichte über eine Katze und einen Roboter."

for t in [0.0, 0.7, 1.2]:
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt,
                            "options": {"temperature": t}})
    print(f"Temp={t}:", r.json()["response"])
```

### Übungen

1. Erzeuge denselben Prompt mit temperature = 0.0, 0.7 und 1.5. Vergleiche die Ergebnisse.
2. Was ist besser für technische Dokumentationen – hohe oder niedrige Temperatur?

### Lösungen

- Unterschied: 0.0 = sehr nüchtern, 0.7 = kreativ, 1.5 = chaotisch.
- Niedrige Temperatur (präziser, weniger kreative Ausschweifungen).

---

## 2.7 — Vergleich verschiedener Modelle

### Hintergrund

Ollama unterstützt mehrere Modelle. Jedes hat Stärken & Schwächen:

- **Llama2:** allgemeines Sprachmodell
- **Mistral:** schnell & kompakt
- **Codellama:** spezialisiert auf Programmierung

### Code-Beispiel

```python
import requests

models = ["llama2", "mistral"]
prompt = "Erkläre den Unterschied zwischen Python und Java."

for m in models:
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": m, "prompt": prompt})
    print(m, ":", r.json()["response"])
```

### Übungen

1. Vergleiche llama2 und mistral bei der Aufgabe: „Fasse einen Text in 3 Sätzen zusammen.“
2. Teste ein Code-Modell mit dem Prompt: „Schreibe eine Python-Funktion für die Fibonacci-Zahlen.“

### Lösungen

- Modelle geben unterschiedliche Stile zurück – mistral oft kürzer, llama2 detaillierter.
- Codellama liefert meist besseren Python-Code als ein Standardmodell.

---

## 2.8 — Fehler & Grenzen von LLMs

### Hintergrund

LLMs sind mächtig, aber nicht perfekt:

- Halluzinationen: erfundene Fakten
- Bias: Vorurteile aus Trainingsdaten
- Keine Rechenmaschine: Mathe kann fehlerhaft sein
- Kontextfenster: zu lange Texte werden abgeschnitten

### Code-Beispiel

```python
prompt = "Was ist die Hauptstadt von Frankreich in Afrika?"
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": prompt})
print(r.json()["response"])
# → Beispiel für Halluzination
```

### Übungen

1. Probiere absichtlich fehlerhafte Fragen (z. B. „Wer hat 1800 den Nobelpreis für KI gewonnen?“).
2. Analysiere, warum die Antworten trotzdem plausibel klingen.

### Lösungen

- Das Modell „halluziniert“ eine Antwort.
- Es wurde darauf trainiert, wahrscheinlich klingende Texte zu erzeugen, nicht Fakten.

---

## 2.9 — Praktische Beispiele für Prompts

1. Text zusammenfassen  
   `prompt = "Fasse folgenden Text in 3 Bulletpoints zusammen:\nText: ..."`

2. Als Rolle agieren  
   `prompt = "Du bist ein Reiseberater. Empfiehl mir 3 Orte in Italien."`

3. Korrekturlesen  
   `prompt = "Korrigiere Rechtschreibfehler im folgenden Text: 'Das is ein Beispil'."`

4. Code erklären  
   `prompt = "Erkläre diesen Python-Code Schritt für Schritt:\n\nfor i in range(5): print(i)"`

5. JSON-Ausgabe erzwingen  

   ```python
   prompt = """Analysiere folgenden Satz: 'Die KI ist faszinierend.'
   Antworte im JSON-Format:
   {"Sprache": "Deutsch", "Stimmung": "positiv"}"""
   ```

---

## Zusammenfassung Tag 2

Nach Tag 2 können die Studierenden:

- erklären, wie LLMs arbeiten und wo ihre Grenzen liegen,
- Prompts gezielt formulieren und die Antworten vergleichen,
- die Parameter (Temperature, Tokens) steuern,
- mit mehreren Modellen experimentieren,
- einen Prompt-Playground in Streamlit bauen,
- verstehen, was ein Prompt ist und wie er aufgebaut sein sollte (Rolle, Kontext, Aufgabe, Format),
- die verschiedenen Rollen (system, user, assistant) einsetzen,
- die wichtigsten Prompt-Prinzipien anwenden: Zero-/Few-Shot, Role, Chain-of-Thought, Self-Consistency, Format-Prompting,
- Prompts für konkrete Aufgaben wie Zusammenfassung, Rollen, Code-Erklärung oder JSON-Ausgaben formulieren.
