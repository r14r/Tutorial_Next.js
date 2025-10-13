## textanalyser-ollama
from lib.helper_ollama import ollama

class TextAnalyser:
    def __init__(self, text):
        self.text = text
    def zusammenfassen(self):
        prompt = f"Fasse den folgenden Text in 1 Satz zusammen:\n{self.text}"
        return ollama.generate(prompt)

analyser = TextAnalyser("Streamlit ist ein Python-Framework für Web-Apps.")
print(analyser.zusammenfassen())
