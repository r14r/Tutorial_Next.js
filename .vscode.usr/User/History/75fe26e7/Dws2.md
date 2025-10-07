## Einheit 1.3 — Ollama in der Kommandozeile (CLI)

### 📖 Hintergrund

Ollama bringt ein eigenes Kommandozeilen-Tool mit. Damit können Modelle heruntergeladen, gelistet und direkt ausgeführt werden – ohne Python.

- `ollama pull <modell>` → Modell herunterladen
- `ollama list` → verfügbare Modelle anzeigen
- `ollama run <modell>` → Modell starten und mit Prompts interagieren

### 💻 Beispiele

- Modell herunterladen

```sh
ollama pull llama2
```

# 2. Alle installierten Modelle anzeigen
ollama list

# 3. Direkt mit einem Modell chatten
ollama run llama2
```

#### Dialog in der CLI

```
>>> Was ist Python?
Python ist eine Programmiersprache, die für ihre Einfachheit und Vielseitigkeit bekannt ist.
```

#### Direkter Prompt von der Shell aus

```sh
echo "Schreibe ein Haiku über KI." | ollama run llama2
```

### 📝 Übungen

1. Lade das Modell mistral herunter.
2. Liste alle Modelle und überprüfe, ob mistral installiert ist.
3. Führe `ollama run mistral` aus und frage nach: „Nenne mir drei Anwendungen von KI.“

### ✅ Lösungen

```sh
ollama pull mistral
ollama list
ollama run mistral
```

Antwortbeispiel:

- Sprachassistenten
- Bildklassifikation
- Betrugserkennung
