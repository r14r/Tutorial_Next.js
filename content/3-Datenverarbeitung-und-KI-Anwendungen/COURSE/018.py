import streamlit as st

file = st.file_uploader("FAQ hochladen", type="txt")
if file:
    faq = file.read().decode()
    frage = st.text_input("Stelle eine Frage:")
    if st.button("Antworten"):
        prompt = f"Beantworte die Frage aus der FAQ:\n{faq}\nFrage: {frage}"
