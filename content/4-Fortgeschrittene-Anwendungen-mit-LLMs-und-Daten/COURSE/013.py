city1, city2 = "Berlin", "Hamburg"
df1 = df[df["City"] == city1]
df2 = df[df["City"] == city2]
prompt = f"Vergleiche {city1} und {city2}:\n{df1.describe().to_string()}\n{df2.describe().to_string()}"
