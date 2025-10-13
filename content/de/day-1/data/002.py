import streamlit as st
from lib.helper_ollama import ollama

st.title("KI-Anwendungen Demo")
anwendung = st.selectbox("Wähle eine KI-Anwendung:", 
                        ["Textgenerierung", "Übersetzung", "Zusammenfassung"])

if anwendung == "Textgenerierung":
    prompt = "Schreibe ein kurzes Gedicht über Künstliche Intelligenz"
elif anwendung == "Übersetzung":
    prompt = "Übersetze 'Hello World' ins Deutsche"
else:
    prompt = "Erkläre Maschinelles Lernen in einem Satz"

if st.button("KI ausführen"):
    result = ollama.generate(prompt)
    st.write("KI-Antwort:", result)
