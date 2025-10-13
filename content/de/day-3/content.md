# Tag 3 — Datenverarbeitung & KI-Anwendungen

## Einheit 0 - Zeitplan 09:00 – 15:00

### Übersicht

Der Tag vermittelt praxisnah die Grundlagen der KI-Textanalyse mit Ollama und Python. Jede Einheit besteht aus einer kurzen Erklärung, Beispielen und praktischen Übungen.

---

### Zeitplan

| Zeit            | Einheit / Inhalt                                                                 | Dauer   |
|-----------------|----------------------------------------------------------------------------------|---------|
| **09:00 – 09:20** | Einführung & Überblick - Motivation, Ziele, KI-Anwendungen      | 20 min  |
| **09:20 – 09:50** | **Einheit 3.1:** Einführung in Textanalyse - Grundbegriffe, Aufgaben | 30 min  |
| **09:50 – 10:30** | **Einheit 3.2:** Sentimentanalyse - Stimmung erkennen, Beispiele, Übungen | 40 min  |
| **10:30 – 11:10** | **Einheit 3.3:** Themenklassifikation - Kategorien, Labeling, Übungen | 40 min  |
| **11:10 – 11:25** | ☕ **Pause**                                                                    | 15 min  |
| **11:25 – 12:00** | **Einheit 3.4:** Schlüsselwort-Extraktion - Keywords, Listen, Übungen | 35 min  |
| **12:00 – 12:35** | **Einheit 3.5:** Named Entity Recognition (NER) - Personen, Orte, Organisationen | 35 min  |
| **12:35 – 13:35** | 🍽️ **Mittagspause**                                                            | 60 min  |
| **13:35 – 14:05** | **Einheit 3.6:** FAQ-Bot mit Ollama - FAQ-Upload, Bot-Logik, Übungen | 30 min  |
| **14:05 – 14:35** | **Einheit 3.7:** Kombination von Analysen - Sentiment + Keywords + Entities | 30 min  |
| **14:35 – 15:00** | **Einheit 3.8:** Analyse-Dashboard mit Streamlit - App bauen, Zusammenfassung | 25 min  |

---



---

## Einheit 1 — Einführung in Textanalyse

### Umfangreiche Beschreibung & Grundlagen

Textanalyse (Natural Language Processing, NLP) ist ein zentrales Anwendungsfeld der Künstlichen Intelligenz. Sie umfasst Methoden, um aus unstrukturiertem Text strukturierte Informationen zu gewinnen. Typische Aufgaben sind:

- **Klassifikation:** Einordnung von Texten in Themen, Kategorien oder Labels (z. B. Sport, Politik, Technik)
- **Sentimentanalyse:** Bewertung der Stimmung (positiv, negativ, neutral)
- **Schlüsselwort-Extraktion:** Herausfiltern der wichtigsten Begriffe
- **Named Entity Recognition (NER):** Erkennen von Eigennamen wie Personen, Orten, Organisationen
- **Zusammenfassung:** Komplexe Texte auf das Wesentliche reduzieren

LLMs (Large Language Models) sind besonders gut für Textanalyse geeignet, da sie auf riesigen Textmengen trainiert wurden und semantische Zusammenhänge erkennen. Sie werden eingesetzt in Business Intelligence, Social Media Monitoring, Chatbots, Kundenfeedback, Suchmaschinen und vielen weiteren Bereichen.

**Warum ist Textanalyse wichtig?**

- Sie hilft, große Mengen an Text automatisch auszuwerten.
- Sie ermöglicht datengetriebene Entscheidungen auf Basis von Textdaten.
- Sie ist Grundlage für viele moderne KI-Anwendungen.

### 5 Beispiele für Textanalyse-Aufgaben (mit Python-Code)

1. **Kategorisierung:**

    Text:

    ```text
    "Lionel Messi schoss ein Tor."
    - Aufgabe: Thema erkennen → "Sport"
    ```

    ```python
    # Datei: beispiel1_kategorisierung.py
    from lib.helper_ollama import ollama

    text = "Lionel Messi schoss ein Tor."
    prompt = f"Ordne diesen Text einem Thema zu (Sport, Politik, Technik, Unterhaltung): {text}"
    result = ollama.generate(prompt)
    print("Thema:", result)
    ```

2. **Stimmungsanalyse:**

    Text:

    ```text
    "Das Produkt ist großartig!"
    - Aufgabe: Stimmung erkennen → "Positiv"
    ```

    ```python
    # Datei: beispiel2_sentiment.py
    from lib.helper_ollama import ollama

    text = "Das Produkt ist großartig!"
    prompt = f"Analysiere die Stimmung (Positiv, Negativ, Neutral): {text}"
    result = ollama.generate(prompt)
    print("Stimmung:", result)
    ```

3. **Schlüsselwörter extrahieren:**

    Text:

    ```text
    "Tesla bringt ein neues Elektroauto auf den Markt."
    - Aufgabe: Keywords → ["Tesla", "Elektroauto"]
    ```

    ```python
    # Datei: beispiel3_keywords.py
    from lib.helper_ollama import ollama

    text = "Tesla bringt ein neues Elektroauto auf den Markt."
    prompt = f"Extrahiere die wichtigsten Keywords als Python-Liste: {text}"
    result = ollama.generate(prompt)
    print("Keywords:", result)
    ```

4. **Named Entities finden:**

    Text:

    ```text
    "Angela Merkel traf Barack Obama in Berlin."
    - Aufgabe: Personen und Orte erkennen → ["Angela Merkel", "Barack Obama", "Berlin"]
    ```

    ```python
    # Datei: beispiel4_entities.py
    from lib.helper_ollama import ollama

    text = "Angela Merkel traf Barack Obama in Berlin."
    prompt = f"Finde Named Entities (Personen, Orte, Organisationen) als JSON: {text}"
    result = ollama.generate(prompt)
    print("Entities:", result)
    ```

5. **Zusammenfassung:**

    Text:

    ```text
    "Die Aktie von Tesla stieg nach der Präsentation eines neuen Modells um 10%."
    - Aufgabe: Kurze Zusammenfassung → "Tesla-Aktie steigt nach neuem Modell."
    ```

    ```python
    # Datei: beispiel5_zusammenfassung.py
    from lib.helper_ollama import ollama

    text = "Die Aktie von Tesla stieg nach der Präsentation eines neuen Modells um 10%."
    prompt = f"Fasse den folgenden Text in einem Satz zusammen: {text}"
    result = ollama.generate(prompt)
    print("Zusammenfassung:", result)
    ```

### 10 Fragen & Lösungen zu Textanalyse

1. **Was ist Textanalyse?**
    - *Lösung:* Die automatische Auswertung und Strukturierung von Texten durch KI.
2. **Nenne zwei typische Aufgaben der Textanalyse.**
    - *Lösung:* Klassifikation, Sentimentanalyse, Keyword-Extraktion, NER, Zusammenfassung (je zwei nennen)
3. **Warum sind LLMs für Textanalyse geeignet?**
    - *Lösung:* Sie erkennen semantische Zusammenhänge und sind auf großen Textmengen trainiert.
4. **Was ist Sentimentanalyse?**
    - *Lösung:* Die Erkennung der Stimmung eines Textes (positiv, negativ, neutral).
5. **Was versteht man unter Named Entity Recognition?**
    - *Lösung:* Das Erkennen von Eigennamen wie Personen, Orten, Organisationen.
6. **Wie kann Textanalyse im Business helfen?**
    - *Lösung:* Automatische Auswertung von Kundenfeedback, Social Media, Support-Tickets etc.
7. **Was ist ein Beispiel für eine Klassifikationsaufgabe?**
    - *Lösung:* Ein Text wird als "Sport" oder "Politik" klassifiziert.
8. **Wie kann man Schlüsselwörter aus Texten extrahieren?**
    - *Lösung:* Mit LLMs oder speziellen Algorithmen, z. B. durch Prompts wie "Extrahiere Keywords: ..."
9. **Was ist eine Zusammenfassung?**
    - *Lösung:* Die Reduktion eines Textes auf die wichtigsten Aussagen.
10. **Nenne ein Beispiel für den Einsatz von Textanalyse im Alltag.**
    - *Lösung:* Spam-Filter, Chatbots, automatische Übersetzungen, Produktempfehlungen.

---

## Einheit 2 — Sentimentanalyse (Stimmung erkennen)

### Umfangreiche Beschreibung & Grundlagen

Sentimentanalyse ist die automatische Erkennung der Stimmung in Texten. Sie wird häufig in Marketing, Social Media, Produktbewertungen und Kundenfeedback eingesetzt. Ziel ist es, herauszufinden, ob ein Text positiv, negativ oder neutral ist. LLMs sind besonders gut darin, weil sie viele Beispiele aus dem Internet kennen und Sprachnuancen erkennen können.

**Warum ist Sentimentanalyse wichtig?**

- Unternehmen können Trends und Meinungen erkennen.
- Sie hilft, Kundenfeedback automatisch auszuwerten.
- Sie ist Grundlage für automatisierte Moderation und Monitoring.

**Herausforderungen:**

- Ironie und Sarkasmus sind schwer zu erkennen.
- Gemischte Stimmungen in einem Text (z. B. "Service schlecht, Essen gut")
- Unterschiedliche Formulierungen für gleiche Gefühle

### 5 Beispiele für Sentimentanalyse (mit Python-Code)

1. **Einfache Analyse:**

    Text:

    ```text
    "Das Produkt ist super!"
    ```

    Ergebnis:

    ```text
    "Positiv"
    ```

    ```python
    # Datei: sentiment1_einfach.py
    from lib.helper_ollama import ollama

    text = "Das Produkt ist super!"
    prompt = f"Analysiere die Stimmung (Positiv, Negativ, Neutral): {text}"
    result = ollama.generate(prompt)
    print("Stimmung:", result)
    ```

2. **Negatives Feedback:**

    Text:

    ```text
    "Ich bin sehr enttäuscht von der Qualität."
    ```

    Ergebnis:

    ```text
    "Negativ"
    ```

    ```python
    # Datei: sentiment2_negativ.py
    from lib.helper_ollama import ollama

    text = "Ich bin sehr enttäuscht von der Qualität."
    prompt = f"Analysiere die Stimmung (Positiv, Negativ, Neutral): {text}"
    result = ollama.generate(prompt)
    print("Stimmung:", result)
    ```

3. **Neutrale Aussage:**

    Text:

    ```text
    "Das Wetter ist heute durchschnittlich."
    ```

    Ergebnis:

    ```text
    "Neutral"
    ```

    ```python
    # Datei: sentiment3_neutral.py
    from lib.helper_ollama import ollama

    text = "Das Wetter ist heute durchschnittlich."
    prompt = f"Analysiere die Stimmung (Positiv, Negativ, Neutral): {text}"
    result = ollama.generate(prompt)
    print("Stimmung:", result)
    ```

4. **Gemischte Stimmung:**

    Text:

    ```text
    "Der Service war langsam, aber das Essen war lecker."
    ```

    Ergebnis:

    ```text
    "Neutral" oder "Gemischt"
    ```

    ```python
    # Datei: sentiment4_gemischt.py
    from lib.helper_ollama import ollama

    text = "Der Service war langsam, aber das Essen war lecker."
    prompt = f"Analysiere die Stimmung (Positiv, Negativ, Neutral, Gemischt): {text}"
    result = ollama.generate(prompt)
    print("Stimmung:", result)
    ```

5. **Ironie/Sarkasmus:**

    Text:

    ```text
    "Toll, schon wieder ein Fehler im System..."
    ```

    Ergebnis:

    ```text
    Modell erkennt evtl. "Negativ"
    ```

    ```python
    # Datei: sentiment5_ironie.py
    from lib.helper_ollama import ollama

    text = "Toll, schon wieder ein Fehler im System..."
    prompt = f"Analysiere die Stimmung (Positiv, Negativ, Neutral, Sarkasmus): {text}"
    result = ollama.generate(prompt)
    print("Stimmung:", result)
    ```

### 10 Fragen & Lösungen zu Sentimentanalyse

1. **Was ist Sentimentanalyse?**
    - *Lösung:* Die automatische Erkennung der Stimmung in Texten.
2. **Welche Stimmungen werden meist unterschieden?**
    - *Lösung:* Positiv, Negativ, Neutral.
3. **Warum ist Sentimentanalyse für Unternehmen wichtig?**
    - *Lösung:* Sie hilft, Meinungen und Trends zu erkennen.
4. **Was ist eine Herausforderung bei Sentimentanalyse?**
    - *Lösung:* Ironie, Sarkasmus, gemischte Stimmungen.
5. **Wie kann man die Antwort auf "Positiv", "Negativ" oder "Neutral" beschränken?**
    - *Lösung:* Durch explizite Vorgabe im Prompt.
6. **Wie kann man mehrere Sätze automatisch analysieren?**
    - *Lösung:* Mit einer Schleife und einer Funktion wie `analyze_sentiment(text)`.
7. **Was ist ein Beispiel für einen neutralen Text?**
    - *Lösung:* "Das Wetter ist heute durchschnittlich."
8. **Wie kann man Sentimentanalyse in einer App nutzen?**
    - *Lösung:* Z. B. mit Streamlit und LLM-API.
9. **Was ist ein Nachteil von LLMs bei Sentimentanalyse?**
    - *Lösung:* Sie können Ironie/Sarkasmus oft nicht sicher erkennen.
10. **Wie kann man die Ergebnisse der Sentimentanalyse verbessern?**
    - *Lösung:* Durch gezielte Prompts, Beispiele und Nachbearbeitung.

---

## Einheit 3 — Themenklassifikation

### Umfangreiche Beschreibung & Grundlagen

Themenklassifikation (Topic Classification) ist die automatische Zuordnung von Texten zu vordefinierten Themen oder Kategorien. LLMs können dies ohne spezielles Training, da sie viele Beispiele aus unterschiedlichen Bereichen kennen. Typische Kategorien sind z. B. Sport, Politik, Wissenschaft, Unterhaltung, Wirtschaft.

**Warum ist Themenklassifikation wichtig?**

- Sie hilft, große Textmengen zu strukturieren und zu filtern.
- Sie ist Grundlage für News-Filter, Content-Moderation, Trend-Analysen und mehr.
- Sie ermöglicht gezielte Auswertungen und Automatisierung.

**Herausforderungen:**

- Texte können mehrere Themen enthalten.
- Kategorien müssen klar definiert sein.
- Unterschiedliche Formulierungen für gleiche Themen.

### 5 Beispiele für Themenklassifikation (mit Python-Code)

1. **Einfache Klassifikation:**

    Text:

    ```text
    "Apple hat ein neues iPhone vorgestellt."
    ```

    Ergebnis:

    ```text
    "Technologie"
    ```

    ```python
    # Datei: topic1_einfach.py
    from lib.helper_ollama import ollama

    text = "Apple hat ein neues iPhone vorgestellt."
    prompt = f"Ordne diesen Text einem Thema zu (Technologie, Politik, Sport, Unterhaltung): {text}"
    result = ollama.generate(prompt)
    print("Thema:", result)
    ```

2. **Politik:**

    Text:

    ```text
    "Die Regierung hat ein neues Gesetz verabschiedet."
    ```

    Ergebnis:

    ```text
    "Politik"
    ```

    ```python
    # Datei: topic2_politik.py
    from lib.helper_ollama import ollama

    text = "Die Regierung hat ein neues Gesetz verabschiedet."
    prompt = f"Ordne diesen Text einem Thema zu (Technologie, Politik, Sport, Unterhaltung): {text}"
    result = ollama.generate(prompt)
    print("Thema:", result)
    ```

3. **Sport:**

    Text:

    ```text
    "Lionel Messi schoss 2 Tore."
    ```

    Ergebnis:

    ```text
    "Sport"
    ```

    ```python
    # Datei: topic3_sport.py
    from lib.helper_ollama import ollama

    text = "Lionel Messi schoss 2 Tore."
    prompt = f"Ordne diesen Text einem Thema zu (Technologie, Politik, Sport, Unterhaltung): {text}"
    result = ollama.generate(prompt)
    print("Thema:", result)
    ```

4. **Mehrdeutiger Text:**

    Text:

    ```text
    "Tesla investiert in neue Batterietechnologie und sponsert ein Fußballteam."
    ```

    Ergebnis:

    ```text
    "Technologie, Sport" (Mehrthemen möglich)
    ```

    ```python
    # Datei: topic4_mehrdeutig.py
    from lib.helper_ollama import ollama

    text = "Tesla investiert in neue Batterietechnologie und sponsert ein Fußballteam."
    prompt = f"Ordne diesen Text den passenden Themen zu (Technologie, Politik, Sport, Unterhaltung): {text}"
    result = ollama.generate(prompt)
    print("Themen:", result)
    ```

5. **Klassifikation mit JSON-Ausgabe:**

    Text:

    ```text
    "Die Aktie von Tesla stieg um 5%."
    ```

    Ergebnis:

    ```text
    {"Text": "Die Aktie von Tesla stieg um 5%.", "Thema": "Wirtschaft"}
    ```

    ```python
    # Datei: topic5_json.py
    from lib.helper_ollama import ollama

    text = "Die Aktie von Tesla stieg um 5%."
    prompt = f"Klassifiziere den Text und antworte im JSON-Format:\n{{\n  'Text': '{text}',\n  'Thema': '<Kategorie>'\n}}"
    result = ollama.generate(prompt)
    print("Klassifikation:", result)
    ```

### 10 Fragen & Lösungen zu Themenklassifikation

1. **Was ist Themenklassifikation?**
    - *Lösung:* Die automatische Zuordnung von Texten zu vordefinierten Themen.
2. **Nenne drei typische Themen-Kategorien.**
    - *Lösung:* Sport, Politik, Technologie, Wirtschaft, Unterhaltung (je drei nennen)
3. **Warum ist Themenklassifikation nützlich?**
    - *Lösung:* Sie hilft, große Textmengen zu strukturieren und gezielt auszuwerten.
4. **Wie kann man mehrere Themen in einem Text erkennen?**
    - *Lösung:* Durch Prompts, die Mehrfachnennungen erlauben.
5. **Was ist eine Herausforderung bei der Themenklassifikation?**
    - *Lösung:* Mehrdeutige oder gemischte Texte.
6. **Wie kann man die Ausgabe strukturieren?**
    - *Lösung:* Durch Vorgabe von JSON- oder Listenformat im Prompt.
7. **Wie kann man Themenklassifikation in einer App nutzen?**
    - *Lösung:* Z. B. für News-Filter, Content-Moderation, Trend-Analysen.
8. **Was ist ein Nachteil von zu vielen Kategorien?**
    - *Lösung:* Die Zuordnung wird schwieriger und ungenauer.
9. **Wie kann man die Qualität der Klassifikation verbessern?**
    - *Lösung:* Durch klare Kategorien und Beispiele im Prompt.
10. **Wie kann man Themenklassifikation mit LLMs testen?**
    - *Lösung:* Durch verschiedene Prompts und Vergleich der Ergebnisse.

---

## Einheit 4 — Schlüsselwort-Extraktion

### Umfangreiche Beschreibung & Grundlagen

Schlüsselwort-Extraktion (Keyword Extraction) ist die Aufgabe, aus einem Text die wichtigsten Begriffe oder Phrasen herauszufiltern. Diese Keywords sind zentral für Suchmaschinen, Zusammenfassungen, Tagging und die schnelle Erfassung von Inhalten. LLMs können automatisch relevante Begriffe erkennen, da sie semantische Zusammenhänge verstehen.

**Warum ist Keyword-Extraktion wichtig?**

- Sie hilft, große Textmengen schnell zu durchsuchen und zu indexieren.
- Sie ist Grundlage für SEO, Textzusammenfassungen und Datenanalyse.
- Sie unterstützt die automatische Verschlagwortung und Kategorisierung.

**Herausforderungen:**

- Unterschiedliche Schreibweisen und Synonyme
- Relevanzbewertung: Was ist wirklich wichtig?
- Mehrwortbegriffe (z. B. "Künstliche Intelligenz")

### 5 Beispiele für Schlüsselwort-Extraktion (mit Python-Code)

1. **Einfache Extraktion:**

    Text:

    ```text
    "Tesla bringt ein neues Elektroauto mit innovativer Batterie auf den Markt."
    ````

    Ergebnis:

    ```text
    ["Tesla", "Elektroauto", "Batterie"]
    ```

    ```python
    # Datei: keywords1_einfach.py
    from lib.helper_ollama import ollama

    text = "Tesla bringt ein neues Elektroauto mit innovativer Batterie auf den Markt."
    prompt = f"Extrahiere die wichtigsten Keywords als Python-Liste: {text}"
    result = ollama.generate(prompt)
    print("Keywords:", result)
    ```

2. **Ausgabe als Liste:**

    Text:

    ```text
    "KI verändert die Medizin durch Bildanalyse und Sprachmodelle."
    ```

    Ergebnis:

    ```text
    ["KI", "Medizin", "Bildanalyse", "Sprachmodelle"]
    ```

    ```python
    # Datei: keywords2_liste.py
    from lib.helper_ollama import ollama

    text = "KI verändert die Medizin durch Bildanalyse und Sprachmodelle."
    prompt = f"Finde die Keywords und gib sie als Python-Liste zurück. Text: {text}"
    result = ollama.generate(prompt)
    print("Keywords:", result)
    ```

3. **JSON-Ausgabe:**

    Text:

    ```text
    "Die FIFA organisiert die Weltmeisterschaft in Katar."
    ```

    Ergebnis:

    ```text
    {"Keywords": ["FIFA", "Weltmeisterschaft", "Katar"], "Anzahl": 3}
    ```

    ```python
    # Datei: keywords3_json.py
    from lib.helper_ollama import ollama

    text = "Die FIFA organisiert die Weltmeisterschaft in Katar."
    prompt = f"Analysiere den Text und gib zurück: {{'Keywords': [...], 'Anzahl': <int>}} Text: {text}"
    result = ollama.generate(prompt)
    print("Keywords JSON:", result)
    ```

4. **Mehrwortbegriffe:**

    Text:

    ```text
    "Künstliche Intelligenz revolutioniert die Industrie."
    ```

    Ergebnis:

    ```text
    ["Künstliche Intelligenz", "Industrie"]
    ```

    ```python
    # Datei: keywords4_mehrwort.py
    from lib.helper_ollama import ollama

    text = "Künstliche Intelligenz revolutioniert die Industrie."
    prompt = f"Extrahiere alle wichtigen Mehrwortbegriffe und Keywords als Liste: {text}"
    result = ollama.generate(prompt)
    print("Mehrwort-Keywords:", result)
    ```

5. **Vergleich verschiedener Prompts:**

    Prompt 1:

    ```prompt
     "Extrahiere Keywords: ..."
     ```

    Prompt 2:

    ```prompt
    "Gib die wichtigsten Begriffe als Liste zurück: ..."
    ```

    Ergebnis:

    ```text
    Unterschiedliche Formate, aber ähnliche Inhalte.
    ```

    ```python
    # Datei: keywords5_vergleich.py
    from lib.helper_ollama import ollama

    text = "KI und Robotik verändern die Arbeitswelt."
    prompt1 = f"Extrahiere Keywords: {text}"
    prompt2 = f"Gib die wichtigsten Begriffe als Liste zurück: {text}"
    result1 = ollama.generate(prompt1)
    result2 = ollama.generate(prompt2)
    print("Prompt 1 Ergebnis:", result1)
    print("Prompt 2 Ergebnis:", result2)
    ```

### 10 Fragen & Lösungen zu Schlüsselwort-Extraktion

1. **Was ist Schlüsselwort-Extraktion?**
    - *Lösung:* Das Herausfiltern der wichtigsten Begriffe aus einem Text.
2. **Wofür werden Keywords verwendet?**
    - *Lösung:* Suchmaschinen, Zusammenfassungen, Tagging, Datenanalyse.
3. **Wie kann man Keywords mit LLMs extrahieren?**
    - *Lösung:* Durch gezielte Prompts wie "Extrahiere Keywords: ..."
4. **Was ist eine Herausforderung bei der Keyword-Extraktion?**
    - *Lösung:* Synonyme, Relevanzbewertung, Mehrwortbegriffe.
5. **Wie kann man die Ausgabe strukturieren?**
    - *Lösung:* Als Liste, JSON oder durch Kommas getrennt.
6. **Was ist ein Beispiel für ein Keyword mit mehreren Wörtern?**
    - *Lösung:* "Künstliche Intelligenz"
7. **Wie kann man die Anzahl der Keywords begrenzen?**
    - *Lösung:* Durch Vorgabe im Prompt (z. B. "Nenne die 3 wichtigsten Keywords...").
8. **Wie kann man Keywords aus PDFs extrahieren?**
    - *Lösung:* Text extrahieren und dann LLM mit Keyword-Prompt nutzen.
9. **Was ist ein Nachteil automatischer Keyword-Extraktion?**
    - *Lösung:* Nicht immer perfekte Relevanz, Kontext kann fehlen.
10. **Wie kann man die Qualität der Keywords verbessern?**
    - *Lösung:* Durch Nachbearbeitung, manuelle Kontrolle oder bessere Prompts.

---

## Einheit 5 — Named Entity Recognition (NER)

### Umfangreiche Beschreibung & Grundlagen

Named Entity Recognition (NER) ist die Aufgabe, Eigennamen wie Personen, Orte und Organisationen in Texten automatisch zu erkennen. LLMs sind dafür besonders geeignet, da sie viele Beispiele aus ihrem Training kennen und Kontext verstehen können.

**Warum ist NER wichtig?**

- Sie hilft, strukturierte Informationen aus unstrukturiertem Text zu gewinnen.
- Sie ist Grundlage für Suchmaschinen, Wissensdatenbanken, Chatbots und viele KI-Anwendungen.
- Sie ermöglicht die Verknüpfung von Textdaten mit externen Datenquellen.

**Herausforderungen:**

- Unterschiedliche Schreibweisen und Abkürzungen
- Mehrdeutigkeit (z. B. "Amazon" als Firma oder Fluss)
- Verschachtelte oder zusammengesetzte Entities

### 5 Beispiele für Named Entity Recognition (mit Python-Code)

1. **Einfache Entities:**

    Text:

    ```text
    "Barack Obama sprach 2015 in Berlin."
    ```

    Ergebnis:

    ```text
    Personen: ["Barack Obama"], Orte: ["Berlin"], Organisationen: []
    ```

    ```python
    # Datei: ner1_einfach.py
    from lib.helper_ollama import ollama

    text = "Barack Obama sprach 2015 in Berlin."
    prompt = f"Finde Named Entities (Personen, Orte, Organisationen) als JSON: {text}"
    result = ollama.generate(prompt)
    print("Entities:", result)
    ```

2. **Organisationen erkennen:**

    Text:

    ```text
    "Elon Musk gründete SpaceX in Kalifornien."
    ```

    Ergebnis:

    ```text
    Personen: ["Elon Musk"], Orte: ["Kalifornien"], Organisationen: ["SpaceX"]
    ```

    ```python
    # Datei: ner2_organisation.py
    from lib.helper_ollama import ollama

    text = "Elon Musk gründete SpaceX in Kalifornien."
    prompt = f"Finde Named Entities (Personen, Orte, Organisationen) als JSON: {text}"
    result = ollama.generate(prompt)
    print("Entities:", result)
    ```

3. **Mehrere Sätze:**

    Text:

    ```text
    "Angela Merkel traf Emmanuel Macron in Paris. Microsoft investierte in OpenAI."
    ```

    Ergebnis:

    ```text
    Personen: ["Angela Merkel", "Emmanuel Macron"], Orte: ["Paris"], Organisationen: ["Microsoft", "OpenAI"]
    ```

    ```python
    # Datei: ner3_mehrere_saetze.py
    from lib.helper_ollama import ollama

    text = "Angela Merkel traf Emmanuel Macron in Paris. Microsoft investierte in OpenAI."
    prompt = f"Finde Named Entities (Personen, Orte, Organisationen) als JSON: {text}"
    result = ollama.generate(prompt)
    print("Entities:", result)
    ```

4. **Mehrdeutige Entities:**

    Text:

    ```text
    "Amazon expandiert nach Brasilien."
    ```

    Ergebnis:

    ```text
    Organisationen: ["Amazon"], Orte: ["Brasilien"]
    ```

    ```python
    # Datei: ner4_mehrdeutig.py
    from lib.helper_ollama import ollama

    text = "Amazon expandiert nach Brasilien."
    prompt = f"Finde Named Entities (Personen, Orte, Organisationen) als JSON: {text}"
    result = ollama.generate(prompt)
    print("Entities:", result)
    ```

5. **JSON-Ausgabe:**

    Text:

    ```text
    "Jeff Bezos gründete Amazon in Seattle."
    
    ```

    Ergebnis:

    ```text
    {"Personen": ["Jeff Bezos"], "Orte": ["Seattle"], "Organisationen": ["Amazon"]}
    ```

    ```python
    # Datei: ner5_json.py
    from lib.helper_ollama import ollama

    text = "Jeff Bezos gründete Amazon in Seattle."
    prompt = f"Extrahiere Named Entities im JSON-Format: {{'Personen': [], 'Orte': [], 'Organisationen': []}} Text: {text}"
    result = ollama.generate(prompt)
    print("Entities JSON:", result)
    ```

### 10 Fragen & Lösungen zu Named Entity Recognition

1. **Was ist Named Entity Recognition?**
    - *Lösung:* Das automatische Erkennen von Eigennamen (Personen, Orte, Organisationen) in Texten.
2. **Nenne drei Typen von Entities.**
    - *Lösung:* Personen, Orte, Organisationen.
3. **Warum ist NER für KI-Anwendungen wichtig?**
    - *Lösung:* Sie liefert strukturierte Informationen für Suche, Datenbanken, Chatbots etc.
4. **Was ist eine Herausforderung bei NER?**
    - *Lösung:* Mehrdeutigkeit, unterschiedliche Schreibweisen, verschachtelte Entities.
5. **Wie kann man die Ausgabe strukturieren?**
    - *Lösung:* Als Listen oder im JSON-Format.
6. **Wie kann man NER mit LLMs testen?**
    - *Lösung:* Durch gezielte Prompts und Vergleich der Ergebnisse.
7. **Was ist ein Beispiel für eine Organisation als Entity?**
    - *Lösung:* "Microsoft", "Amazon", "SpaceX"
8. **Wie kann man Entities aus mehreren Sätzen extrahieren?**
    - *Lösung:* Text als Ganzes analysieren lassen, ggf. Listen ausgeben.
9. **Was ist ein Nachteil automatischer NER?**
    - *Lösung:* Fehler bei unbekannten Namen, Abkürzungen oder Kontext.
10. **Wie kann man die Qualität der NER-Ergebnisse verbessern?**
    - *Lösung:* Durch bessere Prompts, Nachbearbeitung oder Kombination mit anderen Tools.

---

## Einheit 6 — FAQ-Bot mit Ollama

### Umfangreiche Beschreibung & Grundlagen

Ein FAQ-Bot (Frequently Asked Questions Bot) ist ein System, das häufig gestellte Fragen automatisch beantwortet. Die Antworten basieren auf einer vorgegebenen FAQ-Liste oder einem Dokument. LLMs können solche Bots besonders flexibel machen, da sie auch ähnliche oder umformulierte Fragen erkennen und beantworten können.

**Warum sind FAQ-Bots nützlich?**

- Sie entlasten Support-Teams und beantworten Standardfragen rund um die Uhr.
- Sie verbessern die Nutzererfahrung auf Webseiten und in Apps.
- Sie können mit neuen Fragen und Antworten einfach erweitert werden.

**Herausforderungen:**

- Fragen können unterschiedlich formuliert sein.
- Antworten müssen präzise und korrekt sein.
- Umgang mit Fragen, die nicht in der FAQ stehen.

### 5 Beispiele für FAQ-Bot-Anwendungen (mit Python-Code)

1. **Einfache FAQ als Text:**

    FAQ:

    ```text
    "Q: Was ist Python?\nA: Eine Programmiersprache."
    ```

    Frage:

    ```text
    "Was ist Python?"
    ```

    Ergebnis:

    ```text
    "Eine Programmiersprache."
    ```

    ```python
    # Datei: faq1_einfach.py
    from lib.helper_ollama import ollama

    faq = "Q: Was ist Python?\nA: Eine Programmiersprache."
    frage = "Was ist Python?"
    prompt = f"Beantworte die Frage basierend auf dieser FAQ:\n{faq}\n\nFrage: {frage}"
    result = ollama.generate(prompt)
    print("Antwort:", result)
    ```

2. **Frage umformuliert:**
    FAQ:

    ```text
    "Q: Was ist KI?\nA: Maschinen, die Aufgaben wie Menschen lösen."
    ```

    Frage:

    ```text
    "Was versteht man unter Künstlicher Intelligenz?"
    ````

    Ergebnis:

    ```text
    "Maschinen, die Aufgaben wie Menschen lösen."
    ```

    ```python
    # Datei: faq2_umformuliert.py
    from lib.helper_ollama import ollama

    faq = "Q: Was ist KI?\nA: Maschinen, die Aufgaben wie Menschen lösen."
    frage = "Was versteht man unter Künstlicher Intelligenz?"
    prompt = f"Beantworte die Frage basierend auf dieser FAQ:\n{faq}\n\nFrage: {frage}"
    result = ollama.generate(prompt)
    print("Antwort:", result)
    ```

3. **Datei-Upload:**
    - FAQ wird aus einer hochgeladenen Datei geladen und durchsucht.
    - **Python-Code (Streamlit):**

    ```python
    # Datei: faq3_upload.py
    import streamlit as st
    from lib.helper_ollama import ollama

    st.title("FAQ-Bot mit Datei-Upload")
    file = st.file_uploader("FAQ hochladen", type="txt")
    frage = st.text_input("Stelle eine Frage:")
    if file and frage:
        faq = file.read().decode()
        prompt = f"Beantworte die Frage basierend auf dieser FAQ:\n{faq}\n\nFrage: {frage}"
        if st.button("Antworten"):
            result = ollama.generate(prompt)
            st.write("Antwort:", result)
    ```

4. **Mehrere FAQ-Dateien kombinieren:**
    - Mehrere Dokumente werden zusammengeführt, um den Wissensstand zu erweitern.
    - **Python-Code (Streamlit):**

    ```python
    # Datei: faq4_mehrere_uploads.py
    import streamlit as st
    from lib.helper_ollama import ollama

    st.title("FAQ-Bot mit mehreren Dateien")
    files = st.file_uploader("Mehrere FAQs hochladen", type="txt", accept_multiple_files=True)
    frage = st.text_input("Stelle eine Frage:")
    if files and frage:
        faq_data = "\n".join([f.read().decode() for f in files])
        prompt = f"Beantworte die Frage basierend auf dieser FAQ:\n{faq_data}\n\nFrage: {frage}"
        if st.button("Antworten"):
            result = ollama.generate(prompt)
            st.write("Antwort:", result)
    ```

5. **Umgang mit unbekannten Fragen:**

    Frage:

    ```text
    "Wie funktioniert Quantencomputing?" (nicht in FAQ)
    ```

    Ergebnis:

    ```text
    "Diese Frage ist leider nicht in der FAQ enthalten."
    ```

    ```python
    # Datei: faq5_unbekannt.py
    from lib.helper_ollama import ollama

    faq = "Q: Was ist Python?\nA: Eine Programmiersprache."
    frage = "Wie funktioniert Quantencomputing?"
    prompt = f"Beantworte die Frage basierend auf dieser FAQ. Wenn die Antwort nicht enthalten ist, sage: 'Diese Frage ist leider nicht in der FAQ enthalten.'\n{faq}\n\nFrage: {frage}"
    result = ollama.generate(prompt)
    print("Antwort:", result)
    ```

### 10 Fragen & Lösungen zu FAQ-Bots

1. **Was ist ein FAQ-Bot?**
    - *Lösung:* Ein System, das häufig gestellte Fragen automatisch beantwortet.
2. **Wie kann ein FAQ-Bot erweitert werden?**
    - *Lösung:* Durch Hinzufügen neuer Fragen und Antworten zur FAQ-Liste.
3. **Was ist eine Herausforderung bei FAQ-Bots?**
    - *Lösung:* Unterschiedliche Formulierungen der Fragen.
4. **Wie kann man einen FAQ-Bot mit LLMs bauen?**
    - *Lösung:* FAQ als Kontext in den Prompt geben und die Frage anhängen.
5. **Wie kann man mehrere FAQ-Dateien nutzen?**
    - *Lösung:* Dateien zusammenführen und als Kontext verwenden.
6. **Wie sollte der Bot reagieren, wenn eine Frage nicht in der FAQ steht?**
    - *Lösung:* Freundlich darauf hinweisen, dass die Antwort nicht bekannt ist.
7. **Was ist ein Vorteil von LLM-basierten FAQ-Bots?**
    - *Lösung:* Sie erkennen auch umformulierte oder ähnliche Fragen.
8. **Wie kann man die Qualität der Antworten sichern?**
    - *Lösung:* FAQ regelmäßig prüfen und aktualisieren.
9. **Wie kann man einen FAQ-Bot in eine App integrieren?**
    - *Lösung:* Mit Streamlit, Web-Frameworks oder Chatbots.
10. **Was ist ein Nachteil von FAQ-Bots?**
    - *Lösung:* Sie können keine komplexen, individuellen Probleme lösen.

---

## Einheit 7 — Kombination von Analysen (Sentiment + Keywords + Entities)

### Umfangreiche Beschreibung & Grundlagen

LLMs sind in der Lage, mehrere Analyseaufgaben in einem Schritt zu erledigen. Das bedeutet, man kann mit einem einzigen Prompt gleichzeitig die Stimmung, Schlüsselwörter, Named Entities und sogar Zusammenfassungen aus einem Text extrahieren lassen. Das spart Zeit und ermöglicht komplexe Auswertungen mit wenig Code.

**Warum ist die Kombination von Analysen nützlich?**

- Sie liefert ein umfassendes Bild eines Textes auf einen Blick.
- Sie spart Rechenzeit und vereinfacht Workflows.
- Sie ist ideal für Dashboards, Monitoring und automatisierte Reports.

**Herausforderungen:**

- Die Formatierung der Ausgabe muss klar vorgegeben werden.
- Die Ergebnisse müssen ggf. nachbearbeitet oder geparst werden.
- Bei sehr langen Texten kann das Kontextfenster des Modells überschritten werden.

### 5 Beispiele für kombinierte Analysen (mit Python-Code)

1. **Stimmung + Keywords:**

    Text:

    ```text
    "Das neue iPhone ist beeindruckend, aber sehr teuer."
    ```

    Ergebnis:

    ```text
    Stimmung: "Gemischt", Keywords: ["iPhone", "teuer"]
    ```

    ```python
    # Datei: kombi1_stimmung_keywords.py
    from lib.helper_ollama import ollama

    text = "Das neue iPhone ist beeindruckend, aber sehr teuer."
    prompt = f"Analysiere diesen Text und gib zurück:\n1. Stimmung (Positiv/Negativ/Neutral/Gemischt)\n2. Keywords als Liste\nText: {text}"
    result = ollama.generate(prompt)
    print("Analyse:", result)
    ```

2. **Alles in einem:**

    Text:

    ```text
    "Angela Merkel hielt in Berlin eine Rede über die EU."
    ```

    Ergebnis:

    ```text
    Stimmung, Keywords, Named Entities, Zusammenfassung
    ```

    ```python
    # Datei: kombi2_alles.py
    from lib.helper_ollama import ollama

    text = "Angela Merkel hielt in Berlin eine Rede über die EU."
    prompt = f"Analysiere den Text und gib zurück:\n- Stimmung\n- Keywords\n- Named Entities\n- Kurze Zusammenfassung\nText: {text}"
    result = ollama.generate(prompt)
    print("Analyse:", result)
    ```

3. **JSON-Ausgabe:**

    Prompt:

    ```prompt
    "Analysiere den Text und gib das Ergebnis als JSON zurück: Stimmung, Keywords, Entities."
    ```

    ```python
    # Datei: kombi3_json.py
    from lib.helper_ollama import ollama

    text = "Tesla investiert in KI und baut neue Fabriken."
    prompt = f"Analysiere den Text und gib das Ergebnis als JSON zurück: Stimmung, Keywords, Entities. Text: {text}"
    result = ollama.generate(prompt)
    print("JSON-Analyse:", result)
    ```

4. **Mehrere Texte analysieren:**
    - Liste von Texten wird in einer Schleife analysiert
    - Ergebnisse werden gesammelt.

    ```python
    # Datei: kombi4_mehrere.py
    from lib.helper_ollama import ollama

    texte = [
        "Das neue iPhone ist beeindruckend, aber sehr teuer.",
        "Angela Merkel hielt in Berlin eine Rede über die EU.",
        "Tesla investiert in KI und baut neue Fabriken."
    ]
    for text in texte:
        prompt = f"Analysiere den Text und gib das Ergebnis als JSON zurück: Stimmung, Keywords, Entities. Text: {text}"
        result = ollama.generate(prompt)
        print(f"Text: {text}\nAnalyse: {result}\n")
    ```

5. **Dashboard-Anwendung:**
    - Ein Streamlit-Dashboard zeigt für jeden Text alle Analyse-Ergebnisse übersichtlich an.

    ```python
    # Datei: kombi5_dashboard.py
    import streamlit as st
    from lib.helper_ollama import ollama

    st.title("Kombinierte Textanalyse")
    text = st.text_area("Text eingeben")
    if st.button("Analysieren") and text:
        prompt = f"Analysiere den Text und gib das Ergebnis als JSON zurück: Stimmung, Keywords, Entities, Zusammenfassung. Text: {text}"
        result = ollama.generate(prompt)
        st.write("Analyse:", result)
    ```

### 10 Fragen & Lösungen zu kombinierten Analysen

1. **Was bedeutet kombinierte Analyse bei LLMs?**
    - *Lösung:* Mehrere Analyseaufgaben (z. B. Stimmung, Keywords, Entities) werden in einem Schritt erledigt.
2. **Was ist ein Vorteil kombinierter Analysen?**
    - *Lösung:* Spart Zeit, liefert umfassende Ergebnisse.
3. **Wie kann man die Ausgabe strukturieren?**
    - *Lösung:* Durch klare Vorgaben im Prompt, z. B. Listen oder JSON.
4. **Was ist ein Nachteil bei sehr langen Texten?**
    - *Lösung:* Das Kontextfenster des Modells kann überschritten werden.
5. **Wie kann man kombinierte Analysen in einer App nutzen?**
    - *Lösung:* In Dashboards, Monitoring-Tools, Reports.
6. **Wie kann man die Ergebnisse weiterverarbeiten?**
    - *Lösung:* Durch Parsen der Ausgabe (z. B. JSON in Python).
7. **Was ist ein Beispiel für eine kombinierte Analyse?**
    - *Lösung:* Stimmung, Keywords und Entities aus einem Text extrahieren.
8. **Wie kann man mehrere Texte automatisch analysieren?**
    - *Lösung:* Mit einer Schleife und einer Analysefunktion.
9. **Wie kann man die Qualität der kombinierten Analyse verbessern?**
    - *Lösung:* Durch präzise Prompts und Formatvorgaben.
10. **Was ist ein typischer Fehler bei kombinierten Analysen?**
    - *Lösung:* Unklare Formatvorgaben, zu lange Texte, fehlende Nachbearbeitung.

---

## Einheit 8 — Erweiterte Streamlit-App: Analyse-Dashboard

### Umfangreiche Beschreibung & Grundlagen

Ein Analyse-Dashboard ist eine interaktive App, die verschiedene Textanalyse-Funktionen in einer übersichtlichen Oberfläche vereint. Mit Streamlit kann man schnell und einfach ein Dashboard bauen, das Sentimentanalyse, Keyword-Extraktion, Named Entity Recognition und Zusammenfassung kombiniert. Nutzer können Texte eingeben, hochladen oder aus einer Liste auswählen und erhalten sofort eine umfassende Analyse.

**Warum sind Dashboards nützlich?**

- Sie machen komplexe Analysen für alle zugänglich.
- Sie ermöglichen schnelle Auswertungen ohne Programmierkenntnisse.
- Sie sind ideal für Präsentationen, Monitoring und Prototyping.

**Herausforderungen:**

- Übersichtliche Darstellung der Ergebnisse
- Performance bei großen Textmengen
- Flexibilität für verschiedene Analysearten

### 5 Beispiele für Analyse-Dashboards (mit Python-Code)

1. **Einfaches Textfeld:**

    Nutzer gibt einen Text ein, Dashboard zeigt alle Analysen an.

    ```python
    # Datei: dashboard1_textfeld.py
    import streamlit as st
    from lib.helper_ollama import ollama

    st.title("Textanalyse Dashboard")
    text = st.text_area("Text eingeben")
    if st.button("Analysieren") and text:
        prompt = f"Analysiere den Text und gib das Ergebnis als JSON zurück: Stimmung, Keywords, Entities, Zusammenfassung. Text: {text}"
        result = ollama.generate(prompt)
        st.write("Analyse:", result)
    ```

2. **Datei-Upload:**

    Nutzer lädt ein PDF oder eine Textdatei hoch, Dashboard analysiert den gesamten Inhalt.

    ```python
    # Datei: dashboard2_upload.py
    import streamlit as st
    from lib.helper_ollama import ollama

    st.title("Datei-Upload Analyse")
    file = st.file_uploader("Textdatei hochladen", type=["txt"])
    if file:
        text = file.read().decode()
        if st.button("Analysieren"):
            prompt = f"Analysiere den Text und gib das Ergebnis als JSON zurück: Stimmung, Keywords, Entities, Zusammenfassung. Text: {text}"
            result = ollama.generate(prompt)
            st.write("Analyse:", result)
    ```

3. **Mehrere Texte vergleichen:**

    Dashboard zeigt Analyse-Ergebnisse für mehrere Texte nebeneinander.

    ```python
    # Datei: dashboard3_vergleich.py
    import streamlit as st
    from lib.helper_ollama import ollama

    st.title("Vergleich mehrerer Texte")
    texte = st.text_area("Texte (jeweils durch Zeilenumbruch trennen)")
    if st.button("Analysieren") and texte:
        text_list = [t for t in texte.split("\n") if t.strip()]
        cols = st.columns(len(text_list))
        for i, text in enumerate(text_list):
            prompt = f"Analysiere den Text und gib das Ergebnis als JSON zurück: Stimmung, Keywords, Entities, Zusammenfassung. Text: {text}"
            result = ollama.generate(prompt)
            with cols[i]:
                st.write(f"**Text {i+1}:**", text)
                st.write(result)
    ```

4. **Ergebnisse als Tabelle:**
    - Alle Analysen werden in einer Tabelle oder als JSON angezeigt.
    - **Python-Code (Streamlit + pandas):**

    ```python
    # Datei: dashboard4_tabelle.py
    import streamlit as st
    import pandas as pd
    from lib.helper_ollama import ollama

    st.title("Analyse als Tabelle")
    texte = st.text_area("Texte (je Zeile ein Text)")
    if st.button("Analysieren") and texte:
        text_list = [t for t in texte.split("\n") if t.strip()]
        daten = []
        for text in text_list:
            prompt = f"Analysiere den Text und gib das Ergebnis als JSON zurück: Stimmung, Keywords, Entities, Zusammenfassung. Text: {text}"
            result = ollama.generate(prompt)
            daten.append({"Text": text, "Analyse": result})
        df = pd.DataFrame(daten)
        st.dataframe(df)
    ```

5. **Export-Funktion:**

    Ergebnisse können als CSV oder PDF exportiert werden.

    ```python
    # Datei: dashboard5_export.py
    import streamlit as st
    import pandas as pd
    from lib.helper_ollama import ollama

    st.title("Analyse mit Export")
    texte = st.text_area("Texte (je Zeile ein Text)")
    if st.button("Analysieren") and texte:
        text_list = [t for t in texte.split("\n") if t.strip()]
        daten = []
        for text in text_list:
            prompt = f"Analysiere den Text und gib das Ergebnis als JSON zurück: Stimmung, Keywords, Entities, Zusammenfassung. Text: {text}"
            result = ollama.generate(prompt)
            daten.append({"Text": text, "Analyse": result})
        df = pd.DataFrame(daten)
        st.dataframe(df)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("CSV herunterladen", csv, "analysen.csv", "text/csv")
    ```

### 10 Fragen & Lösungen zu Analyse-Dashboards

1. **Was ist ein Analyse-Dashboard?**
    - *Lösung:* Eine App, die verschiedene Analysefunktionen in einer Oberfläche vereint.
2. **Wie kann man ein Dashboard mit Streamlit bauen?**
    - *Lösung:* Mit Python und der Streamlit-Bibliothek.
3. **Welche Analysefunktionen kann ein Dashboard enthalten?**
    - *Lösung:* Sentiment, Keywords, NER, Zusammenfassung, u. v. m.
4. **Was ist ein Vorteil von Dashboards?**
    - *Lösung:* Sie machen Analysen für alle zugänglich und einfach bedienbar.
5. **Wie kann man mehrere Texte vergleichen?**
    - *Lösung:* Durch Anzeige der Ergebnisse nebeneinander oder in einer Tabelle.
6. **Wie kann man Ergebnisse exportieren?**
    - *Lösung:* Als CSV, PDF oder durch Kopieren der Daten.
7. **Was ist eine Herausforderung bei großen Textmengen?**
    - *Lösung:* Performance und Übersichtlichkeit.
8. **Wie kann man die Nutzerfreundlichkeit erhöhen?**
    - *Lösung:* Klare Struktur, einfache Bedienung, gute Visualisierung.
9. **Wie kann man das Dashboard erweitern?**
    - *Lösung:* Weitere Analysefunktionen, Filter, Visualisierungen hinzufügen.
10. **Was ist ein typischer Fehler bei Dashboards?**
    - *Lösung:* Unübersichtliche Darstellung, fehlende Export- oder Vergleichsfunktionen.

---

## Einheit 9 - Zusammenfassung

Nach Tag 3 können die Studierenden:

- Texte mit Ollama analysieren (Stimmung, Themen, Keywords, Entities)
- einen FAQ-Bot mit Dokumenten erstellen
- mehrere Analysen kombinieren
- ein eigenes Analyse-Dashboard in Streamlit bauen
- die Grenzen solcher Modelle erkennen (Halluzinationen, Mehrdeutigkeit)

---

## Einheit 10 - Mini-Projekte

### Mini-Projekt 1: Intelligenter PDF-Analyzer

**Aufgabe:** Baue eine App, die PDF-Dokumente hochlädt und mit KI analysiert.

**Lösung:**

```python
import streamlit as st
import PyPDF2
import io
from lib.helper_ollama import ollama

st.title("PDF-Analyzer mit KI")
pdf_file = st.file_uploader("PDF hochladen", type="pdf")

if pdf_file:
    # PDF Text extrahieren
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.read()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    st.write(f"Extrahierter Text ({len(text)} Zeichen)")
    
    analyse_typ = st.selectbox("Analyse-Typ:", 
                              ["Zusammenfassung", "Hauptthemen", "Sentiment", "Schlüsselwörter"])
    
    if st.button("Analysieren"):
        if analyse_typ == "Zusammenfassung":
            prompt = f"Fasse den folgenden Text in 5 Sätzen zusammen:\n{text[:2000]}"
        elif analyse_typ == "Hauptthemen":
            prompt = f"Identifiziere die 5 Hauptthemen in diesem Text:\n{text[:2000]}"
        elif analyse_typ == "Sentiment":
            prompt = f"Analysiere die Stimmung dieses Textes (positiv/neutral/negativ):\n{text[:2000]}"
        else:
            prompt = f"Extrahiere die 10 wichtigsten Schlüsselwörter:\n{text[:2000]}"
        
        result = ollama.generate(prompt)
        st.write("**Ergebnis:**", result)
```

### Mini-Projekt 2: Multi-Language Content Analyzer

**Aufgabe:** Analysiere Texte in verschiedenen Sprachen und übersetze sie.

**Lösung:**

```python
import streamlit as st
from lib.helper_ollama import ollama

st.title("Multi-Language Content Analyzer")
text = st.text_area("Text eingeben (beliebige Sprache)")

if text:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Spracherkennung & Analyse")
        if st.button("Analysieren"):
            prompt = f"""Analysiere den folgenden Text:
1. Erkenne die Sprache
2. Bestimme die Stimmung
3. Extrahiere Hauptthemen
4. Gib eine kurze Zusammenfassung

Text: {text}"""
            result = ollama.generate(prompt)
            st.write(result)
    
    with col2:
        st.subheader("Übersetzung")
        ziel_sprache = st.selectbox("Übersetzen zu:", 
                                   ["Deutsch", "Englisch", "Französisch", "Spanisch"])
        if st.button("Übersetzen"):
            prompt = f"Übersetze den folgenden Text zu {ziel_sprache}:\n{text}"
            result = ollama.generate(prompt)
            st.write(result)
```

### Mini-Projekt 3: Social Media Content Optimizer

**Aufgabe:** Optimiere Texte für verschiedene Social Media Plattformen.

**Lösung:**

```python
import streamlit as st
from lib.helper_ollama import ollama

st.title("Social Media Content Optimizer")
original_text = st.text_area("Ursprünglicher Text")
plattform = st.selectbox("Ziel-Plattform:", 
                        ["Twitter", "LinkedIn", "Instagram", "Facebook"])

if st.button("Optimieren") and original_text:
    if plattform == "Twitter":
        prompt = f"Kürze den Text auf max. 280 Zeichen für Twitter, behalte die Kernbotschaft:\n{original_text}"
    elif plattform == "LinkedIn":
        prompt = f"Schreibe den Text professioneller und strukturierter für LinkedIn um:\n{original_text}"
    elif plattform == "Instagram":
        prompt = f"Mache den Text emotionaler und visueller für Instagram:\n{original_text}"
    else:
        prompt = f"Mache den Text einladender und community-orientiert für Facebook:\n{original_text}"
    
    result = ollama.generate(prompt)
    st.write("**Optimierter Text:**")
    st.write(result)
    
    # Zusätzlich: Hashtag-Vorschläge
    if st.button("Hashtags vorschlagen"):
        hashtag_prompt = f"Schlage 5 relevante Hashtags für diesen {plattform}-Post vor:\n{result}"
        hashtags = ollama.generate(hashtag_prompt)
        st.write("**Hashtag-Vorschläge:**", hashtags)
```

### Mini-Projekt 4: Competitive Content Analysis

**Aufgabe:** Vergleiche Inhalte von Konkurrenten und analysiere deren Strategien.

**Lösung:**

```python
import streamlit as st
import pandas as pd
from lib.helper_ollama import ollama

st.title("Competitive Content Analysis")
st.write("Analysiere Inhalte von bis zu 3 Konkurrenten")

konkurrenten = []
for i in range(3):
    name = st.text_input(f"Konkurrent {i+1} Name:")
    content = st.text_area(f"Content von {name if name else f'Konkurrent {i+1}'}:")
    if name and content:
        konkurrenten.append({"Name": name, "Content": content})

if st.button("Analysieren") and konkurrenten:
    ergebnisse = []
    
    for k in konkurrenten:
        prompt = f"""Analysiere den folgenden Marketing-Content:
1. Hauptbotschaft
2. Zielgruppe
3. Tonalität/Stil
4. Stärken
5. Verbesserungsvorschläge

Content: {k['Content']}"""
        
        analyse = ollama.generate(prompt)
        ergebnisse.append({
            "Konkurrent": k["Name"],
            "Analyse": analyse
        })
    
    # Vergleichstabelle
    df = pd.DataFrame(ergebnisse)
    st.dataframe(df)
    
    # Strategische Empfehlungen
    if st.button("Strategische Empfehlungen"):
        alle_analysen = "\n\n".join([f"{e['Konkurrent']}: {e['Analyse']}" for e in ergebnisse])
        strategie_prompt = f"Basierend auf diesen Konkurrenzanalysen, gib strategische Empfehlungen für die eigene Content-Strategie:\n{alle_analysen}"
        empfehlungen = ollama.generate(strategie_prompt)
        st.write("**Strategische Empfehlungen:**", empfehlungen)
```

### Mini-Projekt 5: Real-time Content Monitoring Dashboard

**Aufgabe:** Überwache und analysiere Inhalte in Echtzeit.

**Lösung:**

```python
import streamlit as st
import pandas as pd
import time
from datetime import datetime
from lib.helper_ollama import ollama

st.title("Real-time Content Monitoring")

# Initialisiere Session State
if 'monitoring_data' not in st.session_state:
    st.session_state.monitoring_data = []

# Input für neuen Content
new_content = st.text_area("Neuen Content hinzufügen:")
source = st.text_input("Quelle (z.B. Website, Social Media):")

if st.button("Content analysieren") and new_content:
    # Analysiere Content
    prompt = f"""Analysiere diesen Content schnell:
- Sentiment (1-10)
- Kategorie (News/Marketing/Info/etc.)
- Dringlichkeit (niedrig/mittel/hoch)
- Keywords (top 3)

Content: {new_content}"""
    
    analyse = ollama.generate(prompt)
    
    # Speichere in Session State
    st.session_state.monitoring_data.append({
        "Timestamp": datetime.now().strftime("%H:%M:%S"),
        "Source": source,
        "Content": new_content[:100] + "..." if len(new_content) > 100 else new_content,
        "Analyse": analyse
    })

# Dashboard anzeigen
if st.session_state.monitoring_data:
    st.subheader("Live Dashboard")
    df = pd.DataFrame(st.session_state.monitoring_data)
    st.dataframe(df)
    
    # Statistiken
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Gesamt Inhalte", len(st.session_state.monitoring_data))
    with col2:
        st.metric("Letzte Aktualisierung", df.iloc[-1]["Timestamp"])
    with col3:
        if st.button("Dashboard leeren"):
            st.session_state.monitoring_data = []
            st.experimental_rerun()
```

---

> **Ausblick:**  
> Soll für Tag 4 (Fortgeschrittene Anwendungen: Datenintegration mit Pandas, Q&A über CSV-Dateien, KI-Dashboards, Deployment) auch ein vollständiges Lehrbuch-Kapitel mit vielen Beispielen erstellt werden?
