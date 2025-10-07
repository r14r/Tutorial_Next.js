stats = df.describe().to_string()
prompt = f"""Beantworte die Frage basierend auf diesen Daten:
{stats}
Frage: Wie viele Kunden sind älter als 30?"""
