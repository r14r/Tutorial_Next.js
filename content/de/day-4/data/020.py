# Datei: einheit43_balkendiagramm.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
fig, ax = plt.subplots()
df["Sales"].plot(kind="bar", ax=ax)
st.pyplot(fig)
