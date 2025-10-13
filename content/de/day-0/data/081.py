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
