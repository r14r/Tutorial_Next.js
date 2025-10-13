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
