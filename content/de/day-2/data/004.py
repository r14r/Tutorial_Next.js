import streamlit as st
from lib.helper_ollama import ollama

st.title("Chain-of-Thought Problemlöser")
problem = st.text_area("Beschreibe ein Problem:")

if st.button("Lösen") and problem:
    cot_prompt = f"""
Löse das folgende Problem Schritt für Schritt:

Problem: {problem}

Denke laut und erkläre jeden Schritt:
1. Verstehe das Problem
2. Identifiziere die Schlüsselinformationen  
3. Entwickle einen Lösungsansatz
4. Führe die Lösung durch
5. Prüfe das Ergebnis

Lösung:"""
    
    result = ollama.generate(cot_prompt)
    st.write("**Schritt-für-Schritt Lösung:**")
    st.write(result)
