## dump-load-json
import json
config = {"modell": "llama2", "temperatur": 0.7}
with open("config.json", "w") as f:
    json.dump(config, f)

with open("config.json", "r") as f:
    geladen = json.load(f)
    print(geladen)
