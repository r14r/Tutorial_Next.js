# दिवस 0 - पायथन आणि स्ट्रीमलीट बेसिक्स (एआय अॅप्ससाठी)

लेखक: राल्फ गॅन्टेनमेयर  
तारीख: 2025-10-05

-

## युनिट 0 - परिचय

### शिकण्याची उद्दीष्टे

- पायथनमधील मूलभूत नियंत्रण रचना, कार्ये आणि वर्ग आत्मविश्वासाने वापरा.
- लोड, प्रक्रिया आणि फायली सेव्ह करा (मजकूर, जेएसओएन, सीएसव्ही).
- विजेट्स, साइडबार आणि फाइल अपलोडसह एक सोपा, परस्परसंवादी अ‍ॅप तयार करा.
- दिवसाच्या शेवटी स्वतंत्रपणे एक मिनी-प्रोजेक्ट अंमलात आणा (इनपुट → प्रक्रिया → आउटपुट/डाउनलोड).

### आवश्यकता

- संपादक (वि कोड) आणि टर्मिनल वापरण्याचे मूलभूत ज्ञान.
- पायथन 3.11+ स्थापित; प्रवाह स्थापित करण्यायोग्य.
- पर्यायी: द्रुत चाचण्यांसाठी ज्युपिटर/नोटबुक.

### वेळापत्रक सकाळी 9:00 वाजता - 3:00 p.m

| वेळ | युनिट / सामग्री |
| --------------- | --------------------------------------------------------------------------------------------------------------------------
| 09:00 - 09:20 | परिचय आणि विहंगावलोकन (शिकण्याची उद्दीष्टे, आवश्यकता, प्रक्रिया) |
| 09:20 - 10:05 | 1 - पायथनमधील नियंत्रण रचना (जर/इतर, लूप, आकलन + व्यायाम) |
| 10:05 - 10:35 | 2 - कार्ये आणि पुनर्वापर (व्याख्या, पॅरामीटर्स, रिटर्न्स, लॅम्बडा) |
| 10:35 - 11:15 | 3 - वर्ग आणि मॉड्यूल्स (ओओपी, सानुकूल मॉड्यूल, आयात + व्यायाम) |
| 11:15 - 11:30 | ब्रेक |
| 11:30 - 12:10 | 4 - फाइल आणि डेटा प्रक्रिया (मजकूर, जेएसओएन, पांडास + व्यायामासह सीएसव्ही) |
| 12:10 - 1:10 p.m. | लंच ब्रेक |
| 1:10 p.m. - 1:40 दुपारी | 5 - स्ट्रीमलिट बेस यूआय (शीर्षक, मजकूर, विजेट्स, लेआउट + व्यायाम) |
| 1:40 दुपारी - 2:10 p.m. | 6 - अपलोड आणि निर्यात डेटा (सीएसव्ही, प्रतिमा, डाउनलोड बटण + व्यायाम) |
| 2:10 दुपारी - 2:40 दुपारी | मिनी प्रोजेक्ट (लहान डेटा अॅप: इनपुट, अपलोड, प्रक्रिया, निर्यात) |
| 2:40 दुपारी - 3:00 p.m. | सारांश आणि प्रशिक्षक नोट्स |

-

## युनिट 1 - पायथनमधील नियंत्रण रचना

नियंत्रण रचना प्रोग्रामचा कोर्स निश्चित करते. अटींसह (`if`/` elif`/`अन्यथा) सत्य मूल्यांवर अवलंबून अंमलबजावणी शाखा; लूपसह (`for`,` as`) आम्ही स्टेटमेन्टची पुनरावृत्ती करतो; आकलन (यादी, डिक्ट, सेट आकलन) सह आम्ही इटेरॅबल्सद्वारे कॉम्पॅक्ट ट्रान्सफॉर्मेशन लॉजिक तयार करतो.

### उदाहरणे

#### व्हेरिएबल्स आणि प्रकार

```python
## variablen-und-typen
x = 42
y = 3.14
name = "KI-App"
print(type(x), type(y), type(name))
```
#### आयएफ/एलिफ/अन्य

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
लूपसाठी ####

```python
## for-schleife
for i in range(3):
    print("Iteration:", i)
```
#### लूप असताना

```python
## while-schleife
count = 0
while count < 3:
    print("Zähler:", count)
    count += 1
```
#### यादी आकलन

```python
## list-comprehension
quadrate = [n**2 for n in range(5)]
print(quadrate)
```
#### शब्दकोश आकलन

```python
## dict-comprehensions
wort = "streamlit"
buchstaben = {buch: wort.count(buch) for buch in set(wort)}
print(buchstaben)
```
#### दुहेरी

```python
## verdoppeln
nums = [1, 2, 3, 4, 5]
doppelt = [x * 2 for x in nums]
print(doppelt)
```
-

## युनिट 2 - वैशिष्ट्ये आणि पुन्हा वापरा

कार्ये वर्तन एन्केप्युलेट करतात आणि पुन्हा वापरण्यायोग्यता, चाचणी आणि स्पष्ट इंटरफेस प्रोत्साहित करतात. पॅरामीटर्स (पोझिशनल, कीवर्ड, डीफॉल्ट, व्हेरिएडिक) नियंत्रण इनपुट; रिटर्न व्हॅल्यूज परिणाम प्रदान करतात (अगदी प्रति टपल अनेक). साध्या अभिव्यक्तींसाठी अज्ञात कार्ये (`लॅम्बडा’ शॉर्टहँड आहेत.

### उदाहरणे

```python
## functions-greeting
def begruessung(text):
    print(f"Hallo {text}")

print(begruessung("KI-Ingenieur"))
```
#### एकाधिक परतावा

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
#### लॅम्बडा फंक्शन

```python
## lambda-funktion
quadrat = lambda x: x**2
print(quadrat(5))
```
#### वैशिष्ट्ये: व्यायाम

१) तीन संख्येपैकी सर्वात मोठे रिटर्न असे फंक्शन लिहा.  
२) एक लॅम्बडा फंक्शन लिहा जे स्ट्रिंगला उलट करते.

#### वैशिष्ट्ये: समाधान

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
-

## युनिट 3 - वर्ग आणि मॉड्यूल

ऑब्जेक्ट-ओरिएंटेड प्रोग्रामिंग (ओओपी) * स्टेट * (विशेषता) आणि * वर्तन * (पद्धती) सह * ऑब्जेक्ट्स * च्या आसपास प्रोग्राम आयोजित करते. एक वर्ग म्हणजे ब्ल्यू प्रिंट; * एन्केप्युलेशन* अंमलबजावणीचा तपशील लपवितो; * रचना* आणि* वारसा* पुनर्वापरास प्रोत्साहन देते.

मॉड्यूल वैयक्तिक फायली आहेत ज्या पुन्हा वापरण्यायोग्य कार्ये/वर्ग बंडल करतात. पॅकेजेसमध्ये पॅकेजिंग मोठ्या प्रकल्पांची रचना.

### उदाहरण

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
#### आयात मॉड्यूल

```python
## modul-importieren
import math
print("Wurzel:", math.sqrt(16))
```
#### स्वतःचे मॉड्यूल

फाईल: use.py मध्ये हा कोड आहे:

```python
## utils

def add(a,b):
    return a+b
```
फाईल: मेन.पीमध्ये हा कोड आहे:

```python
## main

from utils import add
print(add(2, 3))
```
#### उदाहरणः ओलामा एसडीकेसह मजकूर विश्लेषणासाठी वर्ग

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
#### वर्ग: व्यायाम

१) पद्धती `ड्राइव्ह` आणि `रिफ्युएल` पद्धतीसह वर्ग `कार.  
२) फंक्शनसह मॉड्यूल `math_utils.py`` is_prime (n) `आणि` मेन.पीपी मध्ये आयात करा.

#### वर्ग: समाधान

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
-

## युनिट 4 - फाइल आणि डेटा प्रक्रिया

फायली डेटा कायम ठेवतात. आम्ही अचूक उघडणे/बंद सुनिश्चित करण्यासाठी संदर्भ व्यवस्थापक (open ओपन (...) `) वापरतो. जेएसओएन कॉन्फिगरेशन/स्ट्रक्चर्ससाठी योग्य आहे; सीएसव्ही सामान्य टेबल डेटा स्वरूप आहे; `पांडास विश्लेषण आणि निर्यात करण्यासाठी शक्तिशाली डेटा फ्रेम ऑफर करते.

### उदाहरणे

#### मजकूर फाईल

```python
## read-write-textfile
with open("daten.txt", "w") as f:
    f.write("KI-Apps sind klasse!\n")

with open("daten.txt", "r") as f:
    print(f.read())
```
#### जेसन

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
#### पांडासह सीएसव्ही

```python
## csv-mit-pandas
import pandas as pd
df = pd.DataFrame({"Name": ["Alice", "Bob"], "Punkte": [95, 88]})
df.to_csv("punkte.csv", index=False)
print(pd.read_csv("punkte.csv"))
```
### डेटा प्रक्रिया: व्यायाम

1) जेएसओएन फाईलमध्ये एक करण्याची यादी जतन करा आणि ती पुन्हा लोड करा.  
२) विद्यार्थ्यांची नावे आणि ग्रेड सीएसव्ही फाईलमध्ये लिहा आणि पुन्हा वाचा.

### डेटा प्रक्रिया: समाधान

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
-

## युनिट 5 - प्रवाह

पायथनमध्ये इंटरएक्टिव्ह वेब अनुप्रयोग द्रुतपणे तयार करण्यासाठी प्रवाह एक मुक्त स्त्रोत फ्रेमवर्क आहे. आपण सामान्य पायथन स्क्रिप्ट लिहिता आणि यूआय घटक व्युत्पन्न करण्यासाठी विशेष प्रवाह आज्ञा जोडा. प्रवाह या आज्ञा ओळखतात आणि त्यांच्याकडून स्वयंचलितपणे वेब इंटरफेस तयार करतात. प्रत्येक वेळी जेव्हा वापरकर्ता यूआय घटकाशी संवाद साधतो तेव्हा संपूर्ण स्क्रिप्ट पुन्हा चालते.

### सुव्यवस्थित कसे कार्य करते?

- ** घोषणात्मक प्रोग्रामिंग: ** एचटीएमएल, सीएसएस किंवा जावास्क्रिप्ट लिहिण्याऐवजी बटणे, स्लाइडर, मजकूर बॉक्स किंवा आकृत्या यासारख्या यूआय घटकांना थेट पायथन कमांड म्हणून घोषित केले जाते (उदा. `सेंटबटन ()`, `सेंट -टेक्स्ट_इनपुट ()`, `सेंटटेक्स्ट_इनपुट ().
- ** परस्परसंवादावर स्क्रिप्ट पुन्हा तयार करा: ** प्रत्येक वेळी वापरकर्ता विजेटशी संवाद साधतो (उदा. मूल्य बदलते किंवा बटणावर क्लिक करते), संपूर्ण पायथन स्क्रिप्ट वरपासून खालपर्यंत पुन्हा चालू होते. विजेट्सची सद्य स्थिती (उदा. प्रविष्ट केलेली मूल्ये) कायम आहे.
- ** वेगवान व्हिज्युअलायझेशन: ** डेटा, आकृत्या (उदा. मॅटप्लोटलिब, प्लॉटली, अल्तायरसह) किंवा प्रतिमा कोडच्या काही ओळींनी दर्शविली जाऊ शकतात.
- ** फाइल अपलोड आणि डाउनलोडः ** वापरकर्ते फायली अपलोड करू शकतात (उदा. सीएसव्ही, प्रतिमा) आणि प्रक्रिया केलेले परिणाम डाउनलोड करा.
- ** सुलभ स्थापना आणि प्रारंभः ** स्थापना नंतर (`पीआयपी इन्स्टॉल स्ट्रीमलीट`), ब्राउझरमध्ये `स्ट्रीमलीट रन माय_स्क्रिप्ट.पाय.पी. सह एक अॅप सुरू केला जाऊ शकतो.
- ** लाइव्ह रीलोड: ** पायथन कोडमधील बदल स्वयंचलितपणे शोधले जातात आणि अॅप ब्राउझरमध्ये अद्यतनित करते.

### ठराविक वापर प्रकरणे

- एआय आणि डेटा अनुप्रयोगांसाठी प्रोटोटाइप
- डॅशबोर्ड आणि डेटा व्हिज्युअलायझेशन
- डेटा अन्वेषण किंवा मॉडेल पॅरामीटर ट्यूनिंगसाठी परस्पर साधने
- मशीन लर्निंग मॉडेल्सचे सादरीकरण

द्रुतपणे चाचणी, परिणाम सामायिक करण्यासाठी आणि जास्त विकासाच्या प्रयत्नांशिवाय वापरकर्त्याचे संवाद सक्षम करण्यासाठी प्रवाह उत्कृष्ट आहे.

### सुव्यवस्थित मूलभूत गोष्टी

प्रवाह “यूआय म्हणून कोड” तत्त्वावर कार्य करते. एचटीएमएल/सीएसएस लिहिण्याऐवजी आपण पायथन फंक्शन्स वापरता जे स्वयंचलितपणे वेब घटकांमध्ये रूपांतरित होते. हे डेटा विश्लेषण, मशीन लर्निंग आणि प्रोटोटाइपिंगसाठी आदर्श बनवते.

#### मजकूर आणि मार्कडाउन

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
#### इनपुट विजेट्स

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
#### फायली अपलोड करा

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
#### डेटा व्हिज्युअलायझेशन

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
#### लेआउट आणि कंटेनर

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
#### स्थिती आणि संदेश

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
#### सत्र राज्य

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
#### कॅशिंग आणि कामगिरी

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
#### डाउनलोड आणि निर्यात

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
प्रवाह एक मुक्त स्त्रोत फ्रेमवर्क आहे ज्यामुळे कमीतकमी प्रयत्नांसह पायथनमध्ये थेट परस्पर वेब अनुप्रयोग तयार करणे शक्य होते. हे विशेषत: डेटा वैज्ञानिक, विकसक आणि एआयमध्ये रस असणा those ्यांकडे आहे ज्यांना त्यांचे विश्लेषण, मॉडेल्स किंवा साधने अॅप म्हणून उपलब्ध करुन देऊ इच्छित आहेत आणि वेब विकासाचे कोणतेही ज्ञान न घेता.

### उदाहरणे

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
! [डेमो] (मालमत्ता/5-01.png)

### sreemlit: व्यायाम

1) वजन आणि उंचीसह बीएमआय कॅल्क्युलेटर.  
२) दोन स्तंभ: डावीकडील इनपुट, उजवीकडे उलट स्ट्रिंग.

#### प्रवाह: समाधान

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
### चीटशीट

** प्रवाह एपीआय फसवणूक पत्रक **

हा प्रवाह, v1.50.0 च्या नवीनतम आवृत्तीसाठी डॉक्सचा सारांश आहे.

### फसवणूक पत्रक: स्थापित आणि आयात करा

```bash
pip install streamlit

streamlit run first_app.py
```
#### आयात अधिवेशन

```python
## import
import streamlit as st
```
### चीटशीट: प्री-रीलिझ वैशिष्ट्ये

```bash
## pre-release-features
pip uninstall streamlit
pip install streamlit-nightly --upgrade
```
### चीटशीट: कमांड लाइन

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
#### मॅजिक कमांडस स्ट्रीट राइटला स्पष्टपणे कॉल करा ()

```python
## magic-commands
"*This* is some **Markdown**"
my_variable
"dataframe:", my_data_frame
```
### चीटशीट: मजकूर प्रदर्शित करा

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
### चीटशीट: डेटा प्रदर्शित करा

```python
st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
st.json({"foo":"bar","fu":"ba"})
st.metric("My metric", 42, 2)
```
### चीटशीट: प्रदर्शित मीडिया

```python
st.image("./header.png")
st.logo("logo.jpg")
st.pdf("my_document.pdf")
st.audio(data)
st.video(data)
st.video(data, subtitles="./subs.vtt")
```
### चीटशीट: प्रदर्शन चार्ट

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
#### वापरकर्ता निवडींसह कार्य करा

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
### चीटशीट: साइडबारमध्ये घटक जोडा

#### फक्त सेंट साइडबार नंतर जोडा

```python
a = st.sidebar.radio("Select one:", [1, 2])
```
#### किंवा "सह" नोटेशन वापरा

```python
with st.sidebar:
    st.radio("Select one:", [1, 2])
```
### चीटशीट: स्तंभ

#### दोन समान स्तंभ

```python
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")
```
#### तीन भिन्न स्तंभ

```python
col1, col2, col3 = st.columns([3, 1, 1])
```
#### तळाशी-संरेखित स्तंभ

```python
col1, col2 = st.columns(2, vertical_alignment="bottom")
```
#### आपण "सह" नोटेशन देखील वापरू शकता

```python
with col1:
    st.radio("Select one:", [1, 2])
```
### चीटशीट: टॅब

#### कंटेनर टॅबमध्ये विभक्त केले

```python
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
```
#### आपण "सह" नोटेशन देखील वापरू शकता

```python
with tab1:
    st.radio("Select one:", [1, 2])
```
### चीटशीट: विस्तार करण्यायोग्य कंटेनर

```python
expand = st.expander("My label", icon=":material/info:")
expand.write("Inside the expander.")
pop = st.popover("Button label")
pop.checkbox("Show all")
```
#### आपण "सह" नोटेशन देखील वापरू शकता

```python
with expand:
    st.radio("Select one:", [1, 2])
```
### चीटशीट: नियंत्रण प्रवाह

#### त्वरित अंमलबजावणी थांबवा

```python
st.stop()
```
#### त्वरित स्क्रिप्ट

```python
st.rerun()
```
#### दुसर्‍या पृष्ठावर नेव्हिगेट करा

```python
st.switch_page("pages/my_page.py")
```
### चीटशीट: नेव्हिगेशन

#### आपल्या एंट्रीपॉईंट फाइलमध्ये नेव्हिगेशन विजेट परिभाषित करा

```python
pg = st.navigation(
    st.Page("page1.py", title="Home", url_path="home", default=True)
    st.Page("page2.py", title="Preferences", url_path="settings")
)
pg.run()
```
### चीटशीट: फॉर्म

#### गट एकाधिक विजेट्स

```python
with st.form(key="my_form"):
    username = st.text_input("Username")
    password = st.text_input("Password")
    st.form_submit_button("Login")
```
#### एक संवाद कार्य परिभाषित करा

```python
@st.dialog("Welcome!")
def modal_dialog():
    st.write("Hello")

modal_dialog()
```
#### एक तुकडा परिभाषित करा

```python
@st.fragment
def fragment_function():
    df = get_data()
    st.line_chart(df)
    st.button("Update")

fragment_function()
```
### चीटशीट: इंटरएक्टिव्ह विजेट्स प्रदर्शित करा

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
#### व्हेरिएबल्समध्ये विजेट्सची परत केलेली मूल्ये वापरा

```python
for i in range(int(st.number_input("Num:"))):
    foo()
if st.sidebar.selectbox("I:",["f"]) == "f":
    b()
my_slider_val = st.slider("Quinn Mallory", 1, 88)
st.write(slider_val)
```
#### इंटरएक्टिव्हिटी काढण्यासाठी विजेट्स अक्षम करा

```python
st.slider("Pick a number", 0, 100, disabled=True)
```
चॅट-आधारित अ‍ॅप्स तयार करा

#### चॅट मेसेज कंटेनर घाला

```python
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
```
#### अ‍ॅपच्या तळाशी चॅट इनपुट विजेट प्रदर्शित करा

```python
st.chat_input("Say something")
```
#### चॅट इनपुट विजेट इनलाइन प्रदर्शित करा

```python
with st.container():
    st.chat_input("Say something")
```
मूलभूत एलएलएम चॅट अ‍ॅप कसे तयार करावे ते शिका

### चीटशीट: डेटा उत्परिवर्तित करा

#### डेटा दर्शविल्यानंतर पंक्ती जोडा

```python
element = st.dataframe(df1)
element.add_rows(df2)
```
#### चार चार्टमध्ये दर्शविल्यानंतर पंक्ती जोडा

```python
element = st.line_chart(df1)
element.add_rows(df2)
```
### चीटशीट: प्रदर्शन कोड

```python
with st.echo():
    st.write("Code will be executed and printed")
```
प्लेसहोल्डर, मदत आणि पर्याय

#### कोणताही एकल घटक पुनर्स्थित करा

```python
element = st.empty()
element.line_chart(...)
element.text_input(...)  # Replaces previous.
```
#### ऑर्डरच्या बाहेर घाला

```python
elements = st.container()
elements.line_chart(...)
st.write("Hello")
elements.text_input(...)  # Appears above "Hello".
```
#### आडव्या फ्लेक्स

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
डेटा स्रोतांशी कनेक्ट व्हा

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
### चीटशीट: कामगिरी ऑप्टिमाइझ करा

#### कॅशे डेटा ऑब्जेक्ट्स

डेटा फ्रेम गणना, डाउनलोड केलेला डेटा संचयित करणे इ.

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
#### कॅशे जागतिक संसाधने

टेन्सरफ्लो सत्र, डेटाबेस कनेक्शन इ.

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
### चीटशीट: प्रगती आणि स्थिती प्रदर्शित करा

#### प्रक्रियेदरम्यान फिरकीपटू दर्शवा

```python
with st.spinner(text="In progress"):
    time.sleep(3)
    st.success("Done")
```
#### प्रगती बार दर्शवा आणि अद्यतनित करा

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
### चीटशीट: वापरकर्त्यांसाठी अ‍ॅप्स वैयक्तिकृत करा

#### वापरकर्त्यांना प्रमाणीकृत करा

```python
if not st.user.is_logged_in:
    st.login("my_provider")
f"Hi, {st.user.name}"
st.logout()
```
#### कुकीज, शीर्षलेख, लोकॅल आणि ब्राउझर डेटाचे शब्दकोष मिळवा

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
-

## युनिट 6 - अपलोड आणि निर्यात डेटा

### पाठ्यपुस्तक - मूलभूत आणि पार्श्वभूमी

बरेच एआय अॅप्स फाइल अपलोड (सीएसव्ही, प्रतिमा) ची अपेक्षा करतात आणि निर्यात ऑफर करतात. प्रवाहामध्ये हे `सेंटफाइल_उलपोडर आणि` सेंट डाऊनलोड_बट्टन `सह क्षुल्लक आहे.

### उदाहरणे

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
### व्यायाम

1) प्रतिमा अपलोड आणि पहा.  
२) एकाधिक सीएसव्ही विलीन करा.

### सोल्यूशन्स

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
-

### उदाहरणे

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
#### एआय एकत्रीकरण: अपलोड केलेले सीएसव्ही ओल्लामा एसडीकेसह विलीन करा

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
#### एआय एकत्रीकरण: ओलामा एसडीके सह मजकूर सारांश अॅप प्रवाहित करा

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
-

## युनिट 7 - मिनी प्रकल्प

### ध्येय

इनपुट, सीएसव्ही अपलोड, प्रक्रिया आणि एका मिनी अॅपमध्ये निर्यात करा.

### आवश्यकता

- “टीप” मजकूर फील्ड (प्रत्येक ओळीवर लिहिलेले)
- कच्चा डेटा सीएसव्ही अपलोड करा
- प्रक्रिया: संख्यात्मक "मूल्य" स्तंभ दुप्पट
- आउटपुट: टेबल + डाउनलोड

### सोल्यूशन्स

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
