import requests

try:
    r = requests.get("http://localhost:11434")
    print("✅ Ollama API läuft!")
except Exception as e:
    print("❌ Verbindung fehlgeschlagen:", e)
