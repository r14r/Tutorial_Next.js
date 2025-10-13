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
