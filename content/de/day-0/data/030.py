# status-and-messages
import streamlit as st
import time

# Status-Nachrichten
st.success("Das hat funktioniert! ✅")
st.error("Hier ist ein Fehler aufgetreten ❌")
st.warning("Warnung: Bitte beachten ⚠️")
st.info("Information: Das ist wichtig zu wissen ℹ️")

# Ausnahme anzeigen
try:
    result = 1 / 0
except Exception as e:
    st.exception(e)

# Progress Bar
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)

# Spinner
with st.spinner("Lade Daten..."):
    time.sleep(2)
st.success("Fertig!")

# Ballon-Animation
if st.button("Feier mich!"):
    st.balloons()
