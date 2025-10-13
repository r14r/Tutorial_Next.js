# Day 4 — Advanced Applications with LLMs & Data

## 📅 ​​Schedule 09:00 - 15:00

### Overview

The day delves into advanced applications with LLMs and data integration. Each unit contains short explanations, practical examples and exercises.

---

### Schedule

| time | Unit / Content | Duration |
|-----------------|---------------------------------------------------------------------------------|---------|
| **09:00 – 09:20** | Introduction & Overview - Motivation, Goals of the Day | 20 mins |
| **09:20 – 10:05** | **Unit 4.1:** Data integration with Pandas - CSV/Excel loading, filtering, LLM integration | 45 mins |
| **10:05 – 10:35** | **Unit 4.2:** Q&A about CSV files - Queries, LLM answers, Streamlit app | 30 mins |
| **10:35 – 11:15** | **Unit 4.3:** AI Dashboards with Streamlit - Charts, LLM Comments, Group Comparison | 40 mins |
| **11:15 – 11:30** | ☕ **Break** | 15 mins |
| **11:30 – 12:10** | **Unit 4.4:** Deployment - Start app, requirements.txt, Docker, Streamlit Cloud | 40 mins |
| **12:10 – 12:40** | **Unit 4.5:** Bonus: Q&A across multiple data sources - CSV + FAQ/Text, combined analysis | 30 mins |
| **12:40 – 1:10 pm** | Exercises & Practice - Own data sources, start mini-project | 30 mins |
| **13:10 – 14:10** | 🍽️ **Lunch break** | 60 mins |
| **14:10 – 14:40** | Mini Project & Presentation - App with multiple data sources, Q&A, Dashboard | 30 mins |
| **14:40 – 15:00** | Summary & outlook - reflection, next steps | 20 mins |

---

## Unit expiry

- **Explanation:** approx. 10-15 min
- **Examples:** approx. 10 min
- **Exercises:** approx. 15-20 min  
    → Exercises are carried out directly in Jupyter, VS Code or Streamlit.

---

## Mini Project (2:10 p.m. - 2:40 p.m.)

At the end of the day, an app is developed that combines the following features:

- **CSV upload**
- **FAQ/Text Upload**
- **Processing:** Data analysis with Pandas and LLM
- **Dashboard:** Charts, AI comments
- **Q&A:** Questions about combined data sources

---

## Unit 1 — Data Integration with Pandas

### Examples

#### Example 1 — Load CSV

```python
import pandas as pd
df = pd.read_csv("sales.csv")
print(df.head())
```
#### Example 2 — Load Excel

```python
df = pd.read_excel("data.xlsx")
print(df.shape)
```
#### Example 3 — Filtering

```python
kunden = df[df["Country"] == "Germany"]
print(kunden)
```
#### Example 4 — LLM integration

```python
import requests
stats = df.describe().to_string()
prompt = f"Analysiere die Verkaufsdaten:\n{stats}"
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": prompt})
print(r.json()["response"])
```
#### Example 1 — Load CSV

```python
# Datei: einheit41_csv_laden.py
import pandas as pd
df = pd.read_csv("sales.csv")
print(df.head())
```
#### Example 2 — Load Excel

```python
# Datei: einheit41_excel_laden.py
import pandas as pd
df = pd.read_excel("data.xlsx")
print(df.shape)
```
#### Example 3 — Filtering

```python
# Datei: einheit41_filterung.py
import pandas as pd
df = pd.read_csv("sales.csv")
kunden = df[df["Country"] == "Germany"]
print(kunden)
```
#### Example 4 — LLM integration with Ollama SDK

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
### Exercises

- Load a CSV with columns Name, Age, Income. Calculate the median income.
- Filter all customers over 40 years old.
- Send the statistics to Ollama and ask for an economic interpretation.
- Sort customers in descending order by income.

### Solutions

```python
df = pd.read_csv("kunden.csv")
print(df["Einkommen"].median())
print(df[df["Alter"] > 40])
stats = df.describe().to_string()
prompt = f"Welche wirtschaftlichen Trends lassen sich erkennen?\n{stats}"
print(df.sort_values("Einkommen", ascending=False))
```
---

## Unit 2 — Q&A about CSV files

### Examples

#### Example 1 — Simple Query

```python
frage = "Wie viele Kunden sind älter als 30?"
antwort = len(df[df["Alter"] > 30])
print(antwort)
```
#### Example 2 — Answer with LLM

```python
stats = df.describe().to_string()
prompt = f"""Beantworte die Frage basierend auf diesen Daten:
{stats}
Frage: Wie viele Kunden sind älter als 30?"""
```
#### Example 3 — Streamlit app

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
#### Example 1 — Simple Query

```python
# Datei: einheit42_einfache_abfrage.py
import pandas as pd
df = pd.read_csv("kunden.csv")
frage = "Wie viele Kunden sind älter als 30?"
antwort = len(df[df["Alter"] > 30])
print(antwort)
```
#### Example 2 — Reply with LLM (Ollama SDK)

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
#### Example 3 — Streamlit app with Ollama SDK

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
### Exercises

- Implement: “How many different cities are there in the CSV?”
- Write a function `answer_question(df, question)` that combines pandas + Ollama.
- Test the question: “Which customer has the highest income?”

### Solutions

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

## Unit 3 — AI Dashboards with Streamlit

### Examples

#### Example 1 — Bar Chart

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
df["Sales"].plot(kind="bar", ax=ax)
st.pyplot(fig)
```
#### Example 2 — Histogram

```python
fig, ax = plt.subplots()
df["Age"].hist(ax=ax, bins=10)
st.pyplot(fig)
```
#### Example 3 — LLM comment

```python
stats = df.describe().to_string()
prompt = f"Erkläre die wichtigsten Trends:\n{stats}"
```
#### Example 1 — Bar Chart (Streamlit)

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
#### Example 2 — Histogram (Streamlit)

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
#### Example 3 — LLM Comment (Ollama SDK)

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
#### Example 4 — Comparison of two groups

```python
city1, city2 = "Berlin", "Hamburg"
df1 = df[df["City"] == city1]
df2 = df[df["City"] == city2]
prompt = f"Vergleiche {city1} und {city2}:\n{df1.describe().to_string()}\n{df2.describe().to_string()}"
```
### Exercises

- Create a dashboard with age distribution (histogram) and LLM analysis.
- Build a dropdown to switch between sales chart and age chart.
- Add a feature: “Compare men vs. women in income”.

### Solutions

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

## Unit 4 — Deployment

### Examples

#### Example 1 — Start the app

```bash
streamlit run app.py
```
#### Example 2 — requirements.txt

```
streamlit
pandas
requests
matplotlib
```
#### Example 3 — Dockerfile

```dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```
#### Example 4 — Deployment with Docker

```bash
docker build -t myapp .
docker run -p 8501:8501 myapp
```
#### Example 1 — Start the app

```bash
streamlit run app.py
```
#### Example 2 — requirements.txt

```text
streamlit
pandas
matplotlib
5—Capstone-Projekte.ai-content-studio_1.lib.ollama
```
#### Example 3 — Dockerfile

```dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```
#### Example 4 — Deployment with Docker

```bash
docker build -t myapp .
docker run -p 8501:8501 myapp
```
### Exercises

- Create requirements.txt for your own app.
- Build a Docker image and run it locally.
- Start the app on Streamlit Cloud (GitHub → Streamlit Cloud).

### Solutions

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

## Unit 5 — Bonus: Q&A across multiple data sources

### Examples

#### Example 1 — CSV + FAQ

```python
faq = "Q: Was ist KI? A: Maschinen, die wie Menschen denken."
stats = df.describe().to_string()
prompt = f"""Beantworte die Frage basierend auf diesen Quellen:
FAQ: {faq}
CSV-Daten: {stats}
Frage: Was ist das Durchschnittsalter?"""
```
#### Example 2 — CSV + text document

```python
doc = open("info.txt").read()
prompt = f"""Verwende CSV + Dokument:
CSV: {df.describe().to_string()}
Dokument: {doc}
Frage: Welche Erkenntnisse gibt es?"""
```
#### Example 1 — CSV + FAQ (Ollama SDK)

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
#### Example 2 — CSV + Text Document (Ollama SDK)

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
### Exercises

- Load a CSV with customer data and combine it with an FAQ file.
- Write an app that analyzes both sources at the same time.
- Ask the question: “Which city has the highest sales and how does that fit with the FAQ data?”

### Solutions

```python
faq = open("faq.txt").read()
stats = df.describe().to_string()
frage = "Welche Stadt hat den höchsten Umsatz und wie passt das zu den FAQ-Daten?"

prompt = f"""FAQ: {faq}
CSV: {stats}
Frage: {frage}"""
```
---

## Unit 6 - Summary

After Day 4, students can:

- Process CSV/Excel with Pandas
- Use LLMs for Q&A about data
- Build Streamlit apps for data analysis
- Query CSV data in natural language
- combine multiple data sources
- Containerize apps with Docker
- Deploy apps on Streamlit Cloud

---

## Unit 7 - Mini Projects

### Mini Project 1: Intelligent Business Intelligence Dashboard

**Task:** Build a dashboard that analyzes company data and provides business recommendations.

**Solution:**

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
### Mini Project 2: Automatic Report Generator

**Task:** Automatically generate reports from various data sources.

**Solution:**

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
### Mini Project 3: Smart Data Query Interface

**Task:** Enable natural language queries on structured data.

**Solution:**

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
### Mini Project 4: Multi-Source Data Fusion

**Task:** Intelligently combine and analyze data from different sources.

**Solution:**

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
### Mini Project 5: Predictive Analytics Interface

**Mission:** Use AI for simple predictions and trends based on historical data.

**Solution:**

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
- Build dashboards with charts + AI comments
- Deploy apps (Streamlit Cloud, Docker)
- Combine multiple data sources