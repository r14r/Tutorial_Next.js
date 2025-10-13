st.connection("pets_db", type="sql")
conn = st.connection("sql")
conn = st.connection("snowflake")

class MyConnection(BaseConnection[myconn.MyConnection]):
    def _connect(self, **kwargs) -> MyConnection:
        return myconn.connect(**self._secrets, **kwargs)
    def query(self, query):
        return self._instance.query(query)
