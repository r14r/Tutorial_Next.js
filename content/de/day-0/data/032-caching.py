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
