# solution-merge-cvs
files = st.file_uploader("Mehrere CSVs hochladen", type="csv", accept_multiple_files=True)
if files:
    dfs = [pd.read_csv(f) for f in files]
    merged = pd.concat(dfs, ignore_index=True)
    st.dataframe(merged)
