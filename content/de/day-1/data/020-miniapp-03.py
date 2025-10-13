## miniapp-03
import streamlit as st
from lib.helper_ollama import ollama

st.title("Kreativer Textgenerator")
thema = st.text_input("Thema eingeben")
stil = st.selectbox("Stil wählen", ["Gedicht", "Kurzgeschichte", "Haiku", "Limerick"])

if st.button("Generieren") and thema:
    prompt = f"Schreibe ein {stil} über das Thema '{thema}'"
    result = ollama.generate(prompt)
    st.write("**Generierter Text:**")
    st.write(result)
