stats = df.describe().to_string()
prompt = f"Erkläre die wichtigsten Trends:\n{stats}"
