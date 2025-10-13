## dict-comprehensions
wort = "streamlit"
buchstaben = {buch: wort.count(buch) for buch in set(wort)}
print(buchstaben)
