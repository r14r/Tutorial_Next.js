# Histogramm
fig, ax = plt.subplots()
df["Age"].hist(ax=ax)
st.pyplot(fig)

# Auswahl
chart = st.selectbox("Diagramm wählen", ["Umsatz", "Alter"])
if chart == "Umsatz":
    df["Sales"].plot(kind="bar")
else:
    df["Age"].hist()

# Geschlechtervergleich
male = df[df["Gender"] == "Male"]
female = df[df["Gender"] == "Female"]
prompt = f"Vergleiche Einkommen von Männern und Frauen:\n{male.describe()}\n{female.describe()}"
