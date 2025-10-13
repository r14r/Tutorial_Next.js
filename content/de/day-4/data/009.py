df = pd.read_csv("kunden.csv")
print(df["Einkommen"].median())
print(df[df["Alter"] > 40])
stats = df.describe().to_string()
prompt = f"Welche wirtschaftlichen Trends lassen sich erkennen?\n{stats}"
print(df.sort_values("Einkommen", ascending=False))
