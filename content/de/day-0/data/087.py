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
