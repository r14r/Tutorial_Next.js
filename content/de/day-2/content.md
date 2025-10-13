# Tag 2 — Arbeiten mit LLMs & Prompt Engineering

## Einheit 1 — Zeitplan 09:00 – 15:00

### Übersicht

Der Tag bietet eine praxisnahe Einführung in Large Language Models (LLMs) und Prompt Engineering. Jede Einheit kombiniert kurze Erklärungen, Code-Beispiele und praktische Übungen.

---

### Zeitplan

| Zeit            | Einheit / Inhalt                                                                 | Dauer   |
|-----------------|----------------------------------------------------------------------------------|---------|
| **09:00 – 09:20** | Einführung & Überblick - Was sind LLMs? Ziele des Tages         | 20 min  |
| **09:20 – 09:50** | **Einheit 2.1:** Einführung in LLMs - Hintergrund, Einsatzgebiete, Grenzen | 30 min  |
| **09:50 – 10:20** | **Einheit 2.2:** Was ist ein Prompt? - Prompt-Elemente, Beispiele, Übungen | 30 min  |
| **10:20 – 10:50** | **Einheit 2.3:** Rollen im Prompting & Grundlagen - System/User/Assistant, Prompt Engineering | 30 min  |
| **10:50 – 11:05** | ☕ **Pause**                                                                    | 15 min  |
| **11:05 – 11:35** | **Einheit 2.4:** Prompting-Prinzipien - Zero-/Few-Shot, Chain-of-Thought, Output-Format | 30 min  |
| **11:35 – 12:05** | **Einheit 2.5:** Prompt-Playground & Vergleich - Streamlit-App, Prompt-Experimente | 30 min  |
| **12:05 – 13:05** | 🍽️ **Mittagspause**                                                            | 60 min  |
| **13:05 – 13:35** | **Einheit 2.6:** Temperatur & Kreativität - Parameter, Temperature, Max Tokens | 30 min  |
| **13:35 – 14:05** | **Einheit 2.7:** Vergleich verschiedener Modelle - llama2, mistral, codellama | 30 min  |
| **14:05 – 14:35** | **Einheit 2.8:** Fehler & Grenzen von LLMs - Halluzinationen, Bias, Kontext | 30 min  |
| **14:35 – 14:55** | **Einheit 2.9:** Praktische Prompt-Beispiele - Zusammenfassung, Rollen, Code, JSON | 20 min  |
| **14:55 – 15:00** | **Zusammenfassung & Ausblick** - Wiederholung, Fragen, nächste Schritte | 5 min   |

---

## Einheit 1 — Einführung in Large Language Models (LLMs)

### Beschreibung & Grundlagen

Large Language Models (LLMs) sind künstliche Intelligenzen, die auf riesigen Mengen an Textdaten trainiert wurden. Sie nutzen neuronale Netze, insbesondere Transformer-Architekturen, um Sprache zu verstehen und zu generieren. Bekannte Vertreter sind GPT (OpenAI), Llama (Meta), Mistral und Gemma (Google). LLMs werden mit Milliarden von Textbeispielen gefüttert und lernen dabei, das jeweils wahrscheinlichste nächste Wort vorherzusagen. Dadurch entwickeln sie die Fähigkeit, komplexe Texte zu schreiben, Fragen zu beantworten, zu übersetzen oder sogar Code zu generieren.

**Wie funktionieren LLMs?**

- Sie analysieren den eingegebenen Text (Prompt) und berechnen, welches Wort am besten als nächstes passt.
- Sie haben kein echtes „Verständnis“ wie ein Mensch, sondern erkennen Muster und Wahrscheinlichkeiten.
- Sie können auf verschiedene Aufgaben spezialisiert werden (z. B. Chatbots, Übersetzer, Code-Generatoren).

**Einsatzgebiete:**

- Automatische Textgenerierung (z. B. E-Mails, Geschichten, Zusammenfassungen)
- Übersetzungen zwischen Sprachen
- Beantwortung von Fragen (Q&A)
- Unterstützung beim Programmieren (Code-Vervollständigung, Fehlererklärung)
- Kreative Aufgaben (Gedichte, Brainstorming)

**Grenzen und Herausforderungen:**

- LLMs können „halluzinieren“, also plausible, aber falsche Informationen erfinden.
- Sie sind nicht deterministisch: Gleicher Prompt kann unterschiedliche Antworten liefern.
- Sie haben ein begrenztes Kontextfenster (können sich nur an eine bestimmte Textmenge erinnern).
- Sie übernehmen Vorurteile (Bias) aus den Trainingsdaten.
- Sie können keine echten Fakten nachschlagen, sondern nur auf Trainingsdaten zurückgreifen.

### 5 Beispiele für den Einsatz von LLMs (mit Python-Code)

1. **Textzusammenfassung:**

    Prompt:

    ```prompt
        "Fasse den folgenden Text in 2 Sätzen zusammen: ..."
    ```

    ```python
    # Datei: beispiel1_zusammenfassung.py
    from lib.helper_ollama import ollama
    text = "Künstliche Intelligenz ist ein Teilgebiet der Informatik ..."
    prompt = f"Fasse den folgenden Text in 2 Sätzen zusammen:\n{text}"
    result = ollama.generate(prompt)
    print(result)
    ```

2. **Fragen beantworten:**

    Prompt:

    ```prompt
        "Was ist der Unterschied zwischen KI und ML?"
    ```

    ```python
    # Datei: beispiel2_fragen.py
    from lib.helper_ollama import ollama
    prompt = "Was ist der Unterschied zwischen KI und ML?"
    result = ollama.generate(prompt)
    print(result)
    ```

3. **Code generieren:**

    Prompt:

    ```prompt
        "Schreibe eine Python-Funktion, die die Fakultät berechnet."
    ```

    ```python
    # Datei: beispiel3_code.py
    from lib.helper_ollama import ollama
    prompt = "Schreibe eine Python-Funktion, die die Fakultät berechnet."
    result = ollama.generate(prompt)
    print(result)
    ```

4. **Übersetzen:**

    Prompt:

    ```prompt
        "Übersetze ins Englische: 'Guten Morgen, wie geht es dir?'"
    ```

    ```python
    # Datei: beispiel4_uebersetzen.py
    from lib.helper_ollama import ollama
    prompt = "Übersetze ins Englische: 'Guten Morgen, wie geht es dir?'"
    result = ollama.generate(prompt)
    print(result)
    ```

5. **Kreative Texte schreiben:**

    Prompt:

    ```prompt
        "Schreibe ein kurzes Gedicht über den Herbst."
    ```

    ```python
    # Datei: beispiel5_gedicht.py
    from lib.helper_ollama import ollama
    prompt = "Schreibe ein kurzes Gedicht über den Herbst."
    result = ollama.generate(prompt)
    print(result)
    ```

### 10 Fragen & Lösungen zu LLMs

1. **Was ist ein Large Language Model (LLM)?**

    *Lösung:* Ein KI-Modell, das auf großen Textmengen trainiert wurde und Sprache generieren kann.
2. **Nenne zwei bekannte LLMs.**

    *Lösung:* GPT, Llama, Mistral, Gemma (je zwei nennen)
3. **Was bedeutet „halluzinieren“ bei LLMs?**

    *Lösung:* Das Modell erfindet plausible, aber falsche Informationen.
4. **Warum sind LLMs nicht deterministisch?**

    *Lösung:* Sie arbeiten probabilistisch, daher kann die gleiche Eingabe zu unterschiedlichen Ausgaben führen.
5. **Wofür kann man LLMs einsetzen?**

    *Lösung:* Textgenerierung, Übersetzung, Q&A, Codegenerierung, Zusammenfassung, Kreativaufgaben
6. **Was ist ein Kontextfenster?**

    *Lösung:* Die maximale Textmenge, die das Modell gleichzeitig verarbeiten kann.
7. **Was ist ein Nachteil von LLMs?**

    *Lösung:* Halluzinationen, Bias, begrenztes Kontextfenster, kein echtes Verständnis
8. **Wie lernen LLMs?**

    *Lösung:* Durch Training auf großen Textmengen und das Vorhersagen des nächsten Wortes.
9. **Können LLMs Fakten nachschlagen?**

    *Lösung:* Nein, sie greifen nur auf ihr Trainingswissen zurück.
10. **Was ist ein typischer Fehler bei der Nutzung von LLMs?**

    *Lösung:* Zu viel Vertrauen in die Korrektheit der generierten Antworten.

---

## Einheit 2 — Was ist ein Prompt?

### Umfangreiche Beschreibung & Grundlagen

Ein Prompt ist die Eingabe, mit der ein Mensch ein Sprachmodell (LLM) steuert. Er ist die „Frage“ oder „Anweisung“, die das Modell beantwortet. Die Qualität und Klarheit des Prompts bestimmen maßgeblich die Qualität der Antwort. Ein Prompt kann eine einfache Frage, eine komplexe Aufgabenstellung oder eine detaillierte Anweisung sein. Gute Prompts sind präzise, enthalten Kontext und geben das gewünschte Ausgabeformat vor.

**Elemente eines guten Prompts:**

- **Rolle:** In welcher Rolle soll das Modell antworten? (z. B. „Du bist ein Lehrer…“)
- **Kontext:** Hintergrundinformationen oder Daten, auf die sich die Antwort beziehen soll
- **Aufgabe:** Die eigentliche Anweisung (z. B. „Fasse den Text zusammen“)
- **Format:** Gewünschte Ausgabeform (z. B. Bulletpoints, JSON, Tabelle)

**Warum ist Prompt Engineering wichtig?**

- Unterschiedliche Formulierungen führen zu unterschiedlichen Ergebnissen.
- Ein klarer Prompt reduziert Missverständnisse und Fehler.
- Mit gezielten Prompts kann man das Modell zu besseren, strukturierteren Antworten führen.

### 5 Beispiele für Prompts (mit Python-Code)

1. **Einfache Frage:**

    Prompt:

    ```prompt
        "Was ist künstliche Intelligenz?"
    ```

    ```python
    # Datei: prompt1_einfache_frage.py
    from lib.helper_ollama import ollama
    prompt = "Was ist künstliche Intelligenz?"
    result = ollama.generate(prompt)
    print(result)
    ```

2. **Rolle vorgeben:**

    +Prompt: "Du bist ein Mathematiklehrer. Erkläre den Satz des Pythagoras."

    ```python
    # Datei: prompt2_rolle.py
    from lib.helper_ollama import ollama
    prompt = "Du bist ein Mathematiklehrer. Erkläre den Satz des Pythagoras."
    result = ollama.generate(prompt)
    print(result)
    ```

3. **Kontext einbauen:**

    Prompt: "Hier ist ein Text: 'Python ist eine Programmiersprache...'. Fasse ihn in 2 Sätzen zusammen."

    ```python
    # Datei: prompt3_kontext.py
    from lib.helper_ollama import ollama
    text = "Python ist eine Programmiersprache..."
    prompt = f"Hier ist ein Text: '{text}'. Fasse ihn in 2 Sätzen zusammen."
    result = ollama.generate(prompt)
    print(result)
    ```

4. **Format anfordern:**

    Prompt: "Nenne drei Vorteile von Solarenergie als nummerierte Liste."

    ```python
    # Datei: prompt4_format.py
    from lib.helper_ollama import ollama
    prompt = "Nenne drei Vorteile von Solarenergie als nummerierte Liste."
    result = ollama.generate(prompt)
    print(result)
    ```

5. **Kombinierte Aufgabe:**

    Prompt: "Du bist ein Reiseberater. Empfiehl mir 3 Reiseziele in Italien und gib zu jedem eine kurze Begründung als Tabelle."

    ```python
    # Datei: prompt5_kombiniert.py
    from lib.helper_ollama import ollama
    prompt = "Du bist ein Reiseberater. Empfiehl mir 3 Reiseziele in Italien und gib zu jedem eine kurze Begründung als Tabelle."
    result = ollama.generate(prompt)
    print(result)
    ```

### 10 Fragen & Lösungen zu Prompts

1. **Was ist ein Prompt?**

    *Lösung:* Die Eingabe/Aufforderung, die ein Mensch einem LLM gibt.
2. **Nenne zwei wichtige Elemente eines guten Prompts.**

    *Lösung:* Rolle, Kontext, Aufgabe, Format (je zwei nennen)
3. **Warum ist die Formulierung des Prompts wichtig?**

    *Lösung:* Sie beeinflusst die Qualität und Genauigkeit der Antwort.
4. **Wie kann man das gewünschte Ausgabeformat vorgeben?**

*Lösung:* Indem man es explizit im Prompt beschreibt (z. B. „als Tabelle“).
5. **Was passiert, wenn ein Prompt zu vage ist?**

*Lösung:* Das Modell gibt oft ungenaue oder unerwünschte Antworten.
6. **Wie kann man Kontext in einen Prompt einbauen?**

*Lösung:* Durch Hinzufügen von Hintergrundinformationen oder Beispielen.
7. **Was ist ein Beispiel für einen Prompt mit Rolle?**

*Lösung:* „Du bist ein Lehrer. Erkläre...“
8. **Wie kann man das Modell zu einer strukturierten Antwort bringen?**

*Lösung:* Durch Vorgabe des Formats (z. B. Bulletpoints, JSON)
9. **Was ist Prompt Engineering?**

*Lösung:* Die Kunst, Prompts so zu gestalten, dass das Modell optimale Ergebnisse liefert.
10. **Wie kann man die Antwort eines LLMs gezielt steuern?**

*Lösung:* Durch präzise, klare und formatierte Prompts.

---

## Einheit 3 — Rollen im Prompting & Prompt Engineering: Grundlagen

### Beschreibung & Grundlagen

Prompt Engineering ist die gezielte Gestaltung von Eingaben (Prompts), um von LLMs optimale Ergebnisse zu erhalten. Ein zentrales Konzept dabei sind **Rollen**: Moderne LLM-APIs wie OpenAI oder Ollama nutzen Nachrichten mit unterschiedlichen Rollen, um Kontexte und Aufgaben klar zu trennen. Die wichtigsten Rollen sind:

- **system:** Definiert die Identität und das Verhalten des Modells (z. B. „Du bist ein hilfreicher Tutor.“)
- **user:** Enthält die eigentliche Anfrage des Nutzers.
- **assistant:** (Optional) Vorherige Antworten des Modells, um Konversationen fortzuführen.
- **tool/function:** (In erweiterten Frameworks) Für spezielle Funktionsaufrufe.

Durch die Kombination dieser Rollen kann man Konversationen strukturieren, den Kontext steuern und die Qualität der Antworten verbessern. Unterschiedliche Formulierungen und Rollen führen zu unterschiedlichen Ergebnissen. Prompt Engineering umfasst auch das Testen, Vergleichen und Optimieren von Prompts.

**Warum sind Rollen wichtig?**

- Sie helfen, die Kommunikation mit dem Modell zu strukturieren.
- Sie ermöglichen es, Kontexte und Aufgaben zu trennen.
- Sie machen Konversationen nachvollziehbar und reproduzierbar.

### 5 Beispiele für Rollen im Prompting (mit Python-Code)

1. **System-Rolle festlegen:**

    **System**: "Du bist ein hilfsbereiter Mathematiklehrer."

    **User**: "Erkläre den Satz des Pythagoras."

    ```python
    # Datei: rollen1_system.py
    from lib.helper_ollama import ollama
    prompt = "System: Du bist ein hilfsbereiter Mathematiklehrer.\nUser: Erkläre den Satz des Pythagoras."
    result = ollama.generate(prompt)
    print(result)
    ```

2. **User-Rolle mit Kontext:**

    **System**: "Du bist ein Reiseexperte."

    **User**: "Empfiehl mir drei Reiseziele in Japan."

    ```python
    # Datei: rollen2_user.py
    from lib.helper_ollama import ollama
    prompt = "System: Du bist ein Reiseexperte.\nUser: Empfiehl mir drei Reiseziele in Japan."
    result = ollama.generate(prompt)
    print(result)
    ```

3. **Assistant-Rolle für Konversation:**

    **System**: "Du bist ein Chatbot."

    **User**: "Was ist KI?"

    **Assistant**: "Künstliche Intelligenz ist..."

    **User**: "Gib ein Beispiel für KI im Alltag."

    ```python
    # Datei: rollen3_assistant.py
    from lib.helper_ollama import ollama
    prompt = "System: Du bist ein Chatbot.\nUser: Was ist KI?\nAssistant: Künstliche Intelligenz ist...\nUser: Gib ein Beispiel für KI im Alltag."
    result = ollama.generate(prompt)
    print(result)
    ```

4. **Vergleich von Prompts:**
    - Prompt 1: "Fasse den Text kurz zusammen."
    - Prompt 2: "Erstelle eine ausführliche Zusammenfassung in 5 Sätzen."

    ```python
    # Datei: rollen4_vergleich.py
    from lib.helper_ollama import ollama
    text = "Künstliche Intelligenz ist ein Teilgebiet der Informatik ..."
    prompt1 = f"Fasse den Text kurz zusammen.\nText: {text}"
    prompt2 = f"Erstelle eine ausführliche Zusammenfassung in 5 Sätzen.\nText: {text}"
    result1 = ollama.generate(prompt1)
    result2 = ollama.generate(prompt2)
    print("Kurz:", result1)
    print("Lang:", result2)
    ```

5. **Tool/Function-Rolle (fortgeschritten):**

    **System**: "Du kannst Rechenaufgaben lösen."

    **User**: "Berechne 23 + 42."

    **Tool/Function**: "65"

    ```python
    # Datei: rollen5_tool.py
    from lib.helper_ollama import ollama
    prompt = "System: Du kannst Rechenaufgaben lösen.\nUser: Berechne 23 + 42.\nTool/Function: 65"
    result = ollama.generate(prompt)
    print(result)
    ```

### 10 Fragen & Lösungen zu Rollen und Prompt Engineering

1. **Was ist Prompt Engineering?**

*Lösung:* Die gezielte Gestaltung von Prompts, um optimale Ergebnisse von LLMs zu erhalten.
2. **Welche Rolle definiert das Verhalten des Modells?**

*Lösung:* Die System-Rolle.
3. **Wofür steht die User-Rolle?**

*Lösung:* Für die Anfrage des Nutzers.
4. **Wie kann man Konversationen mit LLMs strukturieren?**

*Lösung:* Durch die Nutzung verschiedener Rollen (system, user, assistant).
5. **Was ist der Vorteil der Assistant-Rolle?**

*Lösung:* Sie ermöglicht fortlaufende Konversationen und Kontext.
6. **Wie kann man die Qualität der Antworten verbessern?**

*Lösung:* Durch klare Rollenverteilung und präzise Prompts.
7. **Was ist ein Beispiel für einen Prompt mit System-Rolle?**

*Lösung:* „Du bist ein freundlicher Lehrer.“
8. **Warum ist die Trennung von Kontext und Aufgabe wichtig?**

*Lösung:* Um Missverständnisse zu vermeiden und gezielte Antworten zu erhalten.
9. **Wie kann man Prompts testen und vergleichen?**

*Lösung:* Durch verschiedene Formulierungen und Analyse der Ergebnisse.
10. **Was ist ein typischer Fehler beim Prompt Engineering?**

*Lösung:* Unklare Rollen oder Aufgabenstellung, fehlender Kontext.

---

## Einheit 4 — Prompting-Prinzipien

### Umfangreiche Beschreibung & Grundlagen

Um die besten Ergebnisse aus LLMs herauszuholen, gibt es verschiedene Prompting-Prinzipien und Strategien. Sie helfen, die Antworten gezielt zu steuern, Fehler zu vermeiden und die Kreativität des Modells zu nutzen. Die wichtigsten Prinzipien sind:

- **Zero-Shot Prompting:** Das Modell erhält nur die Aufgabe, aber keine Beispiele. Es muss die Aufgabe „aus dem Stand“ lösen.
- **Few-Shot Prompting:** Der Prompt enthält zusätzlich Beispiele, wie die Aufgabe gelöst werden soll. Das Modell kann sich daran orientieren.
- **Role Prompting:** Das Modell wird in eine bestimmte Rolle versetzt (z. B. „Du bist ein Arzt…“), um die Antwort zu beeinflussen.
- **Chain-of-Thought (CoT):** Das Modell wird aufgefordert, Schritt für Schritt zu denken und zu argumentieren.
- **Self-Consistency:** Mehrere Antworten werden generiert, um die beste oder konsistenteste auszuwählen.
- **Output-Format Prompting:** Das gewünschte Ausgabeformat wird explizit vorgegeben (z. B. JSON, Tabelle, Bulletpoints).

**Warum sind diese Prinzipien wichtig?**

- Sie erhöhen die Zuverlässigkeit und Nachvollziehbarkeit der Antworten.
- Sie helfen, Fehler und Missverständnisse zu vermeiden.
- Sie ermöglichen strukturierte, formatierte und kreative Ergebnisse.

### 5 Beispiele für Prompting-Prinzipien (mit Python-Code)

1. **Zero-Shot Prompting:**

    Prompt:

    ```prompt
        "Übersetze folgenden Satz ins Französische: 'Ich liebe KI.'"
    ```

    ```python
    # Datei: prinzip1_zeroshot.py
    from lib.helper_ollama import ollama
    prompt = "Übersetze folgenden Satz ins Französische: 'Ich liebe KI.'"
    result = ollama.generate(prompt)
    print(result)
    ```

2. **Few-Shot Prompting:**

    Prompt:

    ```prompt
        "Übersetze ins Französische:\nDeutsch: Hallo → Französisch: Bonjour\nDeutsch: Danke → Französisch: Merci\nDeutsch: Ich liebe KI → Französisch:"
    ```

    ```python
    # Datei: prinzip2_fewshot.py
    from lib.helper_ollama import ollama
    prompt = "Übersetze ins Französische:\nDeutsch: Hallo → Französisch: Bonjour\nDeutsch: Danke → Französisch: Merci\nDeutsch: Ich liebe KI → Französisch:"
    result = ollama.generate(prompt)
    print(result)
    ```

3. **Role Prompting:**

    Prompt:

    ```prompt
        "Du bist ein Arzt. Erkläre die Symptome einer Grippe für einen Patienten in einfacher Sprache."
    ```

    ```python
    # Datei: prinzip3_role.py
    from lib.helper_ollama import ollama
    prompt = "Du bist ein Arzt. Erkläre die Symptome einer Grippe für einen Patienten in einfacher Sprache."
    result = ollama.generate(prompt)
    print(result)
    ```

4. **Chain-of-Thought Prompting:**

    Prompt:

    ```prompt
        "Löse die Aufgabe Schritt für Schritt: Ein Apfel kostet 2€, eine Orange 3€. Wie viel kostet es, 4 Äpfel und 2 Orangen zu kaufen?"
    ```

    ```python
    # Datei: prinzip4_chainofthought.py
    from lib.helper_ollama import ollama
    prompt = "Löse die Aufgabe Schritt für Schritt: Ein Apfel kostet 2€, eine Orange 3€. Wie viel kostet es, 4 Äpfel und 2 Orangen zu kaufen?"
    result = ollama.generate(prompt)
    print(result)
    ```

5. **Output-Format Prompting:**

    Prompt:

    ```prompt
    "Antworte im JSON-Format: {\"Name\": \"<string>\", \"Alter\": <int>} Frage: Person heißt Alice und ist 30 Jahre alt."
    ```

    ```python
    # Datei: prinzip5_format.py
    from lib.helper_ollama import ollama
    prompt = "Antworte im JSON-Format: {\"Name\": \"<string>\", \"Alter\": <int>} Frage: Person heißt Alice und ist 30 Jahre alt."
    result = ollama.generate(prompt)
    print(result)
    ```

### 10 Fragen & Lösungen zu Prompting-Prinzipien

1. **Was ist Zero-Shot Prompting?**

*Lösung:* Das Modell erhält nur die Aufgabe, aber keine Beispiele.
2. **Wie hilft Few-Shot Prompting?**

*Lösung:* Durch Beispiele kann das Modell die Aufgabe besser verstehen und lösen.
3. **Was ist Role Prompting?**

*Lösung:* Das Modell wird in eine bestimmte Rolle versetzt, um die Antwort zu beeinflussen.
4. **Wozu dient Chain-of-Thought Prompting?**

*Lösung:* Das Modell wird aufgefordert, Schritt für Schritt zu denken und zu argumentieren.
5. **Was ist Self-Consistency?**

*Lösung:* Mehrere Antworten werden generiert, um die beste auszuwählen.
6. **Wie kann man das Ausgabeformat steuern?**

*Lösung:* Durch explizite Vorgabe im Prompt (z. B. „im JSON-Format“).
7. **Warum sind Beispiele im Prompt hilfreich?**

*Lösung:* Sie zeigen dem Modell, wie die Aufgabe gelöst werden soll.
8. **Was ist ein Nachteil von Zero-Shot Prompting?**

*Lösung:* Die Antwort kann ungenau oder unerwartet sein, da keine Beispiele vorliegen.
9. **Wie kann man die Kreativität des Modells fördern?**

*Lösung:* Durch offene Aufgabenstellungen und kreative Rollen.
10. **Was ist ein typischer Fehler bei Prompting-Prinzipien?**

*Lösung:* Fehlende Beispiele, unklare Rollen oder kein Format vorgegeben.

---

st.title("Prompt Playground")
st.title("Prompt-Vergleich")
p1 = st.text_area("Prompt 1")
p2 = st.text_area("Prompt 2")

## Einheit 5 — Prompt-Playground & Prompt-Vergleich (Streamlit-App)

### Umfangreiche Beschreibung & Grundlagen

Ein Prompt-Playground ist eine interaktive Anwendung, mit der man Prompts direkt ausprobieren und die Antworten von LLMs sofort sehen kann. Besonders hilfreich ist dies, um die Wirkung kleiner Änderungen am Prompt zu testen und zu verstehen, wie verschiedene Modelle auf identische oder leicht abgewandelte Prompts reagieren. Ein Prompt-Playground fördert das experimentelle Lernen und ist ein zentrales Werkzeug im Prompt Engineering.

**Vorteile eines Prompt-Playgrounds:**

- Sofortiges Feedback auf Prompts
- Vergleich verschiedener Modelle und Parameter
- Förderung von Kreativität und Experimentierfreude
- Ideal für Workshops, Unterricht und Entwicklung

**Prompt-Vergleich:**
Mit einer Vergleichsfunktion kann man zwei (oder mehr) Prompts direkt gegenüberstellen und die Unterschiede in den Antworten analysieren. Das hilft, die Wirkung von Formulierungen, Rollen oder Parametern zu verstehen.

### 5 Beispiele für Playground-Experimente (mit Python-/Streamlit-Code)

1. **Prompt-Variation:**

    Prompt 1:

    ```prompt
    "Fasse den Text in 1 Satz zusammen."
    ```

    Prompt 2:

    ```prompt
    "Fasse den Text in 3 Bulletpoints zusammen."
    ```

    ```python
    # Datei: playground1_variation.py
    from lib.helper_ollama import ollama
    text = "Künstliche Intelligenz ist ein Teilgebiet der Informatik ..."
    prompt1 = f"Fasse den Text in 1 Satz zusammen.\nText: {text}"
    prompt2 = f"Fasse den Text in 3 Bulletpoints zusammen.\nText: {text}"
    result1 = ollama.generate(prompt1)
    result2 = ollama.generate(prompt2)
    print("1 Satz:", result1)
    print("3 Bulletpoints:", result2)
    ```

2. **Modellvergleich:**

    Prompt:

    ```prompt
    "Erkläre den Unterschied zwischen Hund und Katze."
    ```

    Modelle:

    ```text
    llama2 vs. mistral
    ```

    ```python
    # Datei: playground2_modellvergleich.py
    from lib.helper_ollama import ollama
    prompt = "Erkläre den Unterschied zwischen Hund und Katze."
    result_llama2 = ollama.generate(prompt, model="llama2")
    result_mistral = ollama.generate(prompt, model="mistral")
    print("llama2:", result_llama2)
    print("mistral:", result_mistral)
    ```

3. **Parameter-Experiment:**

    Prompt:

    ```prompt
    "Schreibe eine kreative Geschichte über einen Roboter."
    - Temperature: 0.2 vs. 1.2
    ```

    ```python
    # Datei: playground3_parameter.py
    from lib.helper_ollama import ollama
    prompt = "Schreibe eine kreative Geschichte über einen Roboter."
    result_low = ollama.generate(prompt, temperature=0.2)
    result_high = ollama.generate(prompt, temperature=1.2)
    print("Temp 0.2:", result_low)
    print("Temp 1.2:", result_high)
    ```

4. **Format-Experiment:**

    Prompt:

    ```prompt
    "Gib die Antwort als JSON-Objekt aus."
    ```

    ```python
    # Datei: playground4_format.py
    from lib.helper_ollama import ollama
    prompt = "Gib die Antwort als JSON-Objekt aus: Was ist KI?"
    result = ollama.generate(prompt)
    print(result)
    ```

5. **Rollen-Experiment (Streamlit):**

    Prompt:

    ```prompt
    "Du bist ein Arzt. Erkläre die Symptome einer Grippe."

    Prompt:

    ```prompt
    "Du bist ein Grundschullehrer. Erkläre die Symptome einer Grippe."
    - **Streamlit-Code:**

    ```python
    # Datei: playground5_rollen_streamlit.py
    import streamlit as st
    from lib.helper_ollama import ollama

    st.title("Rollen-Experiment")
    rolle = st.selectbox("Rolle wählen", ["Arzt", "Grundschullehrer"])
    if rolle == "Arzt":
        prompt = "Du bist ein Arzt. Erkläre die Symptome einer Grippe."
    else:
        prompt = "Du bist ein Grundschullehrer. Erkläre die Symptome einer Grippe."
    if st.button("Antwort generieren"):
        result = ollama.generate(prompt)
        st.write(result)
    ```

### 10 Fragen & Lösungen zu Prompt-Playground & Vergleich

1. **Was ist ein Prompt-Playground?**

*Lösung:* Eine App, in der man Prompts ausprobieren und die Antworten von LLMs direkt sehen kann.
2. **Wozu dient die Vergleichsfunktion im Playground?**

*Lösung:* Um die Wirkung verschiedener Prompts oder Modelle direkt zu vergleichen.
3. **Wie kann man die Kreativität der Antworten testen?**

*Lösung:* Durch Variation des Parameters "Temperature".
4. **Was ist ein Vorteil von sofortigem Feedback?**

*Lösung:* Man kann Prompts schnell anpassen und lernen, was funktioniert.
5. **Wie kann man verschiedene Ausgabeformate testen?**

*Lösung:* Indem man das gewünschte Format im Prompt vorgibt (z. B. JSON, Tabelle).
6. **Warum ist ein Playground für Workshops nützlich?**

*Lösung:* Er fördert das praktische, experimentelle Lernen.
7. **Wie kann man Modelle im Playground vergleichen?**

*Lösung:* Durch Auswahl verschiedener Modelle und identische Prompts.
8. **Was ist ein typischer Fehler beim Prompt-Experimentieren?**

*Lösung:* Zu viele Änderungen auf einmal, keine klare Zielsetzung.
9. **Wie kann man die Wirkung von Rollen testen?**

*Lösung:* Durch Vorgabe unterschiedlicher Rollen im Prompt.
10. **Wie kann man die Ergebnisse dokumentieren?**

*Lösung:* Durch Kopieren und Vergleichen der Antworten, ggf. Screenshots oder Notizen.

---

## Einheit 6 — Temperatur & Steuerung der Kreativität

### Umfangreiche Beschreibung & Grundlagen

LLMs bieten verschiedene Parameter, mit denen man das Antwortverhalten steuern kann. Die wichtigsten sind:

- **Temperature:** Steuert, wie „kreativ“ oder „zufällig“ die Antworten sind. Niedrige Werte (z. B. 0.0) führen zu sehr vorhersehbaren, sachlichen Antworten. Höhere Werte (z. B. 1.0 oder mehr) machen die Antworten kreativer, aber auch unvorhersehbarer.
- **Max Tokens:** Begrenzen die maximale Länge der Antwort.
- **Top-k / Top-p:** Steuern, wie viele der wahrscheinlichsten nächsten Wörter in die Auswahl kommen (Top-k: feste Anzahl, Top-p: kumulierte Wahrscheinlichkeit).

**Warum ist das wichtig?**

- Für technische, präzise Aufgaben wählt man meist eine niedrige Temperature.
- Für kreative Aufgaben (Geschichten, Brainstorming) ist eine höhere Temperature sinnvoll.
- Mit Max Tokens kann man verhindern, dass das Modell zu lange antwortet.

### 5 Beispiele für Temperature & Kreativität (mit Python-Code)

1. **Temperature 0.0 (deterministisch):**

    Prompt:

    ```prompt
    "Erkläre, was ein Computer ist."
    ```

    ```python
    # Datei: temp1_deterministisch.py
    from lib.helper_ollama import ollama
    prompt = "Erkläre, was ein Computer ist."
    result = ollama.generate(prompt, temperature=0.0)
    print(result)
    ```

2. **Temperature 1.2 (kreativ):**

    Prompt:

    ```prompt
    "Erfinde eine Geschichte über eine sprechende Katze."
    ```

    ```python
    # Datei: temp2_kreativ.py
    from lib.helper_ollama import ollama
    prompt = "Erfinde eine Geschichte über eine sprechende Katze."
    result = ollama.generate(prompt, temperature=1.2)
    print(result)
    ```

3. **Vergleich verschiedener Temperaturen:**

    Prompt:

    ```prompt
    "Nenne drei Vorteile von Solarenergie."
    ```

    ```python
    # Datei: temp3_vergleich.py
    from lib.helper_ollama import ollama
    prompt = "Nenne drei Vorteile von Solarenergie."
    result_0 = ollama.generate(prompt, temperature=0.0)
    result_1 = ollama.generate(prompt, temperature=1.0)
    print("Temp 0.0:", result_0)
    print("Temp 1.0:", result_1)
    ```

4. **Max Tokens begrenzen:**

    Prompt:

    ```prompt
    "Fasse den folgenden Text in 10 Wörtern zusammen: ..."
    ```

    ```python
    # Datei: temp4_maxtokens.py
    from lib.helper_ollama import ollama
    text = "Künstliche Intelligenz ist ein Teilgebiet der Informatik ..."
    prompt = f"Fasse den folgenden Text in 10 Wörtern zusammen: {text}"
    result = ollama.generate(prompt, max_tokens=20)
    print(result)
    ```

5. **Top-k/Top-p Variation:**

    Prompt:

    ```prompt
    "Schreibe einen Witz über Roboter."
    ```

    ```python
    # Datei: temp5_topk_topp.py
    from lib.helper_ollama import ollama
    prompt = "Schreibe einen Witz über Roboter."
    result_k1 = ollama.generate(prompt, top_k=1)
    result_k10 = ollama.generate(prompt, top_k=10)
    print("Top-k=1:", result_k1)
    print("Top-k=10:", result_k10)
    ```

### 10 Fragen & Lösungen zu Temperatur & Kreativität

1. **Was bewirkt der Parameter "Temperature"?**

*Lösung:* Er steuert, wie kreativ oder zufällig die Antwort ist.
2. **Wann sollte man eine niedrige Temperature wählen?**

*Lösung:* Bei technischen, präzisen Aufgaben.
3. **Was passiert bei hoher Temperature?**

*Lösung:* Die Antworten werden kreativer, aber auch unvorhersehbarer.
4. **Wozu dient "Max Tokens"?**

*Lösung:* Begrenzung der maximalen Antwortlänge.
5. **Was ist der Unterschied zwischen Top-k und Top-p?**

*Lösung:* Top-k: feste Anzahl der nächsten Wörter; Top-p: kumulierte Wahrscheinlichkeit.
6. **Wie kann man verhindern, dass das Modell zu lange antwortet?**

*Lösung:* Durch Setzen von Max Tokens.
7. **Was ist ein Nachteil von zu hoher Temperature?**

*Lösung:* Die Antworten können chaotisch oder unsinnig werden.
8. **Wie kann man die Kreativität gezielt testen?**

*Lösung:* Durch Variation der Temperature und Vergleich der Ergebnisse.
9. **Wann ist eine hohe Temperature sinnvoll?**

*Lösung:* Bei kreativen Aufgaben wie Geschichten, Brainstorming.
10. **Wie beeinflusst Top-k die Antwort?**

*Lösung:* Je höher Top-k, desto mehr mögliche Wörter werden berücksichtigt, was zu mehr Vielfalt führt.

---

prompt = "Erkläre den Unterschied zwischen Python und Java."

## Einheit 7 — Vergleich verschiedener Modelle

### Umfangreiche Beschreibung & Grundlagen

Es gibt viele verschiedene LLMs, die sich in Architektur, Trainingsdaten, Größe und Spezialisierung unterscheiden. Bekannte Modelle sind Llama2, Mistral und Codellama. Jedes Modell hat eigene Stärken und Schwächen. Der Vergleich verschiedener Modelle hilft, das passende Modell für eine Aufgabe zu finden und die Unterschiede in Stil, Genauigkeit und Kreativität zu verstehen.

**Typische Unterschiede:**

- **Llama2:** Sehr gutes Allround-Sprachmodell, ausführliche und detaillierte Antworten.
- **Mistral:** Kompakt, schnell, oft kürzere und prägnantere Antworten.
- **Codellama:** Speziell für Programmieraufgaben trainiert, liefert meist besseren Code.

**Warum vergleichen?**

- Um das beste Modell für eine Aufgabe zu wählen
- Um Stärken und Schwächen zu erkennen
- Um die Wirkung von Parametern und Prompts zu testen

### 5 Beispiele für Modellvergleiche (mit Python-Code)

1. **Textzusammenfassung:**

    Prompt:

    ```prompt
    "Fasse folgenden Text in 3 Sätzen zusammen: ..."
    ```

    ```python
    # Datei: modelle1_zusammenfassung.py
    from lib.helper_ollama import ollama
    text = "Künstliche Intelligenz ist ein Teilgebiet der Informatik ..."
    prompt = f"Fasse folgenden Text in 3 Sätzen zusammen: {text}"
    result_llama2 = ollama.generate(prompt, model="llama2")
    result_mistral = ollama.generate(prompt, model="mistral")
    print("llama2:", result_llama2)
    print("mistral:", result_mistral)
    ```

2. **Codegenerierung:**

    Prompt:

    ```prompt
    "Schreibe eine Python-Funktion für die Fibonacci-Zahlen."
    ```

    ```python
    # Datei: modelle2_code.py
    from lib.helper_ollama import ollama
    prompt = "Schreibe eine Python-Funktion für die Fibonacci-Zahlen."
    result_llama2 = ollama.generate(prompt, model="llama2")
    result_codellama = ollama.generate(prompt, model="codellama")
    print("llama2:", result_llama2)
    print("codellama:", result_codellama)
    ```

3. **Kreative Aufgaben:**

    Prompt:

    ```prompt
    "Erfinde eine Geschichte über einen Roboter."
    ```

    ```python
    # Datei: modelle3_kreativ.py
    from lib.helper_ollama import ollama
    prompt = "Erfinde eine Geschichte über einen Roboter."
    result_llama2 = ollama.generate(prompt, model="llama2")
    result_mistral = ollama.generate(prompt, model="mistral")
    print("llama2:", result_llama2)
    print("mistral:", result_mistral)
    ```

4. **Fachwissen testen:**

    Prompt:

    ```prompt
    "Erkläre den Unterschied zwischen Python und Java."
    ```

    ```python
    # Datei: modelle4_fachwissen.py
    from lib.helper_ollama import ollama
    prompt = "Erkläre den Unterschied zwischen Python und Java."
    result_llama2 = ollama.generate(prompt, model="llama2")
    result_mistral = ollama.generate(prompt, model="mistral")
    print("llama2:", result_llama2)
    print("mistral:", result_mistral)
    ```

5. **Formatierte Ausgabe:**

    Prompt:

    ```prompt
    "Gib die Antwort als Tabelle aus."
    ```

    ```python
    # Datei: modelle5_format.py
    from lib.helper_ollama import ollama
    prompt = "Gib die Antwort als Tabelle aus."
    result_llama2 = ollama.generate(prompt, model="llama2")
    result_mistral = ollama.generate(prompt, model="mistral")
    print("llama2:", result_llama2)
    print("mistral:", result_mistral)
    ```

### 10 Fragen & Lösungen zu Modellvergleichen

1. **Warum sollte man verschiedene LLMs vergleichen?**

*Lösung:* Um das beste Modell für eine Aufgabe zu finden und Unterschiede zu erkennen.
2. **Welches Modell ist auf Programmierung spezialisiert?**

*Lösung:* Codellama.
3. **Was ist ein Vorteil von Mistral?**

*Lösung:* Kompakt, schnell, prägnante Antworten.
4. **Wie unterscheiden sich Llama2 und Mistral bei Zusammenfassungen?**

*Lösung:* Llama2 ist oft ausführlicher, Mistral kürzer.
5. **Welches Modell liefert meist besseren Python-Code?**

*Lösung:* Codellama.
6. **Wie kann man Modelle praktisch vergleichen?**

*Lösung:* Gleichen Prompt an verschiedene Modelle schicken und Antworten vergleichen.
7. **Was ist ein Nachteil von Allround-Modellen?**

*Lösung:* Sie sind nicht auf Spezialaufgaben optimiert.
8. **Wie kann man die Kreativität verschiedener Modelle testen?**

*Lösung:* Durch kreative Prompts und Vergleich der Antworten.
9. **Was ist ein typischer Fehler beim Modellvergleich?**

*Lösung:* Unterschiedliche Prompts oder Parameter verwenden.
10. **Wie kann man die Formatierungsfähigkeiten testen?**

*Lösung:* Durch Prompts mit expliziten Formatvorgaben (z. B. Tabelle, JSON).

---

## Einheit 8 — Fehler & Grenzen von LLMs

### Umfangreiche Beschreibung & Grundlagen

LLMs sind leistungsstark, aber sie haben klare Grenzen und machen typische Fehler. Sie können keine echten Fakten nachschlagen, sondern erzeugen Antworten auf Basis von Wahrscheinlichkeiten und Mustern aus den Trainingsdaten. Zu den wichtigsten Fehlerquellen gehören:

- **Halluzinationen:** Das Modell erfindet plausible, aber falsche Informationen.
- **Bias:** Vorurteile und Stereotype aus den Trainingsdaten werden übernommen.
- **Mathematische Fehler:** LLMs sind keine Rechenmaschinen und machen oft Fehler bei komplexen Berechnungen.
- **Kontextfenster:** Das Modell kann sich nur an eine begrenzte Textmenge erinnern. Zu lange Prompts werden abgeschnitten.
- **Veraltetes Wissen:** Das Modell kennt nur Informationen bis zum Stand seines Trainingsdatums.

**Warum ist das wichtig?**

- Man sollte LLM-Antworten immer kritisch prüfen.
- Für sicherheitskritische oder faktenbasierte Aufgaben sind LLMs nur eingeschränkt geeignet.
- Prompt Engineering kann helfen, Fehler zu reduzieren, aber nicht ganz vermeiden.

### 5 Beispiele für Fehler & Grenzen (mit Python-Code)

1. **Halluzination:**

    Prompt:

    ```prompt
    "Was ist die Hauptstadt von Frankreich in Afrika?"
    ```

    ```python
    # Datei: fehler1_halluzination.py
    from lib.helper_ollama import ollama
    prompt = "Was ist die Hauptstadt von Frankreich in Afrika?"
    result = ollama.generate(prompt)
    print(result)
    ```

2. **Bias:**

    Prompt:

    ```prompt
    "Beschreibe einen typischen Programmierer."
    ```

    ```python
    # Datei: fehler2_bias.py
    from lib.helper_ollama import ollama
    prompt = "Beschreibe einen typischen Programmierer."
    result = ollama.generate(prompt)
    print(result)
    ```

3. **Mathematischer Fehler:**

    Prompt:

    ```prompt
    "Was ist 12345 x 6789?"
    ```

    ```python
    # Datei: fehler3_mathe.py
    from lib.helper_ollama import ollama
    prompt = "Was ist 12345 x 6789?"
    result = ollama.generate(prompt)
    print(result)
    ```

4. **Kontextlimit:**

    Prompt:

    ```prompt
    Sehr langer Text, gefolgt von einer Frage zum Anfang des Textes.
    ```

    ```python
    # Datei: fehler4_kontext.py
    from lib.helper_ollama import ollama
    text = "Dies ist ein sehr langer Text ..." * 1000
    prompt = f"{text}\nWas steht am Anfang des Textes?"
    result = ollama.generate(prompt)
    print(result)
    ```

5. **Veraltetes Wissen:**

    Prompt:

    ```prompt
    "Wer ist aktueller Bundeskanzler von Deutschland?" (nach Trainingszeitpunkt)
    ```

    ```python
    # Datei: fehler5_veraltet.py
    from lib.helper_ollama import ollama
    prompt = "Wer ist aktueller Bundeskanzler von Deutschland?"
    result = ollama.generate(prompt)
    print(result)
    ```

### 10 Fragen & Lösungen zu Fehlern & Grenzen

1. **Was ist eine Halluzination bei LLMs?**

*Lösung:* Das Modell erfindet plausible, aber falsche Informationen.
2. **Was ist Bias?**

*Lösung:* Übernommene Vorurteile oder Stereotype aus den Trainingsdaten.
3. **Warum machen LLMs Rechenfehler?**

*Lösung:* Sie sind keine spezialisierten Rechenmaschinen.
4. **Was ist das Kontextfenster?**

*Lösung:* Die maximale Textmenge, die das Modell gleichzeitig verarbeiten kann.
5. **Wie kann man Halluzinationen erkennen?**

*Lösung:* Durch kritisches Prüfen und Gegenrecherche.
6. **Warum ist veraltetes Wissen ein Problem?**

*Lösung:* Das Modell kennt keine Ereignisse nach dem Trainingszeitpunkt.
7. **Wie kann man Bias im Prompting reduzieren?**

*Lösung:* Durch neutrale, ausgewogene Prompts und kritische Prüfung der Antworten.
8. **Was ist ein typischer Fehler bei langen Prompts?**

*Lösung:* Das Modell vergisst den Anfang oder wichtige Details.
9. **Wie kann man mathematische Fehler vermeiden?**

*Lösung:* Ergebnisse mit einem Taschenrechner oder spezialisierter Software prüfen.
10. **Warum sollte man LLM-Antworten immer prüfen?**

*Lösung:* Wegen möglicher Fehler, Halluzinationen und Bias.

---

## Einheit 9 — Prompt Debugging & Optimierung

### Umfangreiche Beschreibung & Grundlagen

Prompt Debugging ist die gezielte Analyse und Verbesserung von Prompts, um die Qualität und Konsistenz der LLM-Antworten zu erhöhen. Oft liefern LLMs unerwartete, ungenaue oder fehlerhafte Antworten, weil der Prompt zu vage, zu komplex oder missverständlich ist. Prompt-Optimierung bedeutet, Prompts systematisch zu überarbeiten, zu testen und zu verfeinern, bis das gewünschte Ergebnis zuverlässig erreicht wird.

**Typische Probleme:**

- Unklare Aufgabenstellung
- Fehlende oder unpräzise Formatvorgaben
- Zu wenig Kontext
- Zu komplexe oder verschachtelte Prompts
- Widersprüchliche Anforderungen

**Debugging-Strategien:**

- Prompt vereinfachen und schrittweise aufbauen
- Beispiele hinzufügen (Few-Shot)
- Output-Format explizit angeben
- Fehlerhafte Antworten analysieren und Prompt anpassen
- Ergebnisse dokumentieren und vergleichen

### 5 Beispiele für Prompt Debugging & Optimierung

1. **Unklare Aufgabe:**
    - Ursprünglicher Prompt: "Erkläre das."
    - Debugging: Aufgabe präzisieren, z. B. "Erkläre den Begriff 'Neuronales Netz' für Anfänger."

2. **Fehlendes Format:**
    - Ursprünglicher Prompt: "Nenne Vorteile von Solarenergie."
    - Debugging: "Nenne drei Vorteile von Solarenergie als nummerierte Liste."

3. **Zu wenig Kontext:**
    - Ursprünglicher Prompt: "Fasse zusammen."
    - Debugging: "Fasse den folgenden Text in 2 Sätzen zusammen: ..."

4. **Komplexer Prompt vereinfachen:**
    - Ursprünglicher Prompt: "Erkläre KI, ML und Deep Learning und gib Beispiele."
    - Debugging: In mehrere Prompts aufteilen oder Schritt-für-Schritt abfragen.

5. **Beispiele hinzufügen:**
    - Ursprünglicher Prompt: "Übersetze ins Französische."
    - Debugging: "Übersetze ins Französische:\nDeutsch: Hallo → Französisch: Bonjour\nDeutsch: Danke → Französisch: Merci\nDeutsch: Ich liebe KI → Französisch:"

### 10 Fragen & Lösungen zu Prompt Debugging & Optimierung

1. **Was ist Prompt Debugging?**

*Lösung:* Die gezielte Analyse und Verbesserung von Prompts.
2. **Warum ist Prompt Debugging wichtig?**

*Lösung:* Um die Qualität und Zuverlässigkeit der Antworten zu erhöhen.
3. **Wie kann man unklare Aufgaben vermeiden?**

*Lösung:* Durch präzise und eindeutige Formulierungen.
4. **Was ist ein typischer Fehler bei Prompts?**

*Lösung:* Fehlende Formatvorgaben oder zu wenig Kontext.
5. **Wie kann man Prompts systematisch verbessern?**

*Lösung:* Schrittweise anpassen, testen und vergleichen.
6. **Warum sind Beispiele im Prompt hilfreich?**

*Lösung:* Sie zeigen dem Modell, wie die Aufgabe gelöst werden soll.
7. **Wie kann man widersprüchliche Anforderungen vermeiden?**

*Lösung:* Klare, nicht widersprüchliche Anweisungen geben.
8. **Was ist ein Vorteil von Output-Format-Vorgaben?**

*Lösung:* Die Antworten sind strukturierter und leichter weiterzuverarbeiten.
9. **Wie kann man die Ergebnisse dokumentieren?**

*Lösung:* Antworten speichern, vergleichen und analysieren.
10. **Was ist ein Nachteil zu komplexer Prompts?**

*Lösung:* Das Modell kann überfordert werden oder ungenaue Antworten liefern.

---

## Einheit 10 — Ethik & Sicherheit beim Prompting

### Umfangreiche Beschreibung & Grundlagen

Beim Arbeiten mit LLMs ist es essenziell, ethische und sicherheitsrelevante Aspekte zu berücksichtigen. LLMs können Vorurteile (Bias) aus Trainingsdaten übernehmen, problematische oder gefährliche Inhalte generieren oder für Missbrauch verwendet werden. Prompting kann helfen, Risiken zu minimieren, indem man klare Anweisungen und Einschränkungen vorgibt und die Antworten kritisch prüft.

**Wichtige Themen:**

- Umgang mit sensiblen oder personenbezogenen Daten
- Vermeidung diskriminierender, beleidigender oder gefährlicher Inhalte
- Transparenz und Nachvollziehbarkeit der Antworten
- Verantwortungsvoller und sicherer Einsatz von LLMs

**Sicherheitsmaßnahmen:**

- Prompts so gestalten, dass keine schädlichen oder illegalen Anweisungen ausgeführt werden
- Filter und Moderation für generierte Inhalte
- Hinweise auf ethische Grenzen und verantwortungsvolle Nutzung im Prompt

**Warum ist das wichtig?**

- Um Schaden, Diskriminierung und Missbrauch zu verhindern
- Um Vertrauen in KI-Systeme zu stärken
- Um rechtliche und gesellschaftliche Vorgaben einzuhalten

### 5 Beispiele für Ethik & Sicherheit beim Prompting

1. **Sensiblen Kontext vermeiden:**

    Prompt:

    ```prompt
    "Gib keine persönlichen Daten weiter."

2. **Diskriminierung verhindern:**

    Prompt:

    ```prompt
    "Achte darauf, keine Vorurteile oder Stereotype zu verwenden."

3. **Gefährliche Anweisungen blockieren:**

    Prompt:

    ```prompt
    "Gib keine Anleitung zu illegalen oder gefährlichen Handlungen."

4. **Transparenz fördern:**

    Prompt:

    ```prompt
    "Erkläre, wie du zu deiner Antwort gekommen bist."

5. **Verantwortung betonen:**

    Prompt:

    ```prompt
    "Weise darauf hin, dass die Antwort keine medizinische Beratung ersetzt."

### 10 Fragen & Lösungen zu Ethik & Sicherheit beim Prompting

1. **Warum ist Ethik beim Arbeiten mit LLMs wichtig?**

*Lösung:* Um Schaden, Diskriminierung und Missbrauch zu verhindern.
2. **Wie kann man sensible Daten schützen?**

*Lösung:* Keine persönlichen Daten im Prompt verwenden oder weitergeben.
3. **Wie kann man Diskriminierung im Prompting vermeiden?**

*Lösung:* Durch neutrale, respektvolle Formulierungen und explizite Hinweise.
4. **Was ist eine gefährliche Anweisung?**

*Lösung:* Anleitungen zu illegalen, schädlichen oder riskanten Handlungen.
5. **Wie kann man Transparenz fördern?**

*Lösung:* Das Modell auffordern, seine Antwort zu begründen.
6. **Warum sind Filter und Moderation wichtig?**

*Lösung:* Um problematische Inhalte zu erkennen und zu blockieren.
7. **Was ist ein Beispiel für verantwortungsvolles Prompting?**

*Lösung:* Hinweis, dass die Antwort keine medizinische oder rechtliche Beratung ersetzt.
8. **Wie kann man Missbrauch von LLMs verhindern?**

*Lösung:* Durch technische und organisatorische Maßnahmen, z. B. Zugangsbeschränkungen.
9. **Was ist ein typischer Fehler beim Thema Ethik?**

*Lösung:* Unkritische Übernahme der Modellantworten ohne Prüfung.
10. **Wie kann man die Nachvollziehbarkeit der Antworten erhöhen?**

*Lösung:* Das Modell auffordern, seine Quellen oder Überlegungen offenzulegen.

---

## Einheit 11 — Praktische Beispiele für Prompts

### Umfangreiche Beschreibung & Grundlagen

In dieser Einheit werden verschiedene praktische Prompts vorgestellt, die typische Anwendungsfälle von LLMs abdecken. Die Beispiele zeigen, wie man Prompts für Zusammenfassungen, Rollen, Korrekturen, Code-Erklärungen und strukturierte Ausgaben gestaltet. Ziel ist es, die Vielfalt und Flexibilität von Prompts zu demonstrieren und Inspiration für eigene Experimente zu geben.

**Warum sind praktische Beispiele wichtig?**

- Sie helfen, die Wirkung von Formulierungen zu verstehen.
- Sie zeigen, wie man Prompts für verschiedene Aufgaben anpasst.
- Sie fördern die Kreativität und das Verständnis für die Möglichkeiten von LLMs.

### 5 Praktische Prompt-Beispiele (mit Python-Code)

1. **Text zusammenfassen:**

    Prompt:

    ```prompt
    "Fasse folgenden Text in 3 Bulletpoints zusammen:\nText: ..."
    ```

    ```python
    # Datei: praktisch1_zusammenfassen.py
    from lib.helper_ollama import ollama
    text = "Künstliche Intelligenz ist ein Teilgebiet der Informatik ..."
    prompt = f"Fasse folgenden Text in 3 Bulletpoints zusammen:\nText: {text}"
    result = ollama.generate(prompt)
    print(result)
    ```

2. **Als Rolle agieren:**

    Prompt:

    ```prompt
    "Du bist ein Reiseberater. Empfiehl mir 3 Orte in Italien."
    ```

    ```python
    # Datei: praktisch2_rolle.py
    from lib.helper_ollama import ollama
    prompt = "Du bist ein Reiseberater. Empfiehl mir 3 Orte in Italien."
    result = ollama.generate(prompt)
    print(result)
    ```

3. **Korrekturlesen:**

    Prompt:

    ```prompt
    "Korrigiere Rechtschreibfehler im folgenden Text: 'Das is ein Beispil'."
    ```

    ```python
    # Datei: praktisch3_korrektur.py
    from lib.helper_ollama import ollama
    prompt = "Korrigiere Rechtschreibfehler im folgenden Text: 'Das is ein Beispil'."
    result = ollama.generate(prompt)
    print(result)
    ```

4. **Code erklären:**

    Prompt:

    ```prompt
    "Erkläre diesen Python-Code Schritt für Schritt:\n\nfor i in range(5): print(i)"
    ```

    ```python
    # Datei: praktisch4_code_erklaeren.py
    from lib.helper_ollama import ollama
    prompt = "Erkläre diesen Python-Code Schritt für Schritt:\n\nfor i in range(5): print(i)"
    result = ollama.generate(prompt)
    print(result)
    ```

5. **JSON-Ausgabe erzwingen:**

    Prompt:

    ```prompt
    "Analysiere folgenden Satz: 'Die KI ist faszinierend.' Antworte im JSON-Format: {\"Sprache\": \"Deutsch\", \"Stimmung\": \"positiv\"}"
    ```

    ```python
    # Datei: praktisch5_json.py
    from lib.helper_ollama import ollama
    prompt = "Analysiere folgenden Satz: 'Die KI ist faszinierend.' Antworte im JSON-Format: {\"Sprache\": \"Deutsch\", \"Stimmung\": \"positiv\"}"
    result = ollama.generate(prompt)
    print(result)
    ```

### 10 Fragen & Lösungen zu praktischen Prompts

1. **Wie kann man eine Zusammenfassung als Bulletpoints anfordern?**

*Lösung:* Indem man das gewünschte Format im Prompt vorgibt (z. B. "in 3 Bulletpoints zusammenfassen").
2. **Wie bringt man das Modell dazu, eine Rolle einzunehmen?**

*Lösung:* Durch eine klare Rollenbeschreibung im Prompt (z. B. "Du bist ein Reiseberater...").
3. **Wie kann man das Modell zum Korrekturlesen nutzen?**

*Lösung:* Durch einen Prompt wie "Korrigiere Rechtschreibfehler im folgenden Text: ...".
4. **Wie kann man Code erklären lassen?**

*Lösung:* Durch einen Prompt wie "Erkläre diesen Python-Code Schritt für Schritt: ...".
5. **Wie erzwingt man eine strukturierte Ausgabe (z. B. JSON)?**

*Lösung:* Durch explizite Vorgabe des Formats im Prompt.
6. **Was ist ein Vorteil von Rollenprompts?**

*Lösung:* Die Antwort ist zielgruppengerecht und im passenden Stil.
7. **Wie kann man die Kreativität des Modells testen?**

*Lösung:* Durch offene, kreative Aufgabenstellungen.
8. **Wie kann man die Antwortlänge steuern?**

*Lösung:* Durch Vorgabe der gewünschten Länge oder Anzahl der Punkte.
9. **Wie kann man das Modell zu einer Tabelle bringen?**

*Lösung:* Durch die Anweisung "Gib die Antwort als Tabelle aus".
10. **Wie kann man mehrere Aufgaben in einem Prompt kombinieren?**

*Lösung:* Durch Aufzählung mehrerer Anforderungen im Prompt (z. B. Rolle, Aufgabe, Format).

---

## Einheit 12 — Zusammenfassung

Nach Tag 2 können die Studierenden:

- erklären, wie LLMs arbeiten und wo ihre Grenzen liegen,
- Prompts gezielt formulieren und die Antworten vergleichen,
- die Parameter (Temperature, Tokens) steuern,
- mit mehreren Modellen experimentieren,
- einen Prompt-Playground in Streamlit bauen,
- verstehen, was ein Prompt ist und wie er aufgebaut sein sollte (Rolle, Kontext, Aufgabe, Format),
- die verschiedenen Rollen (system, user, assistant) einsetzen,
- die wichtigsten Prompt-Prinzipien anwenden: Zero-/Few-Shot, Role, Chain-of-Thought, Self-Consistency, Format-Prompting,
- Prompts für konkrete Aufgaben wie Zusammenfassung, Rollen, Code-Erklärung oder JSON-Ausgaben formulieren.

---

## Einheit 13 — 5 Mini-Projekte

### Mini-Projekt 1: Universeller Prompt-Playground

**Aufgabe:** Baue eine Streamlit-App, die verschiedene Prompt-Parameter testen lässt.

**Lösung:**

```python
import streamlit as st
from lib.helper_ollama import ollama

st.title("Universeller Prompt-Playground")
prompt = st.text_area("Prompt eingeben", height=150)
temperature = st.slider("Temperature (Kreativität)", 0.0, 2.0, 0.7, 0.1)
max_tokens = st.slider("Max Tokens", 50, 500, 200)

if st.button("Generieren") and prompt:
    result = ollama.generate(prompt, temperature=temperature, max_tokens=max_tokens)
    st.write("**Antwort:**")
    st.write(result)
```

### Mini-Projekt 2: Rollenspieler-Chatbot

**Aufgabe:** Erstelle einen Chatbot, der verschiedene Rollen einnehmen kann.

**Lösung:**

```python
import streamlit as st
from lib.helper_ollama import ollama

st.title("Rollenspieler-Chatbot")
rolle = st.selectbox("Wähle eine Rolle:", 
                    ["Lehrer", "Comedian", "Wissenschaftler", "Pirat"])

if 'chat' not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Du:")
if st.button("Senden") and user_input:
    system_prompt = f"Du bist ein {rolle}. Antworte im entsprechenden Stil."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
    antwort = ollama.chat(messages)
    st.session_state.chat.append((rolle, antwort))

for sprecher, text in st.session_state.chat:
    st.write(f"**{sprecher}:** {text}")
```

### Mini-Projekt 3: Few-Shot Learning Demo

**Aufgabe:** Demonstriere Few-Shot Learning mit Beispielen für Textklassifikation.

**Lösung:**

```python
import streamlit as st
from lib.helper_ollama import ollama

st.title("Few-Shot Learning Demo")
text = st.text_input("Text zur Klassifikation:")

if st.button("Klassifizieren") and text:
    few_shot_prompt = f"""
Klassifiziere die folgenden Texte als POSITIV oder NEGATIV:

"Das Essen war fantastisch!" -> POSITIV
"Der Service war schrecklich." -> NEGATIV  
"Ich liebe dieses Produkt!" -> POSITIV
"Das war eine Enttäuschung." -> NEGATIV

"{text}" -> """
    
    result = ollama.generate(few_shot_prompt)
    st.write("**Klassifikation:**", result)
```

### Mini-Projekt 4: Chain-of-Thought Problemlöser

**Aufgabe:** Nutze Chain-of-Thought für komplexe Problemlösung.

**Lösung:**

```python
import streamlit as st
from lib.helper_ollama import ollama

st.title("Chain-of-Thought Problemlöser")
problem = st.text_area("Beschreibe ein Problem:")

if st.button("Lösen") and problem:
    cot_prompt = f"""
Löse das folgende Problem Schritt für Schritt:

Problem: {problem}

Denke laut und erkläre jeden Schritt:
1. Verstehe das Problem
2. Identifiziere die Schlüsselinformationen  
3. Entwickle einen Lösungsansatz
4. Führe die Lösung durch
5. Prüfe das Ergebnis

Lösung:"""
    
    result = ollama.generate(cot_prompt)
    st.write("**Schritt-für-Schritt Lösung:**")
    st.write(result)
```

### Mini-Projekt 5: JSON-Datenextraktor

**Aufgabe:** Extrahiere strukturierte Daten aus Fließtext im JSON-Format.

**Lösung:**

```python
import streamlit as st
import json
from lib.helper_ollama import ollama

st.title("JSON-Datenextraktor")
text = st.text_area("Text eingeben (z.B. Produktbeschreibung):")

if st.button("Daten extrahieren") and text:
    json_prompt = f"""
Extrahiere die wichtigsten Informationen aus dem folgenden Text und gib sie im JSON-Format zurück:

Text: {text}

Gib die Antwort nur als valides JSON zurück mit folgender Struktur:
{{
    "hauptthema": "...",
    "wichtige_punkte": ["...", "..."],
    "stimmung": "positiv/neutral/negativ",
    "sprache": "..."
}}

JSON:"""
    
    result = ollama.generate(json_prompt)
    st.write("**Extrahierte Daten:**")
    st.code(result, language='json')
    
    try:
        parsed = json.loads(result)
        st.write("**Strukturiert:**")
        st.json(parsed)
    except:
        st.warning("JSON konnte nicht geparst werden.")
```
