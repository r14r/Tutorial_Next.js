# Day 0 — Python & Streamlit Basics (for AI Apps)

Author: Ralph Göstenmeier  
Date: 2025-10-05

---

## Unit 0 — Introduction

### Learning objectives

- Confidently use the basic control structures, functions and classes in Python.
- Load, process and save files (text, JSON, CSV).
- Build a simple, interactive app with widgets, sidebar and file upload with Streamlit.
- Implement a mini-project independently at the end of the day (input → processing → output/download).

### Requirements

- Basic knowledge of using an editor (VS Code) and the terminal.
- Python 3.11+ installed; Streamlit installable.
- Optional: Jupyter/Notebooks for quick tests.

### Schedule 9:00 a.m. – 3:00 p.m

| time | Unit / Content |
|---------------|---------------------------------------------------------------------------------|
| 09:00 – 09:20 | Introduction & overview (learning objectives, requirements, process) |
| 09:20 – 10:05 | 1 — Control structures in Python (if/else, loops, comprehensions + exercises) |
| 10:05 – 10:35 | 2 — Functions & Reuse (Definition, Parameters, Returns, Lambda) |
| 10:35 – 11:15 | 3 — Classes & Modules (OOP, custom modules, import + exercises) |
| 11:15 – 11:30 | break |
| 11:30 – 12:10 | 4 — File & Data Processing (Text, JSON, CSV with pandas + exercises) |
| 12:10 – 1:10 p.m. | Lunch break |
| 1:10 p.m. – 1:40 p.m. | 5 — Streamlit Base UI (Title, Text, Widgets, Layout + Exercises) |
| 1:40 p.m. – 2:10 p.m. | 6 — Upload & export data (CSV, images, download button + exercises) |
| 2:10 p.m. – 2:40 p.m. | Mini project (small data app: input, upload, processing, export) |
| 2:40 p.m. – 3:00 p.m. | Summary & Trainer Notes |

---

## Unit 1 — Control Structures in Python

Control structures determine the course of a program. With conditions (`if`/`elif`/`else`) execution branches depending on truth values; with loops (`for`, `while`) we repeat statements; With comprehensions (list, dict, set comprehensions) we formulate compact transformation logic via iterables.

### Examples

#### Variables and types

```python
## variablen-und-typen
x = 42
y = 3.14
name = "KI-App"
print(type(x), type(y), type(name))
```
#### If/elif/else

```python
## if-elif-else
temperatur = 30
if temperatur > 25:
    print("Es ist heiß")
elif temperatur > 15:
    print("Es ist warm")
else:
    print("Es ist kalt")
```
#### For loop

```python
## for-schleife
for i in range(3):
    print("Iteration:", i)
```
#### While loop

```python
## while-schleife
count = 0
while count < 3:
    print("Zähler:", count)
    count += 1
```
#### List comprehension

```python
## list-comprehension
quadrate = [n**2 for n in range(5)]
print(quadrate)
```
#### Dictionary Comprehension

```python
## dict-comprehensions
wort = "streamlit"
buchstaben = {buch: wort.count(buch) for buch in set(wort)}
print(buchstaben)
```
#### Double

```python
## verdoppeln
nums = [1, 2, 3, 4, 5]
doppelt = [x * 2 for x in nums]
print(doppelt)
```
---

## Unit 2 — Features and Reuse

Functions encapsulate behavior and promote reusability, testability and clear interfaces. Parameters (positional, keyword, default, variadic) control inputs; Return values ​​provide results (even several per tuple). Anonymous functions (`lambda`) are shorthand for simple expressions.

### Examples

```python
## functions-greeting
def begruessung(text):
    print(f"Hallo {text}")

print(begruessung("KI-Ingenieur"))
```
#### Multiple returns

```python
## functions-divide
def teile(a, b):
    """Gibt den Quotienten und Rest der Division von a durch b zurück."""
    return a // b, a % b

# Beispielaufruf
quotient, rest = teile(17, 5)
print("Quotient:", quotient)
print("Rest:", rest)
```
#### Lambda function

```python
## lambda-funktion
quadrat = lambda x: x**2
print(quadrat(5))
```
#### Features: Exercises

1) Write a function that returns the largest of three numbers.  
2) Write a lambda function that reverses a string.

#### Features: Solutions

```python
## max-von-drei
def max_von_drei(a, b, c):
    return max(a, b, c)

print(max_von_drei(3, 7, 5))
```

```python
## umkehren
umkehren = lambda s: s[::-1]
print(umkehren("streamlit"))
```
---

## Unit 3 — Classes and Modules

Object-oriented programming (OOP) organizes programs around *objects* with *state* (attributes) and *behavior* (methods). A class is the blueprint; *Encapsulation* hides implementation details; *Composition* and *inheritance* promote reuse.

Modules are individual files that bundle reusable functions/classes. Packaging in packages structures larger projects.

### Example

```python
## bankkonto-klasse
class BankKonto:
    def __init__(self, besitzer, stand=0):
        self.besitzer = besitzer
        self.stand = stand

    def einzahlen(self, betrag):
        self.stand += betrag

    def anzeigen(self):
        print(f"{self.besitzer} hat {self.stand} Euro")

acc = BankKonto("Alice", 100)
acc.einzahlen(50)
acc.anzeigen()
```
#### Import module

```python
## modul-importieren
import math
print("Wurzel:", math.sqrt(16))
```
#### Own module

The file: utils.py contains this code:

```python
## utils

def add(a,b):
    return a+b
```
The file: main.py contains this code:

```python
## main

from utils import add
print(add(2, 3))
```
#### Example: Class for text analysis with Ollama SDK

```python
## textanalyser-ollama
from lib.helper_ollama import ollama

class TextAnalyser:
    def __init__(self, text):
        self.text = text
    def zusammenfassen(self):
        prompt = f"Fasse den folgenden Text in 1 Satz zusammen:\n{self.text}"
        return ollama.generate(prompt)

analyser = TextAnalyser("Streamlit ist ein Python-Framework für Web-Apps.")
print(analyser.zusammenfassen())
```
#### Classes: Exercises

1) Class `Car` with methods `drive` and `refuel`.  
2) Module `math_utils.py` with function `is_prime(n)` and import into `main.py`.

#### Classes: Solutions

```python
## auto-klasse
class Auto:
    def __init__(self, marke, benzin=100):
        self.marke = marke
        self.benzin = benzin

    def fahren(self):
        if self.benzin > 0:
            self.benzin -= 10
            print(f"{self.marke} fährt!")
        else:
            print("Kein Benzin!")

    def tanken(self):
        self.benzin = 100
        print(f"{self.marke} vollgetankt.")
```

```python
## math-utils-is-prime
def ist_primzahl(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

from math_utils import ist_primzahl
print(ist_primzahl(7))
```
---

## Unit 4 — File & Data Processing

Files persist data. We use context managers (`with open(...)`) to ensure correct opening/closing. JSON is suitable for configuration/structures; CSV is common table data format; `pandas` offers powerful data frames for analysis and export.

### Examples

#### Text file

```python
## read-write-textfile
with open("daten.txt", "w") as f:
    f.write("KI-Apps sind klasse!\n")

with open("daten.txt", "r") as f:
    print(f.read())
```
#### JSON

```python
## dump-load-json
import json
config = {"modell": "llama2", "temperatur": 0.7}
with open("config.json", "w") as f:
    json.dump(config, f)

with open("config.json", "r") as f:
    geladen = json.load(f)
    print(geladen)
```
#### CSV with pandas

```python
## csv-mit-pandas
import pandas as pd
df = pd.DataFrame({"Name": ["Alice", "Bob"], "Punkte": [95, 88]})
df.to_csv("punkte.csv", index=False)
print(pd.read_csv("punkte.csv"))
```
### Data processing: exercises

1) Save a to-do list to a JSON file and load it again.  
2) Write student names and grades into a CSV file and read it again.

### Data processing: solutions

```python
## dump-load-json
tasks = ["Dokumentation lesen", "App bauen", "Modell testen"]

import json
with open("tasks.json", "w") as f:
    json.dump(tasks, f)

with open("tasks.json", "r") as f:
    print(json.load(f))
```

```python
## read-write-csv-with-pandas
import pandas as pd
schueler = {"Name": ["Alice", "Bob"], "Note": [90, 85]}
df = pd.DataFrame(schueler)
df.to_csv("noten.csv", index=False)
print(pd.read_csv("noten.csv"))
```
---

## Unit 5 — Streamlit

Streamlit is an open source framework for quickly building interactive web applications in Python. You write a normal Python script and add special Streamlit commands to generate UI elements. Streamlit recognizes these commands and automatically builds a web interface from them. Every time a user interacts with a UI element, the entire script is re-run.

### How does Streamlit work?

- **Declarative programming:** Instead of writing HTML, CSS or JavaScript, UI elements such as buttons, sliders, text boxes or diagrams are declared directly as Python commands (e.g. `st.button()`, `st.slider()`, `st.text_input()`).
- **Script rerun on interaction:** Every time a user interacts with a widget (e.g. changes a value or clicks a button), the entire Python script is rerun from top to bottom. The current state of the widgets (e.g. entered values) is retained.
- **Fast visualization:** Data, diagrams (e.g. with Matplotlib, Plotly, Altair) or images can be displayed with just a few lines of code.
- **File uploads and downloads:** Users can upload files (e.g. CSV, images) and download processed results.
- **Easy installation and start:** After installation (`pip install streamlit`), an app can be started in the browser with `streamlit run my_script.py`.
- **Live Reload:** Changes to the Python code are automatically detected and the app updates in the browser.

### Typical use cases

- Prototypes for AI and data applications
- Dashboards and data visualizations
- Interactive tools for data exploration or model parameter tuning
- Presentation of machine learning models

Streamlit is great for quickly testing ideas, sharing results, and enabling user interactions without much development effort.

### Streamlit basics

Streamlit works on the “Code as UI” principle. Instead of writing HTML/CSS, you use Python functions that are automatically converted into web components. This makes it ideal for data analysis, machine learning and prototyping.

#### Text and Markdown

```python
# title_header_text-and-markdown
import streamlit as st

# Titel und Überschriften
st.title("Meine erste Streamlit-App")
st.header("Das ist eine Überschrift")
st.subheader("Das ist eine Unterüberschrift")

# Einfacher Text
st.text("Das ist einfacher Text")
st.write("Das ist flexibler Text mit **Markdown**-Unterstützung")

# Markdown mit Formatierung
st.markdown("""
### Liste:
- Punkt 1
- Punkt 2
- **Fetter Text**
- *Kursiver Text*
""")

# Code anzeigen
st.code("print('Hallo Welt!')", language='python')
```
#### Input widgets

```python
# input-widgets
import streamlit as st

# Textfelder
name = st.text_input("Dein Name:")
passwort = st.text_input("Passwort:", type="password")
beschreibung = st.text_area("Beschreibung:", height=100)

# Zahlen
alter = st.number_input("Alter:", min_value=0, max_value=120, value=25)
temperatur = st.slider("Temperatur:", -10.0, 40.0, 20.0, 0.5)

# Auswahlfelder
farbe = st.selectbox("Wähle eine Farbe:", ["Rot", "Grün", "Blau"])
hobbys = st.multiselect("Hobbys:", ["Lesen", "Sport", "Musik", "Reisen"])
ist_aktiv = st.checkbox("Aktiv")
geschlecht = st.radio("Geschlecht:", ["Männlich", "Weiblich", "Divers"])

# Datum und Zeit
datum = st.date_input("Geburtsdatum:")
zeit = st.time_input("Uhrzeit:")

# Buttons
if st.button("Absenden"):
    st.success(f"Hallo {name}! Du bist {alter} Jahre alt.")
```
#### Upload files

```python
# upload-files
import streamlit as st
import pandas as pd
from PIL import Image

# Einzelne Datei
csv_file = st.file_uploader("CSV-Datei hochladen", type=["csv"])
if csv_file:
    df = pd.read_csv(csv_file)
    st.dataframe(df)

# Mehrere Dateien
files = st.file_uploader("Mehrere Dateien", accept_multiple_files=True)
if files:
    st.write(f"Du hast {len(files)} Dateien hochgeladen")

# Bilddateien
img_file = st.file_uploader("Bild hochladen", type=["png", "jpg", "jpeg"])
if img_file:
    image = Image.open(img_file)
    st.image(image, caption="Hochgeladenes Bild")
```
#### Data visualization

```python
# visuaöisation
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Beispieldaten
df = pd.DataFrame({
    'x': range(10),
    'y': np.random.randn(10).cumsum()
})

# Streamlit Charts
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

# Matplotlib
fig, ax = plt.subplots()
ax.plot(df['x'], df['y'])
st.pyplot(fig)

# Plotly (interaktiv)
fig = px.line(df, x='x', y='y', title='Interaktiver Plot')
st.plotly_chart(fig)

# Karten
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [52.5, 13.4],  # Berlin
    columns=['lat', 'lon']
)
st.map(map_data)
```
#### Layout and containers

```python
# layout-and-container
import streamlit as st

# Seitenleiste (Sidebar)
st.sidebar.title("Seitenleiste")
filter_wert = st.sidebar.slider("Filter:", 0, 100, 50)

# Spalten
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Spalte 1")
    st.button("Button 1")
with col2:
    st.write("Spalte 2")
    st.button("Button 2")
with col3:
    st.write("Spalte 3")
    st.button("Button 3")

# Spalten mit unterschiedlichen Breiten
col1, col2 = st.columns([2, 1])  # 2:1 Verhältnis

# Container und Expander
with st.container():
    st.write("Das ist ein Container")
    st.write("Alles hier gehört zusammen")

with st.expander("Klick mich zum Erweitern"):
    st.write("Versteckter Inhalt")
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png")

# Tabs
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.write("Inhalt von Tab 1")
with tab2:
    st.write("Inhalt von Tab 2")
with tab3:
    st.write("Inhalt von Tab 3")
```
#### Status and Messages

```python
# status-and-messages
import streamlit as st
import time

# Status-Nachrichten
st.success("Das hat funktioniert! ✅")
st.error("Hier ist ein Fehler aufgetreten ❌")
st.warning("Warnung: Bitte beachten ⚠️")
st.info("Information: Das ist wichtig zu wissen ℹ️")

# Ausnahme anzeigen
try:
    result = 1 / 0
except Exception as e:
    st.exception(e)

# Progress Bar
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)

# Spinner
with st.spinner("Lade Daten..."):
    time.sleep(2)
st.success("Fertig!")

# Ballon-Animation
if st.button("Feier mich!"):
    st.balloons()
```
#### Session State

```python
# session-state
import streamlit as st

# Session State initialisieren
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if 'name' not in st.session_state:
    st.session_state.name = ''

# Counter-Beispiel
st.write(f"Counter: {st.session_state.counter}")

if st.button("+1"):
    st.session_state.counter += 1

if st.button("-1"):
    st.session_state.counter -= 1

if st.button("Reset"):
    st.session_state.counter = 0

# Name speichern
name_input = st.text_input("Name:", value=st.session_state.name)
if name_input != st.session_state.name:
    st.session_state.name = name_input

st.write(f"Gespeicherter Name: {st.session_state.name}")
```
#### Caching and performance

```python
## caching
import streamlit as st
import pandas as pd
import time

# Cache für Daten
@st.cache_data
def load_data():
    # Simuliert langsame Datenladung
    time.sleep(2)
    return pd.DataFrame({
        'A': range(1000),
        'B': range(1000, 2000)
    })

# Cache für Ressourcen (z.B. ML-Modelle)
@st.cache_resource
def load_model():
    # Simuliert Modell-Laden
    time.sleep(3)
    return "Fake ML Model"

st.title("Caching Demo")

# Diese Funktion wird nur einmal ausgeführt
data = load_data()
st.write(f"Daten geladen: {data.shape}")

model = load_model()
st.write(f"Modell geladen: {model}")
```
#### Downloads and Exports

```python
## download-and-export
import streamlit as st
import pandas as pd
import json

# CSV Download
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Alter': [25, 30, 35]}
df = pd.DataFrame(data)

csv = df.to_csv(index=False)
st.download_button(
    label="CSV herunterladen",
    data=csv,
    file_name='daten.csv',
    mime='text/csv'
)

# JSON Download
json_data = json.dumps(data, indent=2)
st.download_button(
    label="JSON herunterladen",
    data=json_data,
    file_name='daten.json',
    mime='application/json'
)

# Text Download
text_data = "Das ist ein Beispieltext\nMit mehreren Zeilen"
st.download_button(
    label="Text herunterladen",
    data=text_data,
    file_name='text.txt',
    mime='text/plain'
)
```
Streamlit is an open source framework that makes it possible to build interactive web applications directly in Python with minimal effort. It is aimed particularly at data scientists, developers and those interested in AI who want to make their analyses, models or tools available as an app quickly and without any knowledge of web development.

### Examples

```python
## app-playground
import streamlit as st

st.title("KI-App Spielwiese")
st.markdown("Fetter Text mit **Markdown**")
st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png")

name = st.text_input("Dein Name")
if st.button("Sag Hallo"):
    st.success(f"Hallo {name}")
```
![Demo](assets/5-01.png)

### Sreamlit: Exercises

1) BMI calculator with weight and height.  
2) Two columns: input on the left, the reverse string on the right.

#### Streamlit: Solutions

```python
# exercise-bmi-calculator
import streamlit as st
st.title("BMI-Rechner")
gewicht = st.number_input("Gewicht (kg)")
groesse = st.number_input("Größe (m)")
if gewicht and groesse:
    bmi = gewicht / (groesse**2)
    st.write(f"Dein BMI ist {bmi:.2f}")
```

```python
## exercise-two-cols
import streamlit as st
col1, col2 = st.columns(2)
text = col1.text_input("Text eingeben")
temp = st.sidebar.slider("Modell-Temperatur", 0.0, 1.0, 0.7)
```
### Cheatsheet

**Streamlit API cheat sheet**

This is a summary of the docs for the latest version of Streamlit, v1.50.0.

### Cheat Sheet: Install and Import

```bash
pip install streamlit

streamlit run first_app.py
```
#### Import convention

```python
## import
import streamlit as st
```
### Cheatsheet: Pre-release features

```bash
## pre-release-features
pip uninstall streamlit
pip install streamlit-nightly --upgrade
```
### Cheatsheet: Command line

```bash
## command-line
streamlit cache clear
streamlit config show
streamlit docs
streamlit hello
streamlit help
streamlit init
streamlit run streamlit_app.py
streamlit version
```
#### Magic commands implicitly call st.write()

```python
## magic-commands
"*This* is some **Markdown**"
my_variable
"dataframe:", my_data_frame
```
### Cheatsheet: Display text

```python
## display-text
st.write("Most objects") # df, err, func, keras!
st.write(["st", "is <", 3])
st.write_stream(my_generator)
st.write_stream(my_llm_stream)

st.text("Fixed width text")
st.markdown("*Markdown*")
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.title("My title")
st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")
st.badge("New")
st.html("<p>Hi!</p>")
```
### Cheatsheet: Display data

```python
st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
st.json({"foo":"bar","fu":"ba"})
st.metric("My metric", 42, 2)
```
### Cheatsheet: Display media

```python
st.image("./header.png")
st.logo("logo.jpg")
st.pdf("my_document.pdf")
st.audio(data)
st.video(data)
st.video(data, subtitles="./subs.vtt")
```
### Cheatsheet: Display charts

```python
st.area_chart(df)
st.bar_chart(df)
st.bar_chart(df, horizontal=True)
st.line_chart(df)
st.map(df)
st.scatter_chart(df)

st.altair_chart(chart)
st.graphviz_chart(fig)
st.plotly_chart(fig)
st.pydeck_chart(chart)
st.pyplot(fig)
st.vega_lite_chart(df, spec)
```
#### Work with user selections

```python
## work-with-user-selections
event = st.plotly_chart(
    df,
    on_select="rerun"
)
event = st.altair_chart(
    chart,
    on_select="rerun"
)
event = st.vega_lite_chart(
    df,
    spec,
    on_select="rerun"
)
```
### Cheatsheet: Add elements to sidebar

#### Just add it after st.sidebar

```python
a = st.sidebar.radio("Select one:", [1, 2])
```
#### Or use "with" notation

```python
with st.sidebar:
    st.radio("Select one:", [1, 2])
```
### Cheatsheet: Columns

#### Two equal columns

```python
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")
```
#### Three different columns

```python
col1, col2, col3 = st.columns([3, 1, 1])
```
#### Bottom-aligned columns

```python
col1, col2 = st.columns(2, vertical_alignment="bottom")
```
#### You can also use "with" notation

```python
with col1:
    st.radio("Select one:", [1, 2])
```
### Cheatsheet: Tabs

#### Insert containers separated into tabs

```python
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
```
#### You can also use "with" notation

```python
with tab1:
    st.radio("Select one:", [1, 2])
```
### Cheatsheet: Expandable containers

```python
expand = st.expander("My label", icon=":material/info:")
expand.write("Inside the expander.")
pop = st.popover("Button label")
pop.checkbox("Show all")
```
#### You can also use "with" notation

```python
with expand:
    st.radio("Select one:", [1, 2])
```
### Cheatsheet: Control flow

#### Stop execution immediately

```python
st.stop()
```
#### Rerun script immediately

```python
st.rerun()
```
#### Navigate to another page

```python
st.switch_page("pages/my_page.py")
```
### Cheatsheet: Navigation

#### Define a navigation widget in your entrypoint file

```python
pg = st.navigation(
    st.Page("page1.py", title="Home", url_path="home", default=True)
    st.Page("page2.py", title="Preferences", url_path="settings")
)
pg.run()
```
### Cheatsheet: Form

#### Group multiple widgets

```python
with st.form(key="my_form"):
    username = st.text_input("Username")
    password = st.text_input("Password")
    st.form_submit_button("Login")
```
#### Define a dialog function

```python
@st.dialog("Welcome!")
def modal_dialog():
    st.write("Hello")

modal_dialog()
```
#### Define a fragment

```python
@st.fragment
def fragment_function():
    df = get_data()
    st.line_chart(df)
    st.button("Update")

fragment_function()
```
### Cheatsheet: Display interactive widgets

```python
st.button("Click me")
st.download_button("Download file", data)
st.link_button("Go to gallery", url)
st.page_link("app.py", label="Home")
st.data_editor("Edit data", data)
st.checkbox("I agree")
st.feedback("thumbs")
st.pills("Tags", ["Sports", "Politics"])
st.radio("Pick one", ["cats", "dogs"])
st.segmented_control("Filter", ["Open", "Closed"])
st.toggle("Enable")
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
st.audio_input("Record a voice message")
st.camera_input("Take a picture")
st.color_picker("Pick a color")
```
#### Use widgets' returned values ​​in variables

```python
for i in range(int(st.number_input("Num:"))):
    foo()
if st.sidebar.selectbox("I:",["f"]) == "f":
    b()
my_slider_val = st.slider("Quinn Mallory", 1, 88)
st.write(slider_val)
```
#### Disable widgets to remove interactivity

```python
st.slider("Pick a number", 0, 100, disabled=True)
```
Build chat-based apps

#### Insert a chat message container

```python
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
```
#### Display a chat input widget at the bottom of the app

```python
st.chat_input("Say something")
```
#### Display a chat input widget inline

```python
with st.container():
    st.chat_input("Say something")
```
Learn how to Build a basic LLM chat app

### Cheatsheet: Mutate data

#### Add rows to a dataframe after showing it

```python
element = st.dataframe(df1)
element.add_rows(df2)
```
#### Add rows to a chart after showing it

```python
element = st.line_chart(df1)
element.add_rows(df2)
```
### Cheatsheet: Display code

```python
with st.echo():
    st.write("Code will be executed and printed")
```
Placeholders, help, and options

#### Replace any single element

```python
element = st.empty()
element.line_chart(...)
element.text_input(...)  # Replaces previous.
```
#### Insert out of order

```python
elements = st.container()
elements.line_chart(...)
st.write("Hello")
elements.text_input(...)  # Appears above "Hello".
```
#### Horizontally flex

```python
flex = st.container(horizontal=True)
flex.button("A")
flex.button("B")
```

```python
st.help(pandas.DataFrame)
st.get_option(key)
st.set_option(key, value)
st.set_page_config(layout="wide")
st.query_params[key]
st.query_params.from_dict(params_dict)
st.query_params.get_all(key)
st.query_params.clear()
st.html("<p>Hi!</p>")
```
Connect to data sources

```python
st.connection("pets_db", type="sql")
conn = st.connection("sql")
conn = st.connection("snowflake")

class MyConnection(BaseConnection[myconn.MyConnection]):
    def _connect(self, **kwargs) -> MyConnection:
        return myconn.connect(**self._secrets, **kwargs)
    def query(self, query):
        return self._instance.query(query)
```
### Cheatsheet: Optimize performance

#### Cache data objects

Data frame computation, storing downloaded data, etc

```python
@st.cache_data
def foo(bar):
    # Do something expensive and return data
    return data

# Executes foo
d1 = foo(ref1)

# Does not execute foo
# Returns cached item by value, d1 == d2
d2 = foo(ref1)

# Different arg, so function foo executes
d3 = foo(ref2)

# Clear the cached value for foo(ref1)
foo.clear(ref1)

# Clear all cached entries for this function
foo.clear()

# Clear values from *all* in-memory or on-disk cached functions
st.cache_data.clear()
```
#### Cache global resources

TensorFlow session, database connection, etc

```python
@st.cache_resource
def foo(bar):
    # Create and return a non-data object
    return session

# Executes foo
s1 = foo(ref1)

# Does not execute foo
# Returns cached item by reference, s1 == s2
s2 = foo(ref1)

# Different arg, so function foo executes
s3 = foo(ref2)

# Clear the cached value for foo(ref1)
foo.clear(ref1)

# Clear all cached entries for this function
foo.clear()

# Clear all global resources from cache
st.cache_resource.clear()
```
### Cheatsheet: Display progress and status

#### Show a spinner during a process

```python
with st.spinner(text="In progress"):
    time.sleep(3)
    st.success("Done")
```
#### Show and update progress bar

```python
bar = st.progress(50)
time.sleep(3)
bar.progress(100)

with st.status("Authenticating...") as s:
    time.sleep(2)
    st.write("Some long response.")
    s.update(label="Response")

st.balloons()
st.snow()
st.toast("Warming up...")
st.error("Error message")
st.warning("Warning message")
st.info("Info message")
st.success("Success message")
st.exception(e)
```
### Cheatsheet: Personalize apps for users

#### Authenticate users

```python
if not st.user.is_logged_in:
    st.login("my_provider")
f"Hi, {st.user.name}"
st.logout()
```
#### Get dictionaries of cookies, headers, locale, and browser data

```python
st.context.cookies
st.context.headers
st.context.ip_address
st.context.is_embedded
st.context.locale
st.context.theme.type
st.context.timezone
st.context.timezone_offset
st.context.url
```
---

## Unit 6 — Upload & Export Data

### Textbook - basics and background

Many AI apps expect file uploads (CSV, images) and offer exports. In Streamlit this is trivial with `st.file_uploader` and `st.download_button`.

### Examples

```python
# upload-and-export
import pandas as pd
import streamlit as st

st.title("Daten-Upload & Export")

file = st.file_uploader("CSV hochladen", type="csv")
if file:
    df = pd.read_csv(file)
    st.dataframe(df)
    csv = df.to_csv(index=False).encode()
    st.download_button("CSV herunterladen", csv, "export.csv")
```
### Exercises

1) Upload and view image.  
2) Merge multiple CSVs.

### Solutions

```python
# solution-image-upload
img_file = st.file_uploader("Bild hochladen", type=["jpg", "png"])
if img_file:
    st.image(img_file)
```

```python
# solution-merge-cvs
files = st.file_uploader("Mehrere CSVs hochladen", type="csv", accept_multiple_files=True)
if files:
    dfs = [pd.read_csv(f) for f in files]
    merged = pd.concat(dfs, ignore_index=True)
    st.dataframe(merged)
```
---

### Examples

```python
# upload-export.py
import pandas as pd
import streamlit as st

st.title("Daten-Upload & Export")

file = st.file_uploader("CSV hochladen", type="csv")
if file:
    df = pd.read_csv(file)
    st.dataframe(df)
    csv = df.to_csv(index=False).encode()
    st.download_button("CSV herunterladen", csv, "export.csv")
```
#### AI integration: Merge uploaded CSV with Ollama SDK

```python
# upload-ollama.py
import pandas as pd
import streamlit as st
from lib.helper_ollama import ollama

st.title("CSV-Upload & KI-Zusammenfassung")
file = st.file_uploader("CSV hochladen", type="csv")
if file:
    df = pd.read_csv(file)
    st.dataframe(df)
    stats = df.describe().to_string()
    prompt = f"Fasse die wichtigsten Erkenntnisse aus diesen Daten zusammen:\n{stats}"
    result = ollama.generate(prompt)
    st.write(result)
```
#### AI integration: Streamlit text summarization app with Ollama SDK

```python
# streamlit-ollama.py
import streamlit as st
from lib.helper_ollama import ollama

st.title("Textzusammenfassung mit KI")
text = st.text_area("Text eingeben")
if st.button("Zusammenfassen") and text:
    prompt = f"Fasse den folgenden Text in 1 Satz zusammen:\n{text}"
    result = ollama.generate(prompt)
    st.write(result)
```
---

## Unit 7 — Mini Projects

### Goal

Combine input, CSV upload, processing and export into one mini app.

### Requirements

- “Note” text field (written on each line)
- CSV upload of raw data
- Processing: double the numeric “Value” column
- Output: table + download

### Solutions

```python
# mini-app
import streamlit as st
import pandas as pd

st.title("Mini-Daten-App")

note = st.text_input("Notiz")
file = st.file_uploader("CSV hochladen", type="csv")

if file:
    df = pd.read_csv(file)
    if "Wert" in df.columns:
        df["Wert_x2"] = df["Wert"] * 2
    if note:
        df["Notiz"] = note
    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Ergebnis als CSV", csv, "ergebnis.csv", "text/csv")
```
