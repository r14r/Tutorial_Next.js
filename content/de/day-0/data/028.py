# visuaöisation
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Beispieldaten
df = pd.DataFrame({
    'x': range(10),
    'y': np.random.randn(10).cumsum()
})

# Streamlit Charts
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

# Matplotlib
fig, ax = plt.subplots()
ax.plot(df['x'], df['y'])
st.pyplot(fig)

# Plotly (interaktiv)
fig = px.line(df, x='x', y='y', title='Interaktiver Plot')
st.plotly_chart(fig)

# Karten
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [52.5, 13.4],  # Berlin
    columns=['lat', 'lon']
)
st.map(map_data)
