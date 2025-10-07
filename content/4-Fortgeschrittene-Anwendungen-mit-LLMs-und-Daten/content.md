# Tag 4 — Fortgeschrittene Anwendungen mit LLMs & Daten

## 📅 Zeitplan 09:00 – 15:00

### Übersicht

Der Tag vertieft fortgeschrittene Anwendungen mit LLMs und Datenintegration. Jede Einheit enthält kurze Erklärungen, praktische Beispiele und Übungen.

---

### Zeitplan

| Zeit              | Einheit / Inhalt                                                                                   | Dauer   |
|-------------------|----------------------------------------------------------------------------------------------------|---------|
| **09:00 – 09:20** | Einführung & Überblick  
  Motivation, Ziele des Tages                                                       | 20 min  |
| **09:20 – 10:05** | **Einheit 4.1:** Datenintegration mit Pandas  
  CSV/Excel laden, filtern, LLM-Integration                                         | 45 min  |
| **10:05 – 10:35** | **Einheit 4.2:** Q&A über CSV-Dateien  
  Abfragen, LLM-Antworten, Streamlit-App                                            | 30 min  |
| **10:35 – 11:15** | **Einheit 4.3:** KI-Dashboards mit Streamlit  
  Diagramme, LLM-Kommentare, Gruppenvergleich                                       | 40 min  |
| **11:15 – 11:30** | ☕ **Pause**                                                                                        | 15 min  |
| **11:30 – 12:10** | **Einheit 4.4:** Deployment  
  App starten, requirements.txt, Docker, Streamlit Cloud                            | 40 min  |
| **12:10 – 12:40** | **Einheit 4.5:** Bonus: Q&A über mehrere Datenquellen  
  CSV + FAQ/Text, kombinierte Analyse                                               | 30 min  |
| **12:40 – 13:10** | Übungen & Praxis  
  Eigene Datenquellen, Mini-Projekt starten                                         | 30 min  |
| **13:10 – 14:10** | 🍽️ **Mittagspause**                                                                                | 60 min  |
| **14:10 – 14:40** | Mini-Projekt & Präsentation  
  App mit mehreren Datenquellen, Q&A, Dashboard                                     | 30 min  |
| **14:40 – 15:00** | Zusammenfassung & Ausblick  
  Reflexion, nächste Schritte                                                       | 20 min  |

---

## Ablauf der Einheiten

- **Erklärung:** ca. 10–15 min
- **Beispiele:** ca. 10 min
- **Übungen:** ca. 15–20 min  
    → Übungen werden direkt in Jupyter, VS Code oder Streamlit durchgeführt.

---

## Mini-Projekt (14:10–14:40)

Am Ende des Tages wird eine App entwickelt, die folgende Funktionen kombiniert:

- **CSV-Upload**
- **FAQ/Text-Upload**
- **Verarbeitung:** Datenanalyse mit Pandas und LLM
- **Dashboard:** Diagramme, KI-Kommentare
- **Q&A:** Fragen zu kombinierten Datenquellen

---

## Einheit 4.1 — Datenintegration mit Pandas

### Beispiele

#### Beispiel 1 — CSV laden

```python
import pandas as pd
df = pd.read_csv("sales.csv")
print(df.head())
```

#### Beispiel 2 — Excel laden

```python
df = pd.read_excel("data.xlsx")
print(df.shape)
```

#### Beispiel 3 — Filterung

```python
kunden = df[df["Country"] == "Germany"]
print(kunden)
```

#### Beispiel 4 — LLM-Integration

```python
import requests
stats = df.describe().to_string()
prompt = f"Analysiere die Verkaufsdaten:\n{stats}"
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": prompt})
print(r.json()["response"])
```

### Übungen

- Lade eine CSV mit Spalten Name, Alter, Einkommen. Berechne den Median des Einkommens.
- Filtere alle Kunden über 40 Jahre.
- Schicke die Statistik an Ollama und bitte um eine wirtschaftliche Interpretation.
- Sortiere die Kunden nach Einkommen absteigend.

### Lösungen

```python
df = pd.read_csv("kunden.csv")
print(df["Einkommen"].median())
print(df[df["Alter"] > 40])
stats = df.describe().to_string()
prompt = f"Welche wirtschaftlichen Trends lassen sich erkennen?\n{stats}"
print(df.sort_values("Einkommen", ascending=False))
```

---

## Einheit 4.2 — Q&A über CSV-Dateien

### Beispiele

#### Beispiel 1 — Einfache Abfrage

```python
frage = "Wie viele Kunden sind älter als 30?"
antwort = len(df[df["Alter"] > 30])
print(antwort)
```

#### Beispiel 2 — Antwort mit LLM

```python
stats = df.describe().to_string()
prompt = f"""Beantworte die Frage basierend auf diesen Daten:
{stats}
Frage: Wie viele Kunden sind älter als 30?"""
```

#### Beispiel 3 — Streamlit-App

```python
import streamlit as st

file = st.file_uploader("CSV hochladen", type="csv")
if file:
    df = pd.read_csv(file)
    frage = st.text_input("Frage:")
    if frage:
        stats = df.describe().to_string()
        prompt = f"{frage}\nDaten:\n{stats}"
        r = requests.post("http://localhost:11434/api/generate",
                          json={"model": "llama2", "prompt": prompt})
        st.write("Antwort:", r.json()["response"])
```

### Übungen

- Implementiere: „Wie viele verschiedene Städte gibt es in der CSV?“
- Schreibe eine Funktion `answer_question(df, frage)`, die pandas + Ollama kombiniert.
- Teste die Frage: „Welcher Kunde hat das höchste Einkommen?“

### Lösungen

```python
# Anzahl Städte
print(df["Stadt"].nunique())

# Funktion
def answer_question(df, frage):
    stats = df.describe().to_string()
    prompt = f"Frage: {frage}\nDaten:\n{stats}"
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    return r.json()["response"]

print(answer_question(df, "Was ist der Durchschnitt des Alters?"))

# Pandas-Lösung
print(df.loc[df["Einkommen"].idxmax()])
```

---

## Einheit 4.3 — KI-Dashboards mit Streamlit

### Beispiele

#### Beispiel 1 — Balkendiagramm

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
df["Sales"].plot(kind="bar", ax=ax)
st.pyplot(fig)
```

#### Beispiel 2 — Histogramm

```python
fig, ax = plt.subplots()
df["Age"].hist(ax=ax, bins=10)
st.pyplot(fig)
```

#### Beispiel 3 — LLM-Kommentar

```python
stats = df.describe().to_string()
prompt = f"Erkläre die wichtigsten Trends:\n{stats}"
```

#### Beispiel 4 — Vergleich zweier Gruppen

```python
city1, city2 = "Berlin", "Hamburg"
df1 = df[df["City"] == city1]
df2 = df[df["City"] == city2]
prompt = f"Vergleiche {city1} und {city2}:\n{df1.describe().to_string()}\n{df2.describe().to_string()}"
```

### Übungen

- Erstelle ein Dashboard mit Altersverteilung (Histogramm) und LLM-Analyse.
- Baue ein Dropdown, um zwischen Umsatzdiagramm und Altersdiagramm zu wechseln.
- Füge eine Funktion hinzu: „Vergleiche Männer vs. Frauen im Einkommen“.

### Lösungen

```python
# Histogramm
fig, ax = plt.subplots()
df["Age"].hist(ax=ax)
st.pyplot(fig)

# Auswahl
chart = st.selectbox("Diagramm wählen", ["Umsatz", "Alter"])
if chart == "Umsatz":
    df["Sales"].plot(kind="bar")
else:
    df["Age"].hist()

# Geschlechtervergleich
male = df[df["Gender"] == "Male"]
female = df[df["Gender"] == "Female"]
prompt = f"Vergleiche Einkommen von Männern und Frauen:\n{male.describe()}\n{female.describe()}"
```

---

## Einheit 4.4 — Deployment

### Beispiele

#### Beispiel 1 — App starten

```bash
streamlit run app.py
```

#### Beispiel 2 — requirements.txt

```
streamlit
pandas
requests
matplotlib
```

#### Beispiel 3 — Dockerfile

```dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Beispiel 4 — Deployment mit Docker

```bash
docker build -t myapp .
docker run -p 8501:8501 myapp
```

### Übungen

- Erstelle requirements.txt für deine eigene App.
- Baue ein Docker-Image und starte es lokal.
- Starte die App auf Streamlit Cloud (GitHub → Streamlit Cloud).

### Lösungen

```text
# requirements.txt
streamlit
pandas
requests

# Docker
docker build -t meine-app .
docker run -p 8501:8501 meine-app
```

---

## Einheit 4.5 — Bonus: Q&A über mehrere Datenquellen

### Beispiele

#### Beispiel 1 — CSV + FAQ

```python
faq = "Q: Was ist KI? A: Maschinen, die wie Menschen denken."
stats = df.describe().to_string()
prompt = f"""Beantworte die Frage basierend auf diesen Quellen:
FAQ: {faq}
CSV-Daten: {stats}
Frage: Was ist das Durchschnittsalter?"""
```

#### Beispiel 2 — CSV + Textdokument

```python
doc = open("info.txt").read()
prompt = f"""Verwende CSV + Dokument:
CSV: {df.describe().to_string()}
Dokument: {doc}
Frage: Welche Erkenntnisse gibt es?"""
```

### Übungen

- Lade eine CSV mit Kundendaten und kombiniere sie mit einer FAQ-Datei.
- Schreibe eine App, die beide Quellen gleichzeitig analysiert.
- Stelle die Frage: „Welche Stadt hat den höchsten Umsatz und wie passt das zu den FAQ-Daten?“

### Lösungen

```python
faq = open("faq.txt").read()
stats = df.describe().to_string()
frage = "Welche Stadt hat den höchsten Umsatz und wie passt das zu den FAQ-Daten?"

prompt = f"""FAQ: {faq}
CSV: {stats}
Frage: {frage}"""
```

---

## Zusammenfassung Tag 4 (erweitert)

Nach Tag 4 können Studierende:

- CSV/Excel mit Pandas verarbeiten
- LLMs für Q&A über Daten nutzen
- Dashboards mit Diagrammen + KI-Kommentaren bauen
- Apps deployen (Streamlit Cloud, Docker)
- Mehrere Datenquellen kombinieren
