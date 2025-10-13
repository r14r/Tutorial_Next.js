## miniapp-02
import streamlit as st
from lib.helper_ollama import ollama

st.title("Sentiment-Analyse mit KI")
text = st.text_area("Text eingeben")
if st.button("Analysieren") and text:
    prompt = f"Klassifiziere den Sentiment des folgenden Textes als 'positiv', 'neutral' oder 'negativ': {text}"
    result = ollama.generate(prompt)
    
    if "positiv" in result.lower():
        st.success(f"Positiv: {result}")
    elif "negativ" in result.lower():
        st.error(f"Negativ: {result}")
    else:
        st.info(f"Neutral: {result}")
