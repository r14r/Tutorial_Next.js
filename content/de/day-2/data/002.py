import streamlit as st
from lib.helper_ollama import ollama

st.title("Rollenspieler-Chatbot")
rolle = st.selectbox("Wähle eine Rolle:", 
                    ["Lehrer", "Comedian", "Wissenschaftler", "Pirat"])

if 'chat' not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Du:")
if st.button("Senden") and user_input:
    system_prompt = f"Du bist ein {rolle}. Antworte im entsprechenden Stil."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
    antwort = ollama.chat(messages)
    st.session_state.chat.append((rolle, antwort))

for sprecher, text in st.session_state.chat:
    st.write(f"**{sprecher}:** {text}")
