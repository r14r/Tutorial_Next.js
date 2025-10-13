import streamlit as st
import PyPDF2
import io
from lib.helper_ollama import ollama

st.title("PDF-Analyzer mit KI")
pdf_file = st.file_uploader("PDF hochladen", type="pdf")

if pdf_file:
    # PDF Text extrahieren
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.read()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    st.write(f"Extrahierter Text ({len(text)} Zeichen)")
    
    analyse_typ = st.selectbox("Analyse-Typ:", 
                              ["Zusammenfassung", "Hauptthemen", "Sentiment", "Schlüsselwörter"])
    
    if st.button("Analysieren"):
        if analyse_typ == "Zusammenfassung":
            prompt = f"Fasse den folgenden Text in 5 Sätzen zusammen:\n{text[:2000]}"
        elif analyse_typ == "Hauptthemen":
            prompt = f"Identifiziere die 5 Hauptthemen in diesem Text:\n{text[:2000]}"
        elif analyse_typ == "Sentiment":
            prompt = f"Analysiere die Stimmung dieses Textes (positiv/neutral/negativ):\n{text[:2000]}"
        else:
            prompt = f"Extrahiere die 10 wichtigsten Schlüsselwörter:\n{text[:2000]}"
        
        result = ollama.generate(prompt)
        st.write("**Ergebnis:**", result)
