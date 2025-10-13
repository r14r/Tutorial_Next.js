## app-playground
import streamlit as st

st.title("KI-App Spielwiese")
st.markdown("Fetter Text mit **Markdown**")
st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png")

name = st.text_input("Dein Name")
if st.button("Sag Hallo"):
    st.success(f"Hallo {name}")
