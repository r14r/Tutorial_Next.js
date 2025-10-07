# Tag 3 — Datenverarbeitung & KI-Anwendungen

## 📅 Zeitplan 09:00 – 15:00

### Übersicht

Der Tag vermittelt praxisnah die Grundlagen der KI-Textanalyse mit Ollama und Python. Jede Einheit besteht aus einer kurzen Erklärung, Beispielen und praktischen Übungen.

---

### Zeitplan

| Zeit              | Einheit / Inhalt                                                                                   | Dauer   |
|-------------------|----------------------------------------------------------------------------------------------------|---------|
| **09:00 – 09:20** | Einführung & Überblick  
  Motivation, Ziele, KI-Anwendungen                                                 | 20 min  |
| **09:20 – 09:50** | **Einheit 3.1:** Einführung in Textanalyse  
  Grundbegriffe, Aufgaben                                                           | 30 min  |
| **09:50 – 10:30** | **Einheit 3.2:** Sentimentanalyse  
  Stimmung erkennen, Beispiele, Übungen                                             | 40 min  |
| **10:30 – 11:10** | **Einheit 3.3:** Themenklassifikation  
  Kategorien, Labeling, Übungen                                                     | 40 min  |
| **11:10 – 11:25** | ☕ **Pause**                                                                                        | 15 min  |
| **11:25 – 12:00** | **Einheit 3.4:** Schlüsselwort-Extraktion  
  Keywords, Listen, Übungen                                                         | 35 min  |
| **12:00 – 12:35** | **Einheit 3.5:** Named Entity Recognition (NER)  
  Personen, Orte, Organisationen                                                    | 35 min  |
| **12:35 – 13:35** | 🍽️ **Mittagspause**                                                                                | 60 min  |
| **13:35 – 14:05** | **Einheit 3.6:** FAQ-Bot mit Ollama  
  FAQ-Upload, Bot-Logik, Übungen                                                    | 30 min  |
| **14:05 – 14:35** | **Einheit 3.7:** Kombination von Analysen  
  Sentiment + Keywords + Entities                                                   | 30 min  |
| **14:35 – 15:00** | **Einheit 3.8:** Analyse-Dashboard mit Streamlit  
  App bauen, Zusammenfassung                                                        | 25 min  |

---

## Ablauf der Einheiten

- **Erklärung:** ca. 10–15 min
- **Beispiele:** ca. 10 min
- **Übungen:** ca. 15–20 min  
    → Übungen werden direkt in Python, Jupyter oder Streamlit durchgeführt.

---

## Mini-Projekt (ab 14:35)

Am Ende des Tages wird ein Analyse-Dashboard entwickelt, das folgende Funktionen kombiniert:

- **Eingabe:** Textfeld
- **Verarbeitung:** Sentiment, Keywords, Named Entities
- **Ausgabe:** Übersichtliche Darstellung der Analyse-Ergebnisse

---

## Einheit 3.1 — Einführung in Textanalyse

### Hintergrund

Textanalyse ist eine Kernaufgabe vieler KI-Anwendungen. Typische Aufgaben sind:

- **Klassifikation:** Thema, Kategorie, Label
- **Bewertung:** Stimmung (positiv/negativ/neutral)
- **Strukturierung:** Schlüsselwörter extrahieren
- **Informationsextraktion:** Named Entities (Namen, Orte, Organisationen)

LLMs sind prädestiniert für diese Aufgaben, da sie auf großen Textmengen trainiert wurden und semantische Zusammenhänge erkennen. Sie sind wertvoll für Business Intelligence, Social Media Monitoring, Chatbots und Customer Feedback.

---

## Einheit 3.2 — Sentimentanalyse (Stimmung erkennen)

### Hintergrund

Sentimentanalyse wird in Bereichen wie Marketing, Social Media und Produktbewertungen eingesetzt.

### Beispiele

#### Beispiel 1: Einfacher Prompt

```python
import requests

text = "Ich liebe dieses neue Produkt, es ist fantastisch!"
prompt = f"Analysiere die Stimmung: {text}"

r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": prompt})
print(r.json()["response"])
```

#### Beispiel 2: Klassifizierung erzwingen

```python
prompt = """Analysiere die Stimmung und antworte NUR mit einem dieser Wörter:
- Positiv
- Negativ
- Neutral
Text: Ich bin enttäuscht von der Qualität."""
```

#### Beispiel 3: Streamlit-Formular

```python
import streamlit as st
import requests

st.title("Sentiment Analyse")

text = st.text_area("Text eingeben")
if st.button("Analysieren"):
    prompt = f"Stimmung (Positiv/Negativ/Neutral): {text}"
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    st.write("Stimmung:", r.json()["response"])
```

### Übungen

1. Analysiere den Satz: „Der Service war langsam, aber das Essen war lecker.“
2. Baue ein Python-Skript, das mehrere Sätze aus einer Liste analysiert.
3. Schreibe eine Funktion `analyze_sentiment(text)`, die nur "Positiv", "Negativ" oder "Neutral" zurückgibt.

#### Lösungen

```python
# 1. Gemischte Stimmung → oft "Neutral" oder "Gemischt"
text = "Der Service war langsam, aber das Essen war lecker."
# Modell sagt z. B. "Neutral"

# 2. Liste verarbeiten
texts = ["Super Qualität!", "Völlig unbrauchbar!", "Ganz okay."]
for t in texts:
    prompt = f"Stimmung: {t}"
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    print(t, "→", r.json()["response"])

# 3. Funktion
def analyze_sentiment(text):
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": f"Analysiere Stimmung: {text}"})
    return r.json()["response"]

print(analyze_sentiment("Das Konzert war großartig!"))
```

---

## Einheit 3.3 — Themenklassifikation

### Hintergrund

LLMs können Texte thematisch einordnen – ohne spezielles Training. Beispiele: Sport, Politik, Wissenschaft, Unterhaltung.

### Beispiele

#### Beispiel 1: Klassische Klassifikation

```python
text = "Apple hat ein neues iPhone vorgestellt."
prompt = f"Ordne diesen Text einem Thema zu (Technologie, Politik, Sport, Unterhaltung): {text}"
```

#### Beispiel 2: JSON-Ausgabe erzwingen

```python
text = "Die Regierung hat ein neues Gesetz verabschiedet."
prompt = f"""Klassifiziere den Text und antworte im JSON-Format:
{{
  "Text": "{text}",
  "Thema": "<Kategorie>"
}}
"""
```

#### Beispiel 3: Mehrere Texte

```python
texts = [
    "Die Aktie von Tesla stieg um 5%.",
    "Lionel Messi schoss 2 Tore.",
    "Das Parlament diskutierte ein neues Gesetz."
]

for t in texts:
    prompt = f"Welches Thema? {t}"
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    print(t, "→", r.json()["response"])
```

### Übungen

1. Schreibe eine Funktion `classify(text, labels)`, die eine Klassifikation basierend auf einer Label-Liste durchführt.
2. Teste mit den Labels ["Sport", "Politik", "Technologie"].
3. Erstelle eine kleine App, die CSV-Dateien mit Nachrichten einliest und jede Nachricht klassifiziert.

#### Lösungen

```python
# 1. Funktion
def classify(text, labels):
    prompt = f"Klassifiziere den Text '{text}' in eine dieser Kategorien: {', '.join(labels)}"
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    return r.json()["response"]

print(classify("Messi schoss ein Tor.", ["Sport", "Politik", "Technologie"]))

# 3. CSV-App
import pandas as pd
import streamlit as st

file = st.file_uploader("Nachrichten CSV", type="csv")
if file:
    df = pd.read_csv(file)
    for row in df["Text"]:
        st.write(row, "→", classify(row, ["Sport", "Politik", "Technologie"]))
```

---

## Einheit 3.4 — Schlüsselwort-Extraktion

### Hintergrund

Schlüsselwörter sind wichtig für Suchmaschinen, Zusammenfassungen und Daten-Tagging. LLMs können automatisch die wichtigsten Begriffe herausziehen.

### Beispiele

#### Beispiel 1: Einfache Extraktion

```python
text = "Tesla bringt ein neues Elektroauto mit innovativer Batterie auf den Markt."
prompt = f"Extrahiere die wichtigsten Keywords: {text}"
```

#### Beispiel 2: Ausgabe als Liste

```python
prompt = """Finde die Keywords und gib sie als Python-Liste zurück.
Text: KI verändert die Medizin durch Bildanalyse und Sprachmodelle."""
```

#### Beispiel 3: Kombination mit JSON

```python
prompt = """Analysiere den Text und gib zurück:
{
  "Keywords": ["..."],
  "Anzahl": <int>
}
Text: Die FIFA organisiert die Weltmeisterschaft in Katar."""
```

### Übungen

1. Extrahiere Keywords für den Text: „Microsoft investiert Milliarden in KI.“
2. Schreibe eine Funktion `extract_keywords(text)`, die eine Liste zurückgibt.
3. Baue eine App, die ein PDF hochlädt, den Text extrahiert und Keywords ausgibt.

#### Lösungen

```python
def extract_keywords(text):
    prompt = f"Extrahiere Keywords als Liste: {text}"
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    return r.json()["response"]

print(extract_keywords("Microsoft investiert Milliarden in KI."))
```

---

## Einheit 3.5 — Named Entity Recognition (NER)

### Hintergrund

NER bedeutet: Eigennamen (Personen, Orte, Organisationen) erkennen.

### Beispiele

#### Beispiel 1: Einfache Entities

```python
text = "Barack Obama sprach 2015 in Berlin."
prompt = f"Finde Named Entities (Person, Ort, Organisation): {text}"
```

#### Beispiel 2: JSON-Ausgabe

```python
text = "Elon Musk gründete SpaceX in Kalifornien."
prompt = """Extrahiere Named Entities und gib im JSON-Format zurück:
{
  "Personen": [],
  "Orte": [],
  "Organisationen": []
}
Text: Elon Musk gründete SpaceX in Kalifornien."""
```

#### Beispiel 3: Mehrere Sätze

```python
text = "Angela Merkel traf Emmanuel Macron in Paris. Microsoft investierte in OpenAI."
prompt = f"Liste alle Named Entities: {text}"
```

### Übungen

1. Extrahiere Entities aus: „Jeff Bezos gründete Amazon in Seattle.“
2. Schreibe eine Funktion `extract_entities(text)` mit JSON-Ausgabe.
3. Baue eine App, die einen hochgeladenen Text analysiert und alle Entities als Tabelle ausgibt.

#### Lösungen

```python
def extract_entities(text):
    prompt = """Extrahiere Named Entities im JSON-Format:
{
  "Personen": [],
  "Orte": [],
  "Organisationen": []
}
Text: %s""" % text
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    return r.json()["response"]

print(extract_entities("Jeff Bezos gründete Amazon in Seattle."))
```

---

## Einheit 3.6 — FAQ-Bot mit Ollama

### Hintergrund

Ein FAQ-Bot kann häufig gestellte Fragen beantworten. Man lädt ein Dokument oder eine FAQ-Liste hoch, und das Modell antwortet basierend auf diesem Text.

### Beispiele

#### Beispiel 1: FAQ als Text

```python
faq = """Q: Was ist Python?
A: Eine Programmiersprache.

Q: Was ist KI?
A: Maschinen, die Aufgaben wie Menschen lösen."""
prompt = f"Beantworte die Frage basierend auf dieser FAQ:\n{faq}\n\nFrage: Was ist KI?"
```

#### Beispiel 2: Datei-Upload

```python
import streamlit as st

file = st.file_uploader("FAQ hochladen", type="txt")
if file:
    faq = file.read().decode()
    frage = st.text_input("Stelle eine Frage:")
    if st.button("Antworten"):
        prompt = f"Beantworte die Frage aus der FAQ:\n{faq}\nFrage: {frage}"
```

#### Beispiel 3: Mehrere FAQ-Dateien

```python
files = st.file_uploader("Mehrere FAQs", type="txt", accept_multiple_files=True)
faq_data = ""
if files:
    for f in files:
        faq_data += f.read().decode() + "\n"
```

### Übungen

1. Schreibe deine eigene FAQ mit mindestens 3 Fragen.
2. Baue eine App, die mehrere FAQ-Dateien akzeptiert und kombiniert.
3. Teste, wie das Modell reagiert, wenn eine Frage nicht in der FAQ steht.

---

## Einheit 3.7 — Kombination von Analysen (Sentiment + Keywords + Entities)

### Hintergrund

LLMs können mehrere Aufgaben gleichzeitig lösen, z. B. Stimmung und Schlüsselwörter aus Text extrahieren.

### Beispiele

#### Beispiel 1: Stimmung + Keywords

```python
text = "Das neue iPhone ist beeindruckend, aber sehr teuer."
prompt = """Analysiere diesen Text:
1. Stimmung (Positiv/Negativ/Neutral)
2. Keywords"""
```

#### Beispiel 2: Alles in einem

```python
text = "Angela Merkel hielt in Berlin eine Rede über die EU."
prompt = """Analysiere den Text:
- Stimmung
- Keywords
- Named Entities
- Kurze Zusammenfassung"""
```

### Übungen

1. Schreibe eine Funktion `analyze(text)` die Stimmung, Keywords und Entities zurückgibt.
2. Baue ein kleines Dashboard, das für mehrere Texte diese Analyse macht.

#### Lösungen

```python
def analyze(text):
    prompt = """Analysiere den Text:
1. Stimmung
2. Keywords
3. Named Entities"""
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    return r.json()["response"]
```

---

## Einheit 3.8 — Erweiterte Streamlit-App: Analyse-Dashboard

### Hintergrund

Man kann eine App bauen, die alle Analyse-Funktionen integriert: Sentiment, Keywords, NER, Zusammenfassung.

### Beispiel: Streamlit-Dashboard

```python
import streamlit as st
import requests

st.title("Textanalyse Dashboard")

text = st.text_area("Text eingeben")

if st.button("Analysieren") and text:
    prompt = """
Analysiere diesen Text:
1. Stimmung (Positiv/Negativ/Neutral)
2. Keywords
3. Named Entities (Personen, Orte, Organisationen)
4. Zusammenfassung in 2 Sätzen
Text: %s
""" % text
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    st.subheader("Analyse-Ergebnis")
    st.write(r.json()["response"])
```

---

## Zusammenfassung Tag 3

Nach Tag 3 können die Studierenden:

- Texte mit Ollama analysieren (Stimmung, Themen, Keywords, Entities)
- einen FAQ-Bot mit Dokumenten erstellen
- mehrere Analysen kombinieren
- ein eigenes Analyse-Dashboard in Streamlit bauen
- die Grenzen solcher Modelle erkennen (Halluzinationen, Mehrdeutigkeit)

---

> **Ausblick:**  
> Soll für Tag 4 (Fortgeschrittene Anwendungen: Datenintegration mit Pandas, Q&A über CSV-Dateien, KI-Dashboards, Deployment) auch ein vollständiges Lehrbuch-Kapitel mit vielen Beispielen erstellt werden?
