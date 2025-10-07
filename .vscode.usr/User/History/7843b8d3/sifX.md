## Einheit 2.3 — Rollen im Prompting & Prompt Engineering: Grundlagen

### Hintergrund

Prompt Engineering bezeichnet die Kunst, Eingaben (Prompts) so zu formulieren, dass das Modell bestmögliche Ergebnisse liefert.

In modernen APIs (z. B. Ollama, OpenAI) bestehen Prompts aus Nachrichten mit Rollen:

- **system** – definiert die Identität des Modells („Du bist ein hilfreicher Tutor…“)
- **user** – enthält die Anfrage des Nutzers
- **assistant** – (optional) vorherige Antworten des Modells, um Konversationen fortzuführen
- **tool/function** – (in erweiterten Frameworks) spezielle Funktionsaufrufe

Ein Prompt enthält:

- Aufgabe („Fasse zusammen…“)
- Kontext („Der Text ist ein Artikel über…“)
- Format („in Bulletpoints“)

Unterschiedliche Formulierungen → unterschiedliche Ergebnisse.
