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
