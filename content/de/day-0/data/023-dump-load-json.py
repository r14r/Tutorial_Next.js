## dump-load-json
tasks = ["Dokumentation lesen", "App bauen", "Modell testen"]

import json
with open("tasks.json", "w") as f:
    json.dump(tasks, f)

with open("tasks.json", "r") as f:
    print(json.load(f))
