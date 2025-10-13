## read-write-textfile
with open("daten.txt", "w") as f:
    f.write("KI-Apps sind klasse!\n")

with open("daten.txt", "r") as f:
    print(f.read())
