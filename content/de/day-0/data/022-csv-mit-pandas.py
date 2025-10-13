## csv-mit-pandas
import pandas as pd
df = pd.DataFrame({"Name": ["Alice", "Bob"], "Punkte": [95, 88]})
df.to_csv("punkte.csv", index=False)
print(pd.read_csv("punkte.csv"))
