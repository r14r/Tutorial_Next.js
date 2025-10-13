## exercise-two-cols
import streamlit as st
col1, col2 = st.columns(2)
text = col1.text_input("Text eingeben")
temp = st.sidebar.slider("Modell-Temperatur", 0.0, 1.0, 0.7)
