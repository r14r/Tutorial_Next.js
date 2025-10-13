## miniapp-01
import streamlit as st
from lib.helper_ollama import ollama

st.title("KI-Tutor Chatbot")
if 'chat' not in st.session_state:
    st.session_state.chat = []
    
user_input = st.text_input("Frage den KI-Tutor:")
if st.button("Senden") and user_input:
    messages = [
        {"role": "system", "content": "Du bist ein freundlicher, geduldiger Tutor."},
        {"role": "user", "content": user_input}
    ]
    antwort = ollama.chat(messages)
    st.session_state.chat.append(("Du", user_input))
    st.session_state.chat.append(("Tutor", antwort))
    
for sprecher, text in st.session_state.chat:
    st.write(f"**{sprecher}:** {text}")
