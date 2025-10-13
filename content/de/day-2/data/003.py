import streamlit as st
from lib.helper_ollama import ollama

st.title("Few-Shot Learning Demo")
text = st.text_input("Text zur Klassifikation:")

if st.button("Klassifizieren") and text:
    few_shot_prompt = f"""
Klassifiziere die folgenden Texte als POSITIV oder NEGATIV:

"Das Essen war fantastisch!" -> POSITIV
"Der Service war schrecklich." -> NEGATIV  
"Ich liebe dieses Produkt!" -> POSITIV
"Das war eine Enttäuschung." -> NEGATIV

"{text}" -> """
    
    result = ollama.generate(few_shot_prompt)
    st.write("**Klassifikation:**", result)
