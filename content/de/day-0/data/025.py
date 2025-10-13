# title_header_text-and-markdown
import streamlit as st

# Titel und Überschriften
st.title("Meine erste Streamlit-App")
st.header("Das ist eine Überschrift")
st.subheader("Das ist eine Unterüberschrift")

# Einfacher Text
st.text("Das ist einfacher Text")
st.write("Das ist flexibler Text mit **Markdown**-Unterstützung")

# Markdown mit Formatierung
st.markdown("""
### Liste:
- Punkt 1
- Punkt 2
- **Fetter Text**
- *Kursiver Text*
""")

# Code anzeigen
st.code("print('Hallo Welt!')", language='python')
