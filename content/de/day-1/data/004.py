from lib.helper_ollama import ollama

try:
    result = ollama.generate("Test")
    print("✅ Ollama API läuft!", result[:50])
except Exception as e:
    print("❌ Verbindung fehlgeschlagen:", e)
