import streamlit as st
import requests

st.title("Chat mit Ollama (lokales LLM)")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("Du:", "")

if st.button("Senden") and user_input:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": user_input}
    )
    reply = response.json()["response"]
    st.session_state['chat_history'].append(("Du", user_input))
    st.session_state['chat_history'].append(("Ollama", reply))

for sender, msg in st.session_state['chat_history']:
    st.write(f"**{sender}:** {msg}")
