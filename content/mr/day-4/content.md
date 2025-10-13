# दिवस 4 - एलएलएम आणि डेटासह प्रगत अनुप्रयोग

## 📅 ​​वेळापत्रक 09:00 - 15:00

### विहंगावलोकन

दिवस एलएलएम आणि डेटा एकत्रीकरणासह प्रगत अनुप्रयोगांमध्ये प्रवेश करतो. प्रत्येक युनिटमध्ये लहान स्पष्टीकरण, व्यावहारिक उदाहरणे आणि व्यायाम असतात.

-

### वेळापत्रक

| वेळ | युनिट / सामग्री | कालावधी |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------
| ** 09: 00 - 09: 20 ** | परिचय आणि विहंगावलोकन - प्रेरणा, दिवसाची उद्दीष्टे | 20 मिनिटे |
| ** 09: 20 - 10: 05 ** | ** युनिट 1.१: ** पांडासह डेटा एकत्रीकरण - सीएसव्ही/एक्सेल लोडिंग, फिल्टरिंग, एलएलएम एकत्रीकरण | 45 मिनिटे |
| ** 10: 05 - 10: 35 ** | ** युनिट 2.२: ** सीएसव्ही फायलींबद्दल प्रश्नोत्तर - क्वेरी, एलएलएम उत्तरे, प्रवाह अ‍ॅप | 30 मिनिटे |
| ** 10: 35 - 11: 15 ** | ** युनिट 3.3: ** प्रवाहासह एआय डॅशबोर्ड्स - चार्ट, एलएलएम टिप्पण्या, गट तुलना | 40 मिनिटे |
| ** 11: 15 - 11: 30 ** | ☕ ** ब्रेक ** | 15 मिनिटे |
| ** 11: 30 - 12: 10 ** | ** युनिट 4.4: ** उपयोजन - अॅप, आवश्यकता. 40 मिनिटे |
| ** 12: 10 - 12: 40 ** | ** युनिट 4.5. :: ** बोनस: एकाधिक डेटा स्रोतांमध्ये प्रश्नोत्तर - सीएसव्ही + सामान्य प्रश्न/मजकूर, एकत्रित विश्लेषण | 30 मिनिटे |
| ** 12: 40 - 1:10 दुपारी ** | व्यायाम आणि सराव - स्वतःचा डेटा स्रोत, मिनी -प्रोजेक्ट प्रारंभ करा | 30 मिनिटे |
| ** 13: 10 - 14: 10 ** | 🍽 ** लंच ब्रेक ** | 60 मिनिटे |
| ** 14: 10 - 14: 40 ** | मिनी प्रकल्प आणि सादरीकरण - एकाधिक डेटा स्रोतांसह अॅप, प्रश्नोत्तर, डॅशबोर्ड | 30 मिनिटे |
| ** 14: 40 - 15: 00 ** | सारांश आणि दृष्टीकोन - प्रतिबिंब, पुढील चरण | 20 मिनिटे |

-

## युनिट एक्सपायरी

- ** स्पष्टीकरण: ** अंदाजे. 10-15 मि
- ** उदाहरणे: ** अंदाजे. 10 मि
- ** व्यायाम: ** अंदाजे. 15-20 मि  
    Ex व्यायाम थेट ज्युपिटर, वि कोड किंवा प्रवाहामध्ये केला जातो.

-

## मिनी प्रकल्प (2:10 p.m. - 2:40 p.m.)

दिवसाच्या शेवटी, एक अॅप विकसित केला जातो जो खालील वैशिष्ट्ये एकत्रित करतो:

- ** सीएसव्ही अपलोड **
- ** FAQ/मजकूर अपलोड **
- ** प्रक्रिया: ** पांडास आणि एलएलएमसह डेटा विश्लेषण
- ** डॅशबोर्ड: ** चार्ट, एआय टिप्पण्या
- ** प्रश्नोत्तर: ** एकत्रित डेटा स्रोतांबद्दलचे प्रश्न

-

## युनिट 1 - पांडासह डेटा एकत्रीकरण

### उदाहरणे

#### उदाहरण 1 - सीएसव्ही लोड करा

```python
import pandas as pd
df = pd.read_csv("sales.csv")
print(df.head())
```
#### उदाहरण 2 - लोड एक्सेल

```python
df = pd.read_excel("data.xlsx")
print(df.shape)
```
#### उदाहरण 3 - फिल्टरिंग

```python
kunden = df[df["Country"] == "Germany"]
print(kunden)
```
#### उदाहरण 4 - एलएलएम एकत्रीकरण

```python
import requests
stats = df.describe().to_string()
prompt = f"Analysiere die Verkaufsdaten:\n{stats}"
r = requests.post("http://localhost:11434/api/generate",
                  json={"model": "llama2", "prompt": prompt})
print(r.json()["response"])
```
#### उदाहरण 1 - सीएसव्ही लोड करा

```python
# Datei: einheit41_csv_laden.py
import pandas as pd
df = pd.read_csv("sales.csv")
print(df.head())
```
#### उदाहरण 2 - लोड एक्सेल

```python
# Datei: einheit41_excel_laden.py
import pandas as pd
df = pd.read_excel("data.xlsx")
print(df.shape)
```
#### उदाहरण 3 - फिल्टरिंग

```python
# Datei: einheit41_filterung.py
import pandas as pd
df = pd.read_csv("sales.csv")
kunden = df[df["Country"] == "Germany"]
print(kunden)
```
#### उदाहरण 4 - ओलामा एसडीकेसह एलएलएम एकत्रीकरण

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
### व्यायाम

- स्तंभांचे नाव, वय, उत्पन्नासह सीएसव्ही लोड करा. मध्यम उत्पन्नाची गणना करा.
- 40 वर्षांपेक्षा जास्त वयाच्या सर्व ग्राहकांना फिल्टर करा.
- आकडेवारी ओल्लामाला पाठवा आणि आर्थिक व्याख्या विचारा.
- उत्पन्नाद्वारे खाली उतरत्या ऑर्डरमध्ये ग्राहकांची क्रमवारी लावा.

### सोल्यूशन्स

```python
df = pd.read_csv("kunden.csv")
print(df["Einkommen"].median())
print(df[df["Alter"] > 40])
stats = df.describe().to_string()
prompt = f"Welche wirtschaftlichen Trends lassen sich erkennen?\n{stats}"
print(df.sort_values("Einkommen", ascending=False))
```
-

## युनिट 2 - सीएसव्ही फायलींबद्दल प्रश्नोत्तर

### उदाहरणे

#### उदाहरण 1 - सोपी क्वेरी

```python
frage = "Wie viele Kunden sind älter als 30?"
antwort = len(df[df["Alter"] > 30])
print(antwort)
```
#### उदाहरण 2 - एलएलएम सह उत्तर

```python
stats = df.describe().to_string()
prompt = f"""Beantworte die Frage basierend auf diesen Daten:
{stats}
Frage: Wie viele Kunden sind älter als 30?"""
```
#### उदाहरण 3 - प्रवाह अॅप

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
#### उदाहरण 1 - सोपी क्वेरी

```python
# Datei: einheit42_einfache_abfrage.py
import pandas as pd
df = pd.read_csv("kunden.csv")
frage = "Wie viele Kunden sind älter als 30?"
antwort = len(df[df["Alter"] > 30])
print(antwort)
```
#### उदाहरण 2 - एलएलएमसह प्रत्युत्तर द्या (ओलामा एसडीके)

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
#### उदाहरण 3 - ओलामा एसडीकेसह प्रवाह अॅप

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
### व्यायाम

- अंमलबजावणी: "सीएसव्हीमध्ये किती वेगवेगळ्या शहरे आहेत?"
- एक फंक्शन लिहा `उत्तर_क्वेशन (डीएफ, प्रश्न)` जे पांडास + ओलामा एकत्र करते.
- या प्रश्नाची चाचणी घ्या: “कोणत्या ग्राहकाचे सर्वाधिक उत्पन्न आहे?”

### सोल्यूशन्स

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
-

## युनिट 3 - प्रवाहासह एआय डॅशबोर्ड

### उदाहरणे

#### उदाहरण 1 - बार चार्ट

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
df["Sales"].plot(kind="bar", ax=ax)
st.pyplot(fig)
```
#### उदाहरण 2 - हिस्टोग्राम

```python
fig, ax = plt.subplots()
df["Age"].hist(ax=ax, bins=10)
st.pyplot(fig)
```
#### उदाहरण 3 - एलएलएम टिप्पणी

```python
stats = df.describe().to_string()
prompt = f"Erkläre die wichtigsten Trends:\n{stats}"
```
#### उदाहरण 1 - बार चार्ट (प्रवाह)

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
#### उदाहरण 2 - हिस्टोग्राम (प्रवाह)

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
#### उदाहरण 3 - एलएलएम टिप्पणी (ओलामा एसडीके)

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
#### उदाहरण 4 - दोन गटांची तुलना

```python
city1, city2 = "Berlin", "Hamburg"
df1 = df[df["City"] == city1]
df2 = df[df["City"] == city2]
prompt = f"Vergleiche {city1} und {city2}:\n{df1.describe().to_string()}\n{df2.describe().to_string()}"
```
### व्यायाम

- वय वितरण (हिस्टोग्राम) आणि एलएलएम विश्लेषणासह डॅशबोर्ड तयार करा.
- विक्री चार्ट आणि वय चार्ट दरम्यान स्विच करण्यासाठी ड्रॉपडाउन तयार करा.
- एक वैशिष्ट्य जोडा: “उत्पन्नातील पुरुष वि. स्त्रियांची तुलना करा”.

### सोल्यूशन्स

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
-

## युनिट 4 - उपयोजन

### उदाहरणे

#### उदाहरण 1 - अॅप प्रारंभ करा

```bash
streamlit run app.py
```
#### उदाहरण 2 - आवश्यकता.टीएक्सटी

```
streamlit
pandas
requests
matplotlib
```
#### उदाहरण 3 - डॉकरफाइल

```dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```
#### उदाहरण 4 - डॉकरसह उपयोजन

```bash
docker build -t myapp .
docker run -p 8501:8501 myapp
```
#### उदाहरण 1 - अॅप प्रारंभ करा

```bash
streamlit run app.py
```
#### उदाहरण 2 - आवश्यकता.टीएक्सटी

```text
streamlit
pandas
matplotlib
5—Capstone-Projekte.ai-content-studio_1.lib.ollama
```
#### उदाहरण 3 - डॉकरफाइल

```dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```
#### उदाहरण 4 - डॉकरसह उपयोजन

```bash
docker build -t myapp .
docker run -p 8501:8501 myapp
```
### व्यायाम

- आपल्या स्वत: च्या अॅपसाठी आवश्यकता तयार करा.
- एक डॉकर प्रतिमा तयार करा आणि स्थानिक पातळीवर चालवा.
- स्ट्रीमलीट क्लाऊड (गिटहब → स्ट्रीमलिट क्लाऊड) वर अ‍ॅप प्रारंभ करा.

### सोल्यूशन्स

```text
# requirements.txt
streamlit
pandas
requests

# Docker
docker build -t meine-app .
docker run -p 8501:8501 meine-app
```
-

## युनिट 5 - बोनस: एकाधिक डेटा स्रोतांमध्ये प्रश्नोत्तर

### उदाहरणे

#### उदाहरण 1 - सीएसव्ही + सामान्य प्रश्न

```python
faq = "Q: Was ist KI? A: Maschinen, die wie Menschen denken."
stats = df.describe().to_string()
prompt = f"""Beantworte die Frage basierend auf diesen Quellen:
FAQ: {faq}
CSV-Daten: {stats}
Frage: Was ist das Durchschnittsalter?"""
```
#### उदाहरण 2 - सीएसव्ही + मजकूर दस्तऐवज

```python
doc = open("info.txt").read()
prompt = f"""Verwende CSV + Dokument:
CSV: {df.describe().to_string()}
Dokument: {doc}
Frage: Welche Erkenntnisse gibt es?"""
```
#### उदाहरण 1 - सीएसव्ही + एफएक्यू (ओलामा एसडीके)

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
#### उदाहरण 2 - सीएसव्ही + मजकूर दस्तऐवज (ओलामा एसडीके)

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
### व्यायाम

- ग्राहक डेटासह सीएसव्ही लोड करा आणि त्यास सामान्य प्रश्न फाईलसह एकत्र करा.
- एकाच वेळी दोन्ही स्त्रोतांचे विश्लेषण करणारे एक अ‍ॅप लिहा.
- प्रश्न विचारा: "कोणत्या शहराची सर्वाधिक विक्री आहे आणि एफएक्यू डेटासह ते कसे फिट आहे?"

### सोल्यूशन्स

```python
faq = open("faq.txt").read()
stats = df.describe().to_string()
frage = "Welche Stadt hat den höchsten Umsatz und wie passt das zu den FAQ-Daten?"

prompt = f"""FAQ: {faq}
CSV: {stats}
Frage: {frage}"""
```
-

## युनिट 6 - सारांश

दिवस 4 नंतर, विद्यार्थी हे करू शकतात:

- पांडासह सीएसव्ही/एक्सेल प्रक्रिया
- डेटा बद्दल प्रश्नोत्तरांसाठी एलएलएमएस वापरा
- डेटा विश्लेषणासाठी प्रवाहित अॅप्स तयार करा
- नैसर्गिक भाषेतील सीएसव्ही डेटा क्वेरी
- एकाधिक डेटा स्रोत एकत्र करा
- डॉकरसह अॅप्स कंटेनरिझ करा
- स्ट्रीमलीट क्लाऊडवर अॅप्स उपयोजित करा

-

## युनिट 7 - मिनी प्रकल्प

### मिनी प्रकल्प 1: बुद्धिमान व्यवसाय बुद्धिमत्ता डॅशबोर्ड

** कार्य: ** कंपनीच्या डेटाचे विश्लेषण करणारे आणि व्यवसायाच्या शिफारसी प्रदान करणारे डॅशबोर्ड तयार करा.

** समाधान: **

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
### मिनी प्रकल्प 2: स्वयंचलित अहवाल जनरेटर

** कार्य: ** विविध डेटा स्रोतांकडून स्वयंचलितपणे अहवाल व्युत्पन्न करा.

** समाधान: **

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
### मिनी प्रोजेक्ट 3: स्मार्ट डेटा क्वेरी इंटरफेस

** कार्य: ** संरचित डेटावर नैसर्गिक भाषेचे क्वेरी सक्षम करा.

** समाधान: **

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
### मिनी प्रोजेक्ट 4: मल्टी-सोर्स डेटा फ्यूजन

** कार्य: ** बुद्धिमानपणे वेगवेगळ्या स्त्रोतांकडील डेटा एकत्र आणि विश्लेषण करा.

** समाधान: **

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
### मिनी प्रकल्प 5: भविष्यवाणी विश्लेषण इंटरफेस

** मिशन: ** ऐतिहासिक डेटावर आधारित साध्या अंदाज आणि ट्रेंडसाठी एआय वापरा.

** समाधान: **

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
- चार्ट + एआय टिप्पण्यांसह डॅशबोर्ड तयार करा
- अॅप्स उपयोजित करा (प्रवाह क्लाऊड, डॉकर)
- एकाधिक डेटा स्रोत एकत्र करा