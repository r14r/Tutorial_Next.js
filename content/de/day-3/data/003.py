import streamlit as st
from lib.helper_ollama import ollama

st.title("Social Media Content Optimizer")
original_text = st.text_area("Ursprünglicher Text")
plattform = st.selectbox("Ziel-Plattform:", 
                        ["Twitter", "LinkedIn", "Instagram", "Facebook"])

if st.button("Optimieren") and original_text:
    if plattform == "Twitter":
        prompt = f"Kürze den Text auf max. 280 Zeichen für Twitter, behalte die Kernbotschaft:\n{original_text}"
    elif plattform == "LinkedIn":
        prompt = f"Schreibe den Text professioneller und strukturierter für LinkedIn um:\n{original_text}"
    elif plattform == "Instagram":
        prompt = f"Mache den Text emotionaler und visueller für Instagram:\n{original_text}"
    else:
        prompt = f"Mache den Text einladender und community-orientiert für Facebook:\n{original_text}"
    
    result = ollama.generate(prompt)
    st.write("**Optimierter Text:**")
    st.write(result)
    
    # Zusätzlich: Hashtag-Vorschläge
    if st.button("Hashtags vorschlagen"):
        hashtag_prompt = f"Schlage 5 relevante Hashtags für diesen {plattform}-Post vor:\n{result}"
        hashtags = ollama.generate(hashtag_prompt)
        st.write("**Hashtag-Vorschläge:**", hashtags)
