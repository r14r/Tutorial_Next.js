# Tag 4 — Fortgeschrittene Anwendungen mit LLMs & Daten

## 📅 Zeitplan 09:00 – 15:00

### Übersicht

Der Tag vertieft fortgeschrittene Anwendungen mit LLMs und Datenintegration. Jede Einheit enthält kurze Erklärungen, praktische Beispiele und Übungen.

---

### Zeitplan

| Zeit            | Einheit / Inhalt                                                                 | Dauer   |
|-----------------|----------------------------------------------------------------------------------|---------|
| **09:00 – 09:20** | Einführung & Überblick - Motivation, Ziele des Tages           | 20 min  |
| **09:20 – 10:05** | **Einheit 4.1:** Datenintegration mit Pandas - CSV/Excel laden, filtern, LLM-Integration | 45 min  |
| **10:05 – 10:35** | **Einheit 4.2:** Q&A über CSV-Dateien - Abfragen, LLM-Antworten, Streamlit-App | 30 min  |
| **10:35 – 11:15** | **Einheit 4.3:** KI-Dashboards mit Streamlit - Diagramme, LLM-Kommentare, Gruppenvergleich | 40 min  |
| **11:15 – 11:30** | ☕ **Pause**                                                                    | 15 min  |
| **11:30 – 12:10** | **Einheit 4.4:** Deployment - App starten, requirements.txt, Docker, Streamlit Cloud | 40 min  |
| **12:10 – 12:40** | **Einheit 4.5:** Bonus: Q&A über mehrere Datenquellen - CSV + FAQ/Text, kombinierte Analyse | 30 min  |
| **12:40 – 13:10** | Übungen & Praxis - Eigene Datenquellen, Mini-Projekt starten   | 30 min  |
| **13:10 – 14:10** | 🍽️ **Mittagspause**                                                            | 60 min  |
| **14:10 – 14:40** | Mini-Projekt & Präsentation - App mit mehreren Datenquellen, Q&A, Dashboard | 30 min  |
| **14:40 – 15:00** | Zusammenfassung & Ausblick - Reflexion, nächste Schritte        | 20 min  |

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

## Einheit 1 — Datenintegration mit Pandas

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

#### Beispiel 1 — CSV laden

```python
# Datei: einheit41_csv_laden.py
import pandas as pd
df = pd.read_csv("sales.csv")
print(df.head())
```

#### Beispiel 2 — Excel laden

```python
# Datei: einheit41_excel_laden.py
import pandas as pd
df = pd.read_excel("data.xlsx")
print(df.shape)
```

#### Beispiel 3 — Filterung

```python
# Datei: einheit41_filterung.py
import pandas as pd
df = pd.read_csv("sales.csv")
kunden = df[df["Country"] == "Germany"]
print(kunden)
```

#### Beispiel 4 — LLM-Integration mit Ollama SDK

```python
# Datei: einheit41_llm_integration.py
import pandas as pd
from lib.helper_ollama import ollama

df = pd.read_csv("sales.csv")
stats = df.describe().to_string()
prompt = f"Analysiere die Verkaufsdaten:\n{stats}"
result = ollama.generate(prompt)
print(result)
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

## Einheit 2 — Q&A über CSV-Dateien

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

#### Beispiel 1 — Einfache Abfrage

```python
# Datei: einheit42_einfache_abfrage.py
import pandas as pd
df = pd.read_csv("kunden.csv")
frage = "Wie viele Kunden sind älter als 30?"
antwort = len(df[df["Alter"] > 30])
print(antwort)
```

#### Beispiel 2 — Antwort mit LLM (Ollama SDK)

```python
# Datei: einheit42_llm_antwort.py
import pandas as pd
from lib.helper_ollama import ollama

df = pd.read_csv("kunden.csv")
stats = df.describe().to_string()
prompt = f"Beantworte die Frage basierend auf diesen Daten:\n{stats}\nFrage: Wie viele Kunden sind älter als 30?"
result = ollama.generate(prompt)
print(result)
```

#### Beispiel 3 — Streamlit-App mit Ollama SDK

```python
# Datei: einheit42_streamlit_app.py
import streamlit as st
import pandas as pd
from lib.helper_ollama import ollama

file = st.file_uploader("CSV hochladen", type="csv")
if file:
    df = pd.read_csv(file)
    frage = st.text_input("Frage:")
    if frage:
        stats = df.describe().to_string()
        prompt = f"{frage}\nDaten:\n{stats}"
        result = ollama.generate(prompt)
        st.write("Antwort:", result)
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

## Einheit 3 — KI-Dashboards mit Streamlit

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

#### Beispiel 1 — Balkendiagramm (Streamlit)

```python
# Datei: einheit43_balkendiagramm.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
fig, ax = plt.subplots()
df["Sales"].plot(kind="bar", ax=ax)
st.pyplot(fig)
```

#### Beispiel 2 — Histogramm (Streamlit)

```python
# Datei: einheit43_histogramm.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
fig, ax = plt.subplots()
df["Age"].hist(ax=ax, bins=10)
st.pyplot(fig)
```

#### Beispiel 3 — LLM-Kommentar (Ollama SDK)

```python
# Datei: einheit43_llm_kommentar.py
import pandas as pd
from lib.helper_ollama import ollama

df = pd.read_csv("sales.csv")
stats = df.describe().to_string()
prompt = f"Erkläre die wichtigsten Trends:\n{stats}"
result = ollama.generate(prompt)
print(result)
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

## Einheit 4 — Deployment

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

#### Beispiel 1 — App starten

```bash
streamlit run app.py
```

#### Beispiel 2 — requirements.txt

```text
streamlit
pandas
matplotlib
5—Capstone-Projekte.ai-content-studio_1.lib.ollama
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

## Einheit 5 — Bonus: Q&A über mehrere Datenquellen

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

#### Beispiel 1 — CSV + FAQ (Ollama SDK)

```python
# Datei: einheit45_csv_faq.py
import pandas as pd
from lib.helper_ollama import ollama

df = pd.read_csv("kunden.csv")
faq = "Q: Was ist KI? A: Maschinen, die wie Menschen denken."
stats = df.describe().to_string()
prompt = f"Beantworte die Frage basierend auf diesen Quellen:\nFAQ: {faq}\nCSV-Daten: {stats}\nFrage: Was ist das Durchschnittsalter?"
result = ollama.generate(prompt)
print(result)
```

#### Beispiel 2 — CSV + Textdokument (Ollama SDK)

```python
# Datei: einheit45_csv_text.py
import pandas as pd
from lib.helper_ollama import ollama

df = pd.read_csv("kunden.csv")
doc = open("info.txt").read()
prompt = f"Verwende CSV + Dokument:\nCSV: {df.describe().to_string()}\nDokument: {doc}\nFrage: Welche Erkenntnisse gibt es?"
result = ollama.generate(prompt)
print(result)
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

## Einheit 6 - Zusammenfassung

Nach Tag 4 können Studierende:

- CSV/Excel mit Pandas verarbeiten
- LLMs für Q&A über Daten nutzen
- Streamlit-Apps für Datenanalyse erstellen
- CSV-Daten in natürlicher Sprache abfragen
- mehrere Datenquellen kombinieren
- Apps mit Docker containerisieren
- Apps auf Streamlit Cloud deployen

---

## Einheit 7 - Mini-Projekte

### Mini-Projekt 1: Intelligenter Business Intelligence Dashboard

**Aufgabe:** Baue ein Dashboard, das Unternehmensdaten analysiert und Geschäftsempfehlungen gibt.

**Lösung:**

```python
import streamlit as st
import pandas as pd
import plotly.express as px
from lib.helper_ollama import ollama

st.title("Business Intelligence Dashboard")

# Daten hochladen
uploaded_file = st.file_uploader("Geschäftsdaten (CSV) hochladen", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Grundlegende Visualisierung
    st.subheader("Datenübersicht")
    st.dataframe(df.head())
    
    # Automatische Diagramme
    if st.button("Automatische Visualisierung"):
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        if len(numeric_cols) >= 2:
            fig = px.scatter(df, x=numeric_cols[0], y=numeric_cols[1])
            st.plotly_chart(fig)
    
    # KI-basierte Analyse
    st.subheader("KI-Geschäftsanalyse")
    analyse_typ = st.selectbox("Analyse-Typ:", 
                              ["Umsatztrends", "Kundenverhalten", "Kostenoptimierung", "Marktchancen"])
    
    if st.button("Analysieren"):
        stats = df.describe().to_string()
        
        if analyse_typ == "Umsatztrends":
            prompt = f"Analysiere diese Geschäftsdaten und identifiziere Umsatztrends. Gib konkrete Empfehlungen:\n{stats}"
        elif analyse_typ == "Kundenverhalten":
            prompt = f"Analysiere das Kundenverhalten basierend auf diesen Daten:\n{stats}"
        elif analyse_typ == "Kostenoptimierung":
            prompt = f"Identifiziere Kostenoptimierungsmöglichkeiten in diesen Daten:\n{stats}"
        else:
            prompt = f"Identifiziere neue Marktchancen basierend auf diesen Daten:\n{stats}"
        
        result = ollama.generate(prompt)
        st.write("**KI-Empfehlungen:**", result)
```

### Mini-Projekt 2: Automatischer Report Generator

**Aufgabe:** Generiere automatisch Berichte aus verschiedenen Datenquellen.

**Lösung:**

```python
import streamlit as st
import pandas as pd
from datetime import datetime
from lib.helper_ollama import ollama

st.title("Automatischer Report Generator")

# Multiple Datenquellen
st.subheader("Datenquellen hinzufügen")
files = st.file_uploader("CSV-Dateien hochladen", type="csv", accept_multiple_files=True)

if files:
    data_summaries = []
    
    for i, file in enumerate(files):
        df = pd.read_csv(file)
        st.write(f"**Datei {i+1}: {file.name}**")
        st.write(f"Shape: {df.shape}")
        
        # Kurze Statistik
        summary = f"Datei: {file.name}\nZeilen: {df.shape[0]}\nSpalten: {df.shape[1]}\nStatistik:\n{df.describe().to_string()}"
        data_summaries.append(summary)
    
    # Report-Typ wählen
    report_typ = st.selectbox("Report-Typ:", 
                             ["Executive Summary", "Detailanalyse", "Vergleichsbericht", "Trend-Report"])
    
    if st.button("Report generieren"):
        all_data = "\n\n".join(data_summaries)
        
        prompt = f"""Erstelle einen professionellen {report_typ} basierend auf folgenden Daten:

{all_data}

Der Report soll enthalten:
1. Management Summary
2. Wichtigste Erkenntnisse
3. Empfehlungen
4. Risiken und Chancen
5. Nächste Schritte

Format: Professioneller Geschäftsbericht"""
        
        result = ollama.generate(prompt)
        
        st.subheader(f"{report_typ} - {datetime.now().strftime('%d.%m.%Y')}")
        st.write(result)
        
        # Download-Button
        st.download_button(
            label="Report als Textdatei herunterladen",
            data=result,
            file_name=f"report_{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain"
        )
```

### Mini-Projekt 3: Smart Data Query Interface

**Aufgabe:** Ermögliche natürlichsprachliche Abfragen auf strukturierte Daten.

**Lösung:**

```python
import streamlit as st
import pandas as pd
import sqlite3
from lib.helper_ollama import ollama

st.title("Smart Data Query Interface")

# Daten laden
uploaded_file = st.file_uploader("CSV-Datei hochladen", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("**Datenvorschau:**")
    st.dataframe(df.head())
    
    # Spaltennamen anzeigen
    st.write("**Verfügbare Spalten:**", ", ".join(df.columns.tolist()))
    
    # Natürlichsprachliche Abfrage
    st.subheader("Stelle eine Frage zu den Daten")
    question = st.text_input("Frage (z.B. 'Was ist der Durchschnittswert der Spalte X?'):")
    
    if st.button("Abfrage ausführen") and question:
        # Erst KI nach SQL-Query fragen
        schema_info = f"Tabelle mit Spalten: {', '.join(df.columns)}\nDatentypen: {df.dtypes.to_string()}"
        
        sql_prompt = f"""Konvertiere diese natürlichsprachliche Frage in eine SQL-Query:

Schema: {schema_info}
Frage: {question}

Gib nur die SQL-Query zurück, ohne Erklärung:"""
        
        sql_query = ollama.generate(sql_prompt).strip()
        st.write("**Generierte SQL-Query:**", sql_query)
        
        try:
            # SQL ausführen (vereinfacht mit pandas)
            # In Realität würde man eine echte SQL-Engine verwenden
            conn = sqlite3.connect(':memory:')
            df.to_sql('data', conn, index=False)
            
            result_df = pd.read_sql_query(sql_query.replace('data', 'data'), conn)
            st.write("**Ergebnis:**")
            st.dataframe(result_df)
            
        except Exception as e:
            st.error(f"Fehler bei SQL-Ausführung: {e}")
            
            # Fallback: Direkte Antwort von KI
            fallback_prompt = f"""Beantworte diese Frage basierend auf den Daten:

Datenstatistik: {df.describe().to_string()}
Spalten: {df.columns.tolist()}
Frage: {question}"""
            
            fallback_result = ollama.generate(fallback_prompt)
            st.write("**KI-Antwort:**", fallback_result)
```

### Mini-Projekt 4: Multi-Source Data Fusion

**Aufgabe:** Kombiniere und analysiere Daten aus verschiedenen Quellen intelligent.

**Lösung:**

```python
import streamlit as st
import pandas as pd
import json
from lib.helper_ollama import ollama

st.title("Multi-Source Data Fusion")

st.write("Lade verschiedene Datenquellen und lasse sie von der KI intelligent kombinieren.")

# Verschiedene Datentypen
col1, col2 = st.columns(2)

with col1:
    st.subheader("Strukturierte Daten")
    csv_file = st.file_uploader("CSV-Datei", type="csv")
    
with col2:
    st.subheader("Unstrukturierte Daten")
    text_file = st.file_uploader("Text-Datei", type="txt")

# JSON-Eingabe
json_text = st.text_area("JSON-Daten (optional):")

# Kombinationsanalyse
if csv_file or text_file or json_text:
    sources = []
    
    if csv_file:
        df = pd.read_csv(csv_file)
        csv_summary = f"CSV-Daten:\nShape: {df.shape}\nSpalten: {df.columns.tolist()}\nStatistik:\n{df.describe().to_string()}"
        sources.append(csv_summary)
        st.write("**CSV geladen:**", df.shape)
    
    if text_file:
        text_content = text_file.read().decode()
        text_summary = f"Text-Daten:\nLänge: {len(text_content)} Zeichen\nInhalt (Auszug): {text_content[:500]}..."
        sources.append(text_summary)
        st.write("**Text geladen:**", len(text_content), "Zeichen")
    
    if json_text:
        try:
            json_data = json.loads(json_text)
            json_summary = f"JSON-Daten:\nStruktur: {json.dumps(json_data, indent=2)[:500]}..."
            sources.append(json_summary)
            st.write("**JSON geparst:** ✅")
        except:
            st.warning("JSON nicht valid")
    
    # Fusion und Analyse
    if st.button("Daten fusionieren und analysieren") and sources:
        fusion_prompt = f"""Analysiere und kombiniere diese verschiedenen Datenquellen intelligent:

{chr(10).join(sources)}

Aufgaben:
1. Identifiziere Verbindungen zwischen den Datenquellen
2. Finde Muster und Trends
3. Erkenne Widersprüche oder Anomalien
4. Gib zusammenfassende Insights
5. Empfehle weitere Analyseschritte

Antwort als strukturierter Bericht:"""
        
        result = ollama.generate(fusion_prompt)
        st.subheader("Fusionsanalyse")
        st.write(result)
        
        # Zusätzlich: Spezifische Fragen stellen
        custom_question = st.text_input("Spezifische Frage zu den kombinierten Daten:")
        if st.button("Frage stellen") and custom_question:
            question_prompt = f"Beantworte diese Frage basierend auf allen Datenquellen:\n\n{chr(10).join(sources)}\n\nFrage: {custom_question}"
            answer = ollama.generate(question_prompt)
            st.write("**Antwort:**", answer)
```

### Mini-Projekt 5: Predictive Analytics Interface

**Aufgabe:** Nutze KI für einfache Vorhersagen und Trends basierend auf historischen Daten.

**Lösung:**

```python
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
from lib.helper_ollama import ollama

st.title("Predictive Analytics Interface")

uploaded_file = st.file_uploader("Zeitreihen-Daten (CSV) hochladen", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Datenvorschau")
    st.dataframe(df.head())
    
    # Spalten für Analyse auswählen
    date_col = st.selectbox("Datums-Spalte:", df.columns)
    value_col = st.selectbox("Wert-Spalte:", df.select_dtypes(include=['float64', 'int64']).columns)
    
    if date_col and value_col:
        # Daten vorbereiten
        try:
            df[date_col] = pd.to_datetime(df[date_col])
            df_sorted = df.sort_values(date_col)
            
            # Visualisierung
            fig = px.line(df_sorted, x=date_col, y=value_col, title="Zeitreihen-Verlauf")
            st.plotly_chart(fig)
            
            # Vorhersage-Parameter
            col1, col2 = st.columns(2)
            with col1:
                prediction_days = st.slider("Vorhersage für X Tage:", 1, 90, 30)
            with col2:
                confidence_level = st.selectbox("Konfidenz-Level:", ["Niedrig", "Mittel", "Hoch"])
            
            if st.button("Vorhersage generieren"):
                # Datenanalyse für KI
                recent_data = df_sorted.tail(20)
                data_summary = f"""
Letzte 20 Datenpunkte:
{recent_data[[date_col, value_col]].to_string()}

Statistiken:
- Mittelwert: {df[value_col].mean():.2f}
- Standardabweichung: {df[value_col].std():.2f}
- Trend (letzte 5 vs vorherige 5): {recent_data[value_col].tail(5).mean() - recent_data[value_col].head(5).mean():.2f}
- Min: {df[value_col].min():.2f}
- Max: {df[value_col].max():.2f}
"""
                
                prediction_prompt = f"""Analysiere diese Zeitreihen-Daten und gib eine Vorhersage für die nächsten {prediction_days} Tage:

{data_summary}

Aufgaben:
1. Identifiziere Trends und Muster
2. Schätze wahrscheinliche Werte für die nächsten {prediction_days} Tage
3. Erkenne Saisonalität oder Zyklen
4. Bewerte Risiken und Unsicherheiten
5. Gib konkrete Zahlenwerte als Prognose

Konfidenz-Level: {confidence_level}

Format die Antwort als:
- Trend-Analyse
- Vorhersage (numerische Werte)
- Konfidenz-Bewertung
- Einflussfaktoren
- Empfehlungen"""
                
                prediction = ollama.generate(prediction_prompt)
                
                st.subheader(f"Vorhersage für {prediction_days} Tage")
                st.write(prediction)
                
                # Zusätzlich: What-If Szenarien
                st.subheader("What-If Analyse")
                scenario = st.text_input("Beschreibe ein Szenario (z.B. '20% Umsatzsteigerung'):")
                
                if st.button("Szenario analysieren") and scenario:
                    scenario_prompt = f"""Analysiere dieses What-If Szenario basierend auf den historischen Daten:

Historische Daten: {data_summary}
Szenario: {scenario}

Wie würde sich das auf die Vorhersage auswirken? Gib konkrete Zahlen und Wahrscheinlichkeiten."""
                    
                    scenario_result = ollama.generate(scenario_prompt)
                    st.write("**Szenario-Analyse:**", scenario_result)
                    
        except Exception as e:
            st.error(f"Fehler bei der Datenverarbeitung: {e}")
```

- Dashboards mit Diagrammen + KI-Kommentaren bauen
- Apps deployen (Streamlit Cloud, Docker)
- Mehrere Datenquellen kombinieren
