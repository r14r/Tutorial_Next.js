# session-state
import streamlit as st

# Session State initialisieren
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if 'name' not in st.session_state:
    st.session_state.name = ''

# Counter-Beispiel
st.write(f"Counter: {st.session_state.counter}")

if st.button("+1"):
    st.session_state.counter += 1

if st.button("-1"):
    st.session_state.counter -= 1

if st.button("Reset"):
    st.session_state.counter = 0

# Name speichern
name_input = st.text_input("Name:", value=st.session_state.name)
if name_input != st.session_state.name:
    st.session_state.name = name_input

st.write(f"Gespeicherter Name: {st.session_state.name}")
