fig, ax = plt.subplots()
df["Age"].hist(ax=ax, bins=10)
st.pyplot(fig)
