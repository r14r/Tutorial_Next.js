# Day 3 — Data Processing & AI Applications

## Unit 0 - Schedule 09:00 - 15:00

### Overview

The day teaches the practical basics of AI text analysis with Ollama and Python. Each unit consists of a short explanation, examples and practical exercises.

---

### Schedule

| time | Unit / Content | Duration |
|-----------------|---------------------------------------------------------------------------------|---------|
| **09:00 – 09:20** | Introduction & Overview - Motivation, Goals, AI Applications | 20 mins |
| **09:20 – 09:50** | **Unit 3.1:** Introduction to text analysis - basic concepts, tasks | 30 mins |
| **09:50 – 10:30** | **Unit 3.2:** Sentiment analysis - recognizing sentiment, examples, exercises | 40 mins |
| **10:30 – 11:10** | **Unit 3.3:** Topic classification - categories, labeling, exercises | 40 mins |
| **11:10 – 11:25** | ☕ **Break** | 15 mins |
| **11:25 – 12:00** | **Unit 3.4:** Keyword Extraction - Keywords, Lists, Exercises | 35 mins |
| **12:00 – 12:35** | **Unit 3.5:** Named Entity Recognition (NER) - People, Places, Organizations | 35 mins |
| **12:35 – 1:35 pm** | 🍽️ **Lunch break** | 60 mins |
| **1:35 p.m. – 2:05 p.m.** | **Unit 3.6:** FAQ bot with Ollama - FAQ upload, bot logic, exercises | 30 mins |
| **14:05 – 14:35** | **Unit 3.7:** Combination of Analytics - Sentiment + Keywords + Entities | 30 mins |
| **14:35 – 15:00** | **Unit 3.8:** Analyzing Dashboard with Streamlit - Building an App, Summary | 25 mins |

---

## Unit 1 — Introduction to Text Analysis

### Comprehensive description & basics

Text analysis (Natural Language Processing, NLP) is a central application area of ​​artificial intelligence. It includes methods for obtaining structured information from unstructured text. Typical tasks are:

- **Classification:** Classification of texts into topics, categories or labels (e.g. sports, politics, technology)
- **Sentiment analysis:** Rating of sentiment (positive, negative, neutral)
- **Keyword extraction:** Filtering out the most important terms
- **Named Entity Recognition (NER):** Recognition of proper names such as people, places, organizations
- **Summary:** Reduce complex texts to the essentials

LLMs (Large Language Models) are particularly well suited for text analysis because they have been trained on huge amounts of text and recognize semantic connections. They are used in business intelligence, social media monitoring, chatbots, customer feedback, search engines and many other areas.

**Why is text analysis important?**

- It helps to automatically evaluate large amounts of text.
- It enables data-driven decisions based on text data.
- It is the basis for many modern AI applications.

### 5 examples of text analysis tasks (with Python code)

1. **Categorization:**

Text:

```text
    "Lionel Messi scored a goal."
    - Task: Recognize topic → “Sport”
    ```

```python
    # File: example1_categorization.py
    from lib.helper_ollama import ollama

text = "Lionel Messi scored a goal."
    prompt = f"Assign this text to a topic (sports, politics, technology, entertainment): {text}"
    result = ollama.generate(prompt)
    print("Topic:", result)
    ```

2. **Sentiment Analysis:**

Text:

```text
    "The product is great!"
    - Task: Recognize mood → “Positive”
    ```

```python
    # File: example2_sentiment.py
    from lib.helper_ollama import ollama

text = "The product is great!"
    prompt = f"Analyze the sentiment (Positive, Negative, Neutral): {text}"
    result = ollama.generate(prompt)
    print("Mood:", result)
    ```

3. **Extract Keywords:**

Text:

```text
    "Tesla is launching a new electric car."
    - Task: Keywords → [“Tesla”, “electric car”]
    ```

```python
    # File: example3_keywords.py
    from lib.helper_ollama import ollama

text = "Tesla is launching a new electric car."
    prompt = f"Extract the most important keywords as a Python list: {text}"
    result = ollama.generate(prompt)
    print("Keywords:", result)
    ```

4. **Find Named Entities:**

Text:

```text
    "Angela Merkel met Barack Obama in Berlin."
    - Task: Recognize people and places → ["Angela Merkel", "Barack Obama", "Berlin"]
    ```

```python
    # File: example4_entities.py
    from lib.helper_ollama import ollama

text = "Angela Merkel met Barack Obama in Berlin."
    prompt = f"Find Named Entities (People, Places, Organizations) as JSON: {text}"
    result = ollama.generate(prompt)
    print("Entities:", result)
    ```

5. **Summary:**

Text:

```text
    "Tesla shares rose 10% after unveiling a new model."
    - Task: Short summary → "Tesla shares rise according to new model."
    ```

```python
    # File: example5_summary.py
    from lib.helper_ollama import ollama

text = "Tesla shares rose by 10% after the presentation of a new model."
    prompt = f"Summarize the following text in one sentence: {text}"
    result = ollama.generate(prompt)
    print("Summary:", result)
    ```

### 10 questions and solutions about text analysis

1. **What is text analysis?**
    - *Solution:* The automatic evaluation and structuring of texts by AI.
2. **Name two typical text analysis tasks.**
    - *Solution:* Classification, sentiment analysis, keyword extraction, NER, summary (name two each)
3. **Why are LLMs suitable for text analysis?**
    - *Solution:* You recognize semantic connections and are trained on large amounts of text.
4. **What is sentiment analysis?**
    - *Solution:* Detecting the mood of a text (positive, negative, neutral).
5. **What does Named Entity Recognition mean?**
    - *Solution:* Recognizing proper names such as people, places, organizations.
6. **How ​​can text analysis help in business?**
    - *Solution:* Automatic evaluation of customer feedback, social media, support tickets etc.
7. **What is an example of a classification task?**
    - *Solution:* A text is classified as "Sport" or "Politics".
8. **How ​​to extract keywords from text?**
    - *Solution:* Using LLMs or special algorithms, e.g. B. through prompts like “Extract keywords: …”
9. **What is a summary?**
    - *Solution:* Reducing a text to the most important statements.
10. **Give an example of the use of text analysis in everyday life.**
    - *Solution:* Spam filters, chatbots, automatic translations, product recommendations.

---

## Unit 2 — Sentiment Analysis (Detecting Mood)

### Comprehensive description & basics

Sentiment analysis is the automatic recognition of the mood in texts. It is commonly used in marketing, social media, product reviews and customer feedback. The goal is to find out whether a text is positive, negative or neutral. LLMs are particularly good at this because they know lots of examples from the internet and can recognize language nuances.

**Why is sentiment analysis important?**

- Companies can identify trends and opinions.
- It helps to automatically evaluate customer feedback.
- It is the basis for automated moderation and monitoring.

**Challenges:**

- Irony and sarcasm are difficult to recognize.
- Mixed moods in a text (e.g. "service bad, food good")
- Different wording for the same feelings

### 5 Examples of Sentiment Analysis (with Python Code)

1. **Simple Analysis:**

Text:

```text
    "The product is great!"
    ```

Result:

```text
    "Positive"
    ```

```python
    # File: sentiment1_easy.py
    from lib.helper_ollama import ollama

text = "The product is great!"
    prompt = f"Analyze the sentiment (Positive, Negative, Neutral): {text}"
    result = ollama.generate(prompt)
    print("Mood:", result)
    ```

2. **Negative Feedback:**

Text:

```text
    "I am very disappointed with the quality."
    ```

Result:

```text
    "Negative"
    ```

```python
    # File: sentiment2_negative.py
    from lib.helper_ollama import ollama

text = "I am very disappointed with the quality."
    prompt = f"Analyze the sentiment (Positive, Negative, Neutral): {text}"
    result = ollama.generate(prompt)
    print("Mood:", result)
    ```

3. **Neutral statement:**

Text:

```text
    "The weather is average today."
    ```

Result:

```text
    "Neutral"
    ```

```python
    # File: sentiment3_neutral.py
    from lib.helper_ollama import ollama

text = "The weather today is average."
    prompt = f"Analyze the sentiment (Positive, Negative, Neutral): {text}"
    result = ollama.generate(prompt)
    print("Mood:", result)
    ```

4. **Mixed Mood:**

Text:

```text
    "Service was slow but food was tasty."
    ```

Result:

```text
    "Neutral" or "Mixed"
    ```

```python
    # File: sentiment4_mixed.py
    from lib.helper_ollama import ollama

text = "The service was slow, but the food was delicious."
    prompt = f"Analyze the sentiment (Positive, Negative, Neutral, Mixed): {text}"
    result = ollama.generate(prompt)
    print("Mood:", result)
    ```

5. **Irony/Sarcasm:**

Text:

```text
    "Great, another error in the system..."
    ```

Result:

```text
    Model may detect “negative”
    ```

```python
    # File: sentiment5_ironie.py
    from lib.helper_ollama import ollama

text = "Great, another error in the system..."
    prompt = f"Analyze the mood (Positive, Negative, Neutral, Sarcasm): {text}"
    result = ollama.generate(prompt)
    print("Mood:", result)
    ```

### 10 questions and solutions about sentiment analysis

1. **What is sentiment analysis?**
    - *Solution:* Automatic detection of mood in texts.
2. **Which moods are usually distinguished?**
    - *Solution:* Positive, Negative, Neutral.
3. **Why is sentiment analysis important for companies?**
    - *Solution:* It helps to identify opinions and trends.
4. **What is a challenge in sentiment analysis?**
    - *Solution:* Irony, sarcasm, mixed moods.
5. **How ​​to limit the answer to Positive, Negative or Neutral?**
    - *Solution:* By explicitly specifying it in the prompt.
6. **How ​​to automatically parse multiple sentences?**
    - *Solution:* With a loop and a function like `analyze_sentiment(text)`.
7. **What is an example of neutral text?**
    - *Solution:* "The weather is average today."
8. **How ​​to use sentiment analysis in an app?**
    - *Solution:* E.g. with Streamlit and LLM API.
9. **What is a disadvantage of LLMs in sentiment analysis?**
    - *Solution:* You often cannot recognize irony/sarcasm with certainty.
10. **How ​​to improve sentiment analysis results?**
    - *Solution:* Through targeted prompts, examples and post-processing.

---

## Unit 3 — Topic Classification

### Comprehensive description & basics

Topic classification is the automatic assignment of texts to predefined topics or categories. LLMs can do this without any special training because they know many examples from different areas. Typical categories include: B. Sports, politics, science, entertainment, business.

**Why is topic classification important?**

- It helps to structure and filter large amounts of text.
- It is the basis for news filters, content moderation, trend analyzes and more.
- It enables targeted evaluations and automation.

**Challenges:**

- Texts can contain multiple topics.
- Categories must be clearly defined.
- Different wording for the same topics.

### 5 Topic Classification Examples (with Python Code)

1. **Simple classification:**

Text:

```text
    "Apple has introduced a new iPhone."
    ```

Result:

```text
    "Technology"
    ```

```python
    # File: topic1_easy.py
    from lib.helper_ollama import ollama

text = "Apple has introduced a new iPhone."
    prompt = f"Assign this text to a topic (technology, politics, sports, entertainment): {text}"
    result = ollama.generate(prompt)
    print("Topic:", result)
    ```

2. **Policy:**

Text:

```text
    "The government has passed a new law."
    ```

Result:

```text
    "Policy"
    ```

```python
    # File: topic2_politik.py
    from lib.helper_ollama import ollama

text = "The government has passed a new law."
    prompt = f"Assign this text to a topic (technology, politics, sports, entertainment): {text}"
    result = ollama.generate(prompt)
    print("Topic:", result)
    ```

3. **Sports:**

Text:

```text
    "Lionel Messi scored 2 goals."
    ```

Result:

```text
    "Sport"
    ```

```python
    # File: topic3_sport.py
    from lib.helper_ollama import ollama

text = "Lionel Messi scored 2 goals."
    prompt = f"Assign this text to a topic (technology, politics, sports, entertainment): {text}"
    result = ollama.generate(prompt)
    print("Topic:", result)
    ```

4. **Ambiguous text:**

Text:

```text
    "Tesla invests in new battery technology and sponsors a football team."
    ```

Result:

```text
    "Technology, Sport" (multiple topics possible)
    ```

```python
    # File: topic4_ambiguous.py
    from lib.helper_ollama import ollama

text = "Tesla invests in new battery technology and sponsors a football team."
    prompt = f"Assign this text to the appropriate topics (technology, politics, sports, entertainment): {text}"
    result = ollama.generate(prompt)
    print("Topics:", result)
    ```

5. **Classification with JSON output:**

Text:

```text
    "Tesla shares rose 5%."
    ```

Result:

```text
    {"Text": "Tesla shares rose 5%.", "Topic": "Economy"}
    ```

```python
    # File: topic5_json.py
    from lib.helper_ollama import ollama

text = "Tesla shares rose 5%."
    prompt = f"Classify the text and reply in JSON format:\n{{\n 'Text': '{text}',\n 'Topic': '<Category>'\n}}"
    result = ollama.generate(prompt)
    print("Classification:", result)
    ```

### 10 questions and solutions on the topic of classification

1. **What is Topic Classification?**
    - *Solution:* The automatic assignment of texts to predefined topics.
2. **Name three typical topic categories.**
    - *Solution:* Sports, politics, technology, business, entertainment (name three each)
3. **Why is topic classification useful?**
    - *Solution:* It helps to structure and specifically evaluate large amounts of text.
4. **How ​​can you identify multiple topics in a text?**
    - *Solution:* Through prompts that allow multiple answers.
5. **What is a challenge in topic classification?**
    - *Solution:* Ambiguous or mixed texts.
6. **How ​​to structure the output?**
    - *Solution:* By specifying JSON or list format in the prompt.
7. **How ​​to use topic classification in an app?**
    - *Solution:* E.g. for news filters, content moderation, trend analysis.
8. **What is a disadvantage of having too many categories?**
    - *Solution:* The assignment becomes more difficult and less precise.
9. **How ​​to improve the quality of the classification?**
    - *Solution:* Through clear categories and examples in the prompt.
10. **How ​​to test topic classification with LLMs?**
    - *Solution:* By using different prompts and comparing the results.

---

## Unit 4 — Keyword Extraction

### Comprehensive description & basics

Keyword extraction is the task of filtering out the most important terms or phrases from a text. These keywords are central to search engines, summaries, tagging and quick content capture. LLMs can automatically recognize relevant terms because they understand semantic relationships.

**Why is keyword extraction important?**

- It helps to quickly search and index large amounts of text.
- It is the basis for SEO, text summaries and data analysis.
- It supports automatic keywording and categorization.

**Challenges:**

- Different spellings and synonyms
- Relevance assessment: What is really important?
- Multi-word terms (e.g. “artificial intelligence”)

### 5 Examples of Keyword Extraction (with Python Code)

1. **Easy Extraction:**

Text:

```text
    "Tesla is launching a new electric car with an innovative battery."
    ````

Result:

```text
    ["Tesla", "electric car", "battery"]
    ```

```python
    # File: keywords1_easy.py
    from lib.helper_ollama import ollama

text = "Tesla is launching a new electric car with an innovative battery."
    prompt = f"Extract the most important keywords as a Python list: {text}"
    result = ollama.generate(prompt)
    print("Keywords:", result)
    ```

2. **Output as a list:**

Text:

```text
    "AI is changing medicine through image analysis and language models."
    ```

Result:

```text
    ["AI", "Medicine", "Image Analysis", "Language Models"]
    ```

```python
    # File: keywords2_list.py
    from lib.helper_ollama import ollama

text = "AI is changing medicine through image analysis and language models."
    prompt = f"Find the keywords and return them as a Python list. Text: {text}"
    result = ollama.generate(prompt)
    print("Keywords:", result)
    ```

3. **JSON output:**

Text:

```text
    "FIFA is organizing the World Cup in Qatar."
    ```

Result:

```text
    {"Keywords": ["FIFA", "World Cup", "Qatar"], "Number": 3}
    ```

```python
    # File: keywords3_json.py
    from lib.helper_ollama import ollama

text = "FIFA is organizing the World Cup in Qatar."
    prompt = f"Parse the text and return: {{'Keywords': [...], 'Number': <int>}} Text: {text}"
    result = ollama.generate(prompt)
    print("Keywords JSON:", result)
    ```

4. **Multi-word terms:**

Text:

```text
    "Artificial intelligence is revolutionizing industry."
    ```

Result:

```text
    ["Artificial Intelligence", "Industry"]
    ```

```python
    # File: keywords4_multiword.py
    from lib.helper_ollama import ollama

text = "Artificial intelligence is revolutionizing industry."
    prompt = f"Extract all important multi-word terms and keywords as a list: {text}"
    result = ollama.generate(prompt)
    print("Multi-word keywords:", result)
    ```

5. **Comparison of different prompts:**

Prompt 1:

```prompt
     “Extract keywords: …”
     ```

Prompt 2:

```prompt
    "Return the most important terms as a list: ..."
    ```

Result:

```text
    Different formats but similar content.
    ```

```python
    # File: keywords5_vergleich.py
    from lib.helper_ollama import ollama

text = "AI and robotics are changing the world of work."
    prompt1 = f"Extract keywords: {text}"
    prompt2 = f"Return the most important terms as a list: {text}"
    result1 = ollama.generate(prompt1)
    result2 = ollama.generate(prompt2)
    print("Prompt 1 result:", result1)
    print("Prompt 2 result:", result2)
    ```

### 10 questions and solutions about keyword extraction

1. **What is Keyword Extraction?**
    - *Solution:* Filtering out the most important terms from a text.
2. **What are keywords used for?**
    - *Solution:* Search engines, summaries, tagging, data analysis.
3. **How ​​to extract keywords with LLMs?**
    - *Solution:* Through targeted prompts like “Extract keywords: …”
4. **What is a challenge in keyword extraction?**
    - *Solution:* Synonyms, relevance rating, multi-word terms.
5. **How ​​to structure the output?**
    - *Solution:* As a list, JSON or comma separated.
6. **What is an example of a multi-word keyword?**
    - *Solution:* "Artificial Intelligence"
7. **How ​​to limit the number of keywords?**
    - *Solution:* By specifying in the prompt (e.g. "Name the 3 most important keywords...").
8. **How ​​to extract keywords from PDFs?**
    - *Solution:* Extract text and then use LLM with keyword prompt.
9. **What is a disadvantage of automatic keyword extraction?**
    - *Solution:* Not always perfect relevance, context may be missing.
10. **How ​​to improve keyword quality?**
    - *Solution:* Through post-processing, manual control or better prompts.

---

## Unit 5 — Named Entity Recognition (NER)

### Comprehensive description & basics

Named Entity Recognition (NER) is the task of automatically recognizing proper names such as people, places and organizations in texts. LLMs are particularly suitable for this as they know many examples from their training and can understand context.

**Why is NER important?**

- It helps to extract structured information from unstructured text.
- It is the basis for search engines, knowledge databases, chatbots and many AI applications.
- It enables text data to be linked to external data sources.

**Challenges:**

- Different spellings and abbreviations
- Ambiguity (e.g. "Amazon" as a company or river)
- Nested or compound entities

### 5 Examples of Named Entity Recognition (with Python Code)

1. **Simple Entities:**

Text:

```text
    "Barack Obama spoke in Berlin in 2015."
    ```

Result:

```text
    People: ["Barack Obama"], Places: ["Berlin"], Organizations: []
    ```

```python
    # File: ner1_easy.py
    from lib.helper_ollama import ollama

text = "Barack Obama spoke in Berlin in 2015."
    prompt = f"Find Named Entities (People, Places, Organizations) as JSON: {text}"
    result = ollama.generate(prompt)
    print("Entities:", result)
    ```

2. **Recognize organizations:**

Text:

```text
    "Elon Musk founded SpaceX in California."
    ```

Result:

```text
    People: ["Elon Musk"], Places: ["California"], Organizations: ["SpaceX"]
    ```

```python
    # File: ner2_organization.py
    from lib.helper_ollama import ollama

text = "Elon Musk founded SpaceX in California."
    prompt = f"Find Named Entities (People, Places, Organizations) as JSON: {text}"
    result = ollama.generate(prompt)
    print("Entities:", result)
    ```

3. **Multiple sentences:**

Text:

```text
    "Angela Merkel met Emmanuel Macron in Paris. Microsoft invested in OpenAI."
    ```

Result:

```text
    People: ["Angela Merkel", "Emmanuel Macron"], Places: ["Paris"], Organizations: ["Microsoft", "OpenAI"]
    ```

```python
    # File: ner3_mehrere_saetze.py
    from lib.helper_ollama import ollama

text = "Angela Merkel met Emmanuel Macron in Paris. Microsoft invested in OpenAI."
    prompt = f"Find Named Entities (People, Places, Organizations) as JSON: {text}"
    result = ollama.generate(prompt)
    print("Entities:", result)
    ```

4. **Ambiguous Entities:**

Text:

```text
    "Amazon expands into Brazil."
    ```

Result:

```text
    Organizations: ["Amazon"], Locations: ["Brazil"]
    ```

```python
    # File: ner4_ambiguous.py
    from lib.helper_ollama import ollama

text = "Amazon is expanding into Brazil."
    prompt = f"Find Named Entities (People, Places, Organizations) as JSON: {text}"
    result = ollama.generate(prompt)
    print("Entities:", result)
    ```

5. **JSON output:**

Text:

```text
    "Jeff Bezos founded Amazon in Seattle."
    
```

Result:

```text
    {"People": ["Jeff Bezos"], "Places": ["Seattle"], "Organizations": ["Amazon"]}
    ```

```python
    # File: ner5_json.py
    from lib.helper_ollama import ollama

text = "Jeff Bezos founded Amazon in Seattle."
    prompt = f"Extract Named Entities in JSON format: {{'People': [], 'Places': [], 'Organizations': []}} Text: {text}"
    result = ollama.generate(prompt)
    print("Entities JSON:", result)
    ```

### 10 questions and solutions about Named Entity Recognition

1. **What is Named Entity Recognition?**
    - *Solution:* The automatic recognition of proper names (people, places, organizations) in texts.
2. **Name three types of entities.**
    - *Solution:* People, places, organizations.
3. **Why is NER important for AI applications?**
    - *Solution:* It provides structured information for search, databases, chatbots etc.
4. **What is a challenge in NER?**
    - *Solution:* Ambiguity, different spellings, nested entities.
5. **How ​​to structure the output?**
    - *Solution:* As lists or in JSON format.
6. **How ​​to test NER with LLMs?**
    - *Solution:* Through targeted prompts and comparing the results.
7. **What is an example of an organization as an entity?**
    - *Solution:* "Microsoft", "Amazon", "SpaceX"
8. **How ​​to extract entities from multiple sentences?**
    - *Solution:* Have the text analyzed as a whole, output lists if necessary.
9. **What is a disadvantage of automatic NER?**
    - *Solution:* Error with unknown names, abbreviations or context.
10. **How ​​to improve the quality of NER results?**
    - *Solution:* Through better prompts, post-processing or combination with other tools.

---

## Unit 6 — FAQ Bot with Ollama

### Comprehensive description & basics

An FAQ bot (Frequently Asked Questions Bot) is a system that automatically answers frequently asked questions. The answers are based on a given FAQ list or document. LLMs can make such bots particularly flexible because they can also recognize and answer similar or reformulated questions.

**Why are FAQ bots useful?**

- You relieve support teams and answer standard questions around the clock.
- They improve the user experience on websites and in apps.
- They can be easily expanded with new questions and answers.

**Challenges:**

- Questions can be worded differently.
- Answers must be precise and correct.
- Dealing with questions that are not in the FAQ.

### 5 Examples of FAQ Bot Applications (with Python Code)

1. **Simple FAQ as text:**

FAQ:

```text
    "Q: What is Python?\nA: A programming language."
    ```

Ask:

```text
    "What is Python?"
    ```

Result:

```text
    "A programming language."
    ```

```python
    # File: faq1_easy.py
    from lib.helper_ollama import ollama

faq = "Q: What is Python?\nA: A programming language."
    question = "What is Python?"
    prompt = f"Answer the question based on this FAQ:\n{faq}\n\nQuestion: {question}"
    result = ollama.generate(prompt)
    print("Answer:", result)
    ```

2. **Question rephrased:**
    FAQ:

```text
    "Q: What is AI?\nA: Machines that solve tasks like humans."
    ```

Ask:

```text
    “What is meant by artificial intelligence?”
    ````

Result:

```text
    "Machines that solve tasks like humans."
    ```

```python
    # File: faq2_reformulated.py
    from lib.helper_ollama import ollama

faq = "Q: What is AI?\nA: Machines that solve tasks like humans."
    question = "What is meant by artificial intelligence?"
    prompt = f"Answer the question based on this FAQ:\n{faq}\n\nQuestion: {question}"
    result = ollama.generate(prompt)
    print("Answer:", result)
    ```

3. **File Upload:**
    - FAQ is loaded from an uploaded file and searched.
    - **Python code (Streamlit):**

```python
    # File: faq3_upload.py
    import streamlit as st
    from lib.helper_ollama import ollama

st.title("FAQ bot with file upload")
    file = st.file_uploader("Upload FAQ", type="txt")
    question = st.text_input("Ask a question:")
    if file and question:
        faq = file.read().decode()
        prompt = f"Answer the question based on this FAQ:\n{faq}\n\nQuestion: {question}"
        if st.button("Reply"):
            result = ollama.generate(prompt)
            st.write("Answer:", result)
    ```

4. **Combine multiple FAQ files:**
    - Multiple documents are merged to expand knowledge.
    - **Python code (Streamlit):**

```python
    # File: faq4_multiple_uploads.py
    import streamlit as st
    from lib.helper_ollama import ollama

st.title("FAQ bot with multiple files")
    files = st.file_uploader("Upload multiple FAQs", type="txt", accept_multiple_files=True)
    question = st.text_input("Ask a question:")
    if files and question:
        faq_data = "\n".join([f.read().decode() for f in files])
        prompt = f"Answer the question based on this FAQ:\n{faq_data}\n\nQuestion: {question}"
        if st.button("Reply"):
            result = ollama.generate(prompt)
            st.write("Answer:", result)
    ```

5. **Dealing with unknown questions:**

Ask:

```text
    "How does quantum computing work?" (not in FAQ)
    ```

Result:

```text
    "Unfortunately, this question is not included in the FAQ."
    ```

```python
    # File: faq5_unknown.py
    from lib.helper_ollama import ollama

faq = "Q: What is Python?\nA: A programming language."
    question = "How does quantum computing work?"
    prompt = f"Answer the question based on this FAQ. If the answer is not included, say: 'Unfortunately, this question is not included in the FAQ.'\n{faq}\n\nQuestion: {question}"
    result = ollama.generate(prompt)
    print("Answer:", result)
    ```

### 10 questions and solutions about FAQ bots

1. **What is an FAQ bot?**
    - *Solution:* A system that automatically answers frequently asked questions.
2. **How ​​can an FAQ bot be expanded?**
    - *Solution:* By adding new questions and answers to the FAQ list.
3. **What is a challenge with FAQ bots?**
    - *Solution:* Different wording of the questions.
4. **How ​​to build an FAQ bot with LLMs?**
    - *Solution:* Add FAQ as context in the prompt and attach the question.
5. **How ​​to use multiple FAQ files?**
    - *Solution:* Merge files and use as context.
6. **How ​​should the bot react if a question is not in the FAQ?**
    - *Solution:* Kindly point out that the answer is not known.
7. **What is a benefit of LLM based FAQ bots?**
    - *Solution:* You also recognize reformulated or similar questions.
8. **How ​​can you ensure the quality of the answers?**
    - *Solution:* Check and update FAQ regularly.
9. **How ​​to integrate an FAQ bot into an app?**
    - *Solution:* With Streamlit, web frameworks or chatbots.
10. **What is a disadvantage of FAQ bots?**
    - *Solution:* You cannot solve complex, individual problems.

---

## Unit 7 — Combining Analytics (Sentiment + Keywords + Entities)

### Comprehensive description & basics

LLMs are capable of completing multiple analysis tasks in one step. This means you can simultaneously extract sentiment, keywords, named entities and even summaries from a text with a single prompt. This saves time and enables complex evaluations with little code.

**Why is combining analytics useful?**

- It provides a comprehensive picture of a text at a glance.
- It saves computing time and simplifies workflows.
- It is ideal for dashboards, monitoring and automated reports.

**Challenges:**

- The formatting of the output must be clearly specified.
- The results may need to be post-processed or parsed.
- With very long texts, the context window of the model can be exceeded.

### 5 Examples of Combined Analysis (with Python Code)

1. **Mood + Keywords:**

Text:

```text
    "The new iPhone is impressive, but very expensive."
    ```

Result:

```text
    Mood: "Mixed", Keywords: ["iPhone", "expensive"]
    ```

```python
    # File: kombi1_stimm_keywords.py
    from lib.helper_ollama import ollama

text = "The new iPhone is impressive, but very expensive."
    prompt = f"Analyze this text and return:\n1. Sentiment (Positive/Negative/Neutral/Mixed)\n2. Keywords as a list\nText: {text}"
    result = ollama.generate(prompt)
    print("Analysis:", result)
    ```

2. **All in one:**

Text:

```text
    "Angela Merkel gave a speech about the EU in Berlin."
    ```

Result:

```text
    Sentiment, Keywords, Named Entities, Summary
    ```

```python
    # File: kombi2_alles.py
    from lib.helper_ollama import ollama

text = "Angela Merkel gave a speech about the EU in Berlin."
    prompt = f"Analyze the text and return:\n- Sentiment\n- Keywords\n- Named Entities\n- Short summary\nText: {text}"
    result = ollama.generate(prompt)
    print("Analysis:", result)
    ```

3. **JSON output:**

Prompt:

```prompt
    "Parse the text and return the result as JSON: sentiment, keywords, entities."
    ```

```python
    # File: kombi3_json.py
    from lib.helper_ollama import ollama

text = "Tesla invests in AI and builds new factories."
    prompt = f"Parse the text and return the result as JSON: Sentiment, Keywords, Entities. Text: {text}"
    result = ollama.generate(prompt)
    print("JSON parse:", result)
    ```

4. **Analyze multiple texts:**
    - List of texts is parsed in a loop
    - Results are collected.

```python
    # File: kombi4_multiple.py
    from lib.helper_ollama import ollama

texts = [
        "The new iPhone is impressive, but very expensive.",
        "Angela Merkel gave a speech about the EU in Berlin.",
        "Tesla is investing in AI and building new factories."
    ]
    for text in text:
        prompt = f"Parse the text and return the result as JSON: Sentiment, Keywords, Entities. Text: {text}"
        result = ollama.generate(prompt)
        print(f"Text: {text}\nAnalysis: {result}\n")
    ```

5. **Dashboard Application:**
    - A Streamlit dashboard clearly shows all analysis results for each text.

```python
    # File: kombi5_dashboard.py
    import streamlit as st
    from lib.helper_ollama import ollama

st.title("Combined Text Analysis")
    text = st.text_area("Enter text")
    if st.button("Analyze") and text:
        prompt = f"Parse the text and return the result as JSON: sentiment, keywords, entities, summary. Text: {text}"
        result = ollama.generate(prompt)
        st.write("Analysis:", result)
    ```

### 10 questions and solutions about combined analysis

1. **What does combined analysis mean in LLMs?**
    - *Solution:* Multiple analysis tasks (e.g. sentiment, keywords, entities) are completed in one step.
2. **What is an advantage of combined analysis?**
    - *Solution:* Saves time, provides comprehensive results.
3. **How ​​to structure the output?**
    - *Solution:* Through clear specifications in the prompt, e.g. B. Lists or JSON.
4. **What is a disadvantage of very long texts?**
    - *Solution:* The context window of the model can be exceeded.
5. **How ​​to use combined analytics in one app?**
    - *Solution:* In dashboards, monitoring tools, reports.
6. **How ​​can you further process the results?**
    - *Solution:* By parsing the output (e.g. JSON in Python).
7. **What is an example of a combined analysis?**
    - *Solution:* Extract sentiment, keywords and entities from a text.
8. **How ​​to automatically analyze multiple texts?**
    - *Solution:* With a loop and an analysis function.
9. **How ​​to improve the quality of the combined analysis?**
    - *Solution:* Through precise prompts and format specifications.
10. **What is a typical error in combined analysis?**
    - *Solution:* Unclear format specifications, texts that are too long, lack of post-processing.

---

## Unit 8 — Advanced Streamlit App: Analytics Dashboard

### Comprehensive description & basics

An analysis dashboard is an interactive app that combines various text analysis functions in a clear interface. With Streamlit you can quickly and easily build a dashboard that combines sentiment analysis, keyword extraction, named entity recognition and summarization. Users can enter text, upload it or select from a list and receive a comprehensive analysis immediately.

**Why are dashboards useful?**

- They make complex analyzes accessible to everyone.
- They enable quick evaluations without programming knowledge.
- They are ideal for presentations, monitoring and prototyping.

**Challenges:**

- Clear presentation of the results
- Performance with large amounts of text
- Flexibility for different types of analysis

### 5 Examples of Analytics Dashboards (with Python Code)

1. **Simple text field:**

User enters text, dashboard shows all analyzes.

```python
    # File: dashboard1_textfeld.py
    import streamlit as st
    from lib.helper_ollama import ollama

st.title("Text Analysis Dashboard")
    text = st.text_area("Enter text")
    if st.button("Analyze") and text:
        prompt = f"Parse the text and return the result as JSON: sentiment, keywords, entities, summary. Text: {text}"
        result = ollama.generate(prompt)
        st.write("Analysis:", result)
    ```

2. **File Upload:**

User uploads a PDF or text file, Dashboard analyzes the entire content.

```python
    # File: dashboard2_upload.py
    import streamlit as st
    from lib.helper_ollama import ollama

st.title("File Upload Analysis")
    file = st.file_uploader("Upload text file", type=["txt"])
    if file:
        text = file.read().decode()
        if st.button("Analyze"):
            prompt = f"Parse the text and return the result as JSON: sentiment, keywords, entities, summary. Text: {text}"
            result = ollama.generate(prompt)
            st.write("Analysis:", result)
    ```

3. **Compare multiple texts:**

Dashboard shows analysis results for several texts side by side.

```python
    # File: dashboard3_vergleich.py
    import streamlit as st
    from lib.helper_ollama import ollama

st.title("Comparison of several texts")
    texts = st.text_area("Texts (separated by line breaks)")
    if st.button("Analyze") and texte:
        text_list = [t for t in texte.split("\n") if t.strip()]
        cols = st.columns(len(text_list))
        for i, text in enumerate(text_list):
            prompt = f"Parse the text and return the result as JSON: sentiment, keywords, entities, summary. Text: {text}"
            result = ollama.generate(prompt)
            with cols[i]:
                st.write(f"**Text {i+1}:**", text)
                st.write(result)
    ```

4. **Results as table:**
    - All analyzes are displayed in a table or as JSON.
    - **Python code (Streamlit + pandas):**

```python
    # File: dashboard4_table.py
    import streamlit as st
    import pandas as pd
    from lib.helper_ollama import ollama

st.title("Analysis as a table")
    texts = st.text_area("Texts (one text per line)")
    if st.button("Analyze") and texte:
        text_list = [t for t in texte.split("\n") if t.strip()]
        data = []
        for text in text_list:
            prompt = f"Parse the text and return the result as JSON: sentiment, keywords, entities, summary. Text: {text}"
            result = ollama.generate(prompt)
            data.append({"Text": text, "Analysis": result})
        df = pd.DataFrame(data)
        st.dataframe(df)
    ```

5. **Export function:**

Results can be exported as CSV or PDF.

```python
    # File: dashboard5_export.py
    import streamlit as st
    import pandas as pd
    from lib.helper_ollama import ollama

st.title("Analysis with export")
    texts = st.text_area("Texts (one text per line)")
    if st.button("Analyze") and texte:
        text_list = [t for t in texte.split("\n") if t.strip()]
        data = []
        for text in text_list:
            prompt = f"Parse the text and return the result as JSON: sentiment, keywords, entities, summary. Text: {text}"
            result = ollama.generate(prompt)
            data.append({"Text": text, "Analysis": result})
        df = pd.DataFrame(data)
        st.dataframe(df)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", csv, "analyses.csv", "text/csv")
    ```

### 10 questions and solutions about analysis dashboards

1. **What is an analytics dashboard?**
    - *Solution:* An app that combines various analysis functions in one interface.
2. **How ​​to build a dashboard with Streamlit?**
    - *Solution:* Using Python and the Streamlit library.
3. **What analytics features can a dashboard include?**
    - *Solution:* Sentiment, keywords, NER, summary, and much more. m.
4. **What is a benefit of dashboards?**
    - *Solution:* You make analyzes accessible and easy to use for everyone.
5. **How ​​can you compare multiple texts?**
    - *Solution:* By displaying the results side by side or in a table.
6. **How ​​to export results?**
    - *Solution:* As CSV, PDF or by copying the data.
7. **What is challenging with large amounts of text?**
    - *Solution:* Performance and clarity.
8. **How ​​can you increase user-friendliness?**
    - *Solution:* Clear structure, easy operation, good visualization.
9. **How ​​to extend the dashboard?**
    - *Solution:* Add more analysis functions, filters, visualizations.
10. **What is a typical dashboard error?**
    - *Solution:* Confusing display, missing export or comparison functions.

---

## Unit 9 - Summary

After Day 3, students can:

- Analyze texts with Ollama (mood, topics, keywords, entities)
- create an FAQ bot with documents
- combine multiple analyses
- Build your own analytics dashboard in Streamlit
- recognize the limitations of such models (hallucinations, ambiguity)

---

## Unit 10 - Mini Projects

### Mini Project 1: Intelligent PDF Analyzer

**Task:** Build an app that uploads PDF documents and analyzes them with AI.

**Solution:**

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

### Mini Project 2: Multi-Language Content Analyzer

**Task:** Analyze and translate texts in different languages.

**Solution:**

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

### Mini Project 3: Social Media Content Optimizer

**Task:** Optimize texts for various social media platforms.

**Solution:**

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

### Mini Project 4: Competitive Content Analysis

**Task:** Compare competitor content and analyze their strategies.

**Solution:**

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

### Mini Project 5: Real-time Content Monitoring Dashboard

**Task:** Monitor and analyze content in real time.

**Solution:**

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
