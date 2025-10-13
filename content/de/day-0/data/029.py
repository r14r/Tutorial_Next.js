# layout-and-container
import streamlit as st

# Seitenleiste (Sidebar)
st.sidebar.title("Seitenleiste")
filter_wert = st.sidebar.slider("Filter:", 0, 100, 50)

# Spalten
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Spalte 1")
    st.button("Button 1")
with col2:
    st.write("Spalte 2")
    st.button("Button 2")
with col3:
    st.write("Spalte 3")
    st.button("Button 3")

# Spalten mit unterschiedlichen Breiten
col1, col2 = st.columns([2, 1])  # 2:1 Verhältnis

# Container und Expander
with st.container():
    st.write("Das ist ein Container")
    st.write("Alles hier gehört zusammen")

with st.expander("Klick mich zum Erweitern"):
    st.write("Versteckter Inhalt")
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png")

# Tabs
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.write("Inhalt von Tab 1")
with tab2:
    st.write("Inhalt von Tab 2")
with tab3:
    st.write("Inhalt von Tab 3")
