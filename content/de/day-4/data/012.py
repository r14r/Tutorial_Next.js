import streamlit as st

file = st.file_uploader("CSV hochladen", type="csv")
if file:
    df = pd.read_csv(file)
    frage = st.text_input("Frage:")
    if frage:
        stats = df.describe().to_string()
        prompt = f"{frage}\nDaten:\n{stats}"
        r = requests.post("http://localhost:11434/api/generate",
                          json={"model": "llama2", "prompt": prompt})
        st.write("Antwort:", r.json()["response"])
