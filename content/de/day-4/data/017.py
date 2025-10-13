import matplotlib.pyplot as plt

fig, ax = plt.subplots()
df["Sales"].plot(kind="bar", ax=ax)
st.pyplot(fig)
