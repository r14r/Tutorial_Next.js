## read-write-csv-with-pandas
import pandas as pd
schueler = {"Name": ["Alice", "Bob"], "Note": [90, 85]}
df = pd.DataFrame(schueler)
df.to_csv("noten.csv", index=False)
print(pd.read_csv("noten.csv"))
