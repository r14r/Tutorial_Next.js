# 1. Gemischte Stimmung → oft "Neutral" oder "Gemischt"
text = "Der Service war langsam, aber das Essen war lecker."
# Modell sagt z. B. "Neutral"

# 2. Liste verarbeiten
texts = ["Super Qualität!", "Völlig unbrauchbar!", "Ganz okay."]
for t in texts:
    prompt = f"Stimmung: {t}"
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": prompt})
    print(t, "→", r.json()["response"])

# 3. Funktion
def analyze_sentiment(text):
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "llama2", "prompt": f"Analysiere Stimmung: {text}"})
    return r.json()["response"]

print(analyze_sentiment("Das Konzert war großartig!"))
