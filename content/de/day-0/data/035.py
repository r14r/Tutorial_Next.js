# exercise-bmi-calculator
import streamlit as st
st.title("BMI-Rechner")
gewicht = st.number_input("Gewicht (kg)")
groesse = st.number_input("Größe (m)")
if gewicht and groesse:
    bmi = gewicht / (groesse**2)
    st.write(f"Dein BMI ist {bmi:.2f}")
