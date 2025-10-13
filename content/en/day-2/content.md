# Day 2 — Working with LLMs & Prompt Engineering

## Unit 1 — Schedule 09:00 – 15:00

### Overview

The day offers a practical introduction to Large Language Models (LLMs) and prompt engineering. Each unit combines short explanations, code examples and practical exercises.

---

### Schedule

| time | Unit / Content | Duration |
|-----------------|---------------------------------------------------------------------------------|---------|
| **09:00 – 09:20** | Introduction & Overview - What are LLMs? Goals of the day | 20 mins |
| **09:20 – 09:50** | **Unit 2.1:** Introduction to LLMs - background, areas of application, limitations | 30 mins |
| **09:50 – 10:20** | **Unit 2.2:** What is a prompt? - Prompt elements, examples, exercises | 30 mins |
| **10:20 – 10:50** | **Unit 2.3:** Roles in Prompting & Basics - System/User/Assistant, Prompt Engineering | 30 mins |
| **10:50 – 11:05** | ☕ **Break** | 15 mins |
| **11:05 – 11:35** | **Unit 2.4:** Prompting Principles - Zero-/Few-Shot, Chain-of-Thought, Output Format | 30 mins |
| **11:35 – 12:05** | **Unit 2.5:** Prompt Playground & Comparison - Streamlit App, Prompt Experiments | 30 mins |
| **12:05 – 1:05 pm** | 🍽️ **Lunch break** | 60 mins |
| **1:05 - 1:35 pm** | **Unit 2.6:** Temperature & Creativity - Parameters, Temperature, Max Tokens | 30 mins |
| **1:35 p.m. – 2:05 p.m.** | **Unit 2.7:** Comparison of different models - llama2, mistral, codellama | 30 mins |
| **14:05 – 14:35** | **Unit 2.8:** Errors & Limitations of LLMs - Hallucinations, Bias, Context | 30 mins |
| **14:35 – 14:55** | **Unit 2.9:** Practical Prompt Examples - Summary, Roles, Code, JSON | 20 mins |
| **14:55 – 15:00** | **Summary & Outlook** - Review, Questions, Next Steps | 5 min |

---

## Unit 1 — Introduction to Large Language Models (LLMs)

### Description & Basics

Large Language Models (LLMs) are artificial intelligences trained on massive amounts of text data. They use neural networks, particularly transformer architectures, to understand and generate language. Well-known representatives are GPT (OpenAI), Llama (Meta), Mistral and Gemma (Google). LLMs are fed billions of text examples and learn to predict the most likely next word. As a result, they develop the ability to write complex texts, answer questions, translate or even generate code.

**How ​​do LLMs work?**

- You analyze the entered text (prompt) and calculate which word fits best next.
- They do not have a real “understanding” like a human, but rather recognize patterns and probabilities.
- They can be specialized in different tasks (e.g. chatbots, translators, code generators).

**Areas of application:**

- Automatic text generation (e.g. emails, stories, summaries)
- Translations between languages
- Answering questions (Q&A)
- Support with programming (code completion, error explanation)
- Creative tasks (poems, brainstorming)

**Limits and Challenges:**

- LLMs can “hallucinate”, i.e. invent plausible but false information.
- They are not deterministic: the same prompt can give different answers.
- You have a limited context window (can only remember a certain amount of text).
- They adopt prejudices from the training data.
- You can't look up real facts, only training data.

### 5 Examples of Using LLMs (with Python Code)

1. **Text summary:**

    Prompt:

    ```prompt
            "Summarize the following text in 2 sentences: ..."
    ```

    ```python
        # File: example1_summary.py
        from lib.helper_ollama import ollama
        text = "Artificial intelligence is a branch of computer science ..."
        prompt = f"Summarize the following text into 2 sentences:\n{text}"
        result = ollama.generate(prompt)
        print(result)
    ```

2. **Answer questions:**

    Prompt:

    ```prompt
            "What is the difference between AI and ML?"
    ```

    ```python
        # File: example2_questions.py
        from lib.helper_ollama import ollama
        prompt = "What is the difference between AI and ML?"
        result = ollama.generate(prompt)
        print(result)
    ```

3. **Generate code:**

    Prompt:

    ```prompt
            "Write a Python function that calculates the factorial."
        ```

    ```python
        # File: example3_code.py
        from lib.helper_ollama import ollama
        prompt = "Write a Python function that calculates the factorial."
        result = ollama.generate(prompt)
        print(result)
    ```

4. **Translate:**

    Prompt:

    ```prompt
            "Translate into English: 'Good morning, how are you?'"
        ```

    ```python
        # File: example4_ueberstellen.py
        from lib.helper_ollama import ollama
        prompt = "Translate into English: 'Good morning, how are you?'"
        result = ollama.generate(prompt)
        print(result)
    ```

5. **Write creative texts:**

    Prompt:

    ```prompt
            "Write a short poem about autumn."
        ```

    ```python
        # File: example5_poem.py
        from lib.helper_ollama import ollama
        prompt = "Write a short poem about autumn."
        result = ollama.generate(prompt)
        print(result)
    ```

### 10 Questions and Solutions on LLMs

1. **What is a Large Language Model (LLM)?**

*Solution:* An AI model trained on large amounts of text that can generate speech.
2. **Name two well-known LLMs.**

*Solution:* GPT, Llama, Mistral, Gemma (name two each)
3. **What does “hallucinate” mean in LLMs?**

*Solution:* The model invents plausible but false information.
4. **Why are LLMs not deterministic?**

*Solution:* They work probabilistically, so the same input can result in different outputs.
5. **What can LLMs be used for?**

*Solution:* Text generation, translation, Q&A, code generation, summary, creative tasks
6. **What is a context window?**

*Solution:* The maximum amount of text the model can process at one time.
7. **What is a disadvantage of LLMs?**

*Solution:* Hallucinations, bias, limited window of context, no real understanding
8. **How ​​do LLMs learn?**

*Solution:* By training on large amounts of text and predicting the next word.
9. **Can LLMs look up facts?**

*Solution:* No, they just rely on their training knowledge.
10. **What is a common mistake when using LLMs?**

*Solution:* Too much confidence in the correctness of the generated answers.

---

## Unit 2 — What is a prompt?

### Comprehensive description & basics

A prompt is the input that a human uses to control a language model (LLM). It is the “question” or “instruction” that the model answers. The quality and clarity of the prompt largely determine the quality of the answer. A prompt can be a simple question, a complex task or a detailed instruction. Good prompts are precise, contain context, and specify the desired output format.

**Elements of a good prompt:**

- **Role:** In what role should the model respond? (e.g. “You are a teacher…”)
- **Context:** Background information or data to which the answer should refer
- **Task:** The actual instruction (e.g. “Summarize the text”)
- **Format:** Desired output form (e.g. bulletpoints, JSON, table)

**Why is prompt engineering important?**

- Different formulations lead to different results.
- A clear prompt reduces misunderstandings and errors.
- With targeted prompts you can guide the model to better, more structured answers.

### 5 Examples of Prompts (with Python Code)

1. **Simple question:**

Prompt:

```prompt
        "What is artificial intelligence?"
    ```

```python
    # File: prompt1_simple_question.py
    from lib.helper_ollama import ollama
    prompt = "What is artificial intelligence?"
    result = ollama.generate(prompt)
    print(result)
    ```

2. **Assign role:**

+Prompt: "You are a math teacher. Explain the Pythagorean theorem."

```python
    # File: prompt2_rolle.py
    from lib.helper_ollama import ollama
    prompt = "You are a math teacher. Explain the Pythagorean theorem."
    result = ollama.generate(prompt)
    print(result)
    ```

3. **Include context:**

Prompt: "Here is a text: 'Python is a programming language...'. Summarize it in 2 sentences."

```python
    # File: prompt3_context.py
    from lib.helper_ollama import ollama
    text = "Python is a programming language..."
    prompt = f"Here is a text: '{text}'. Summarize it in 2 sentences."
    result = ollama.generate(prompt)
    print(result)
    ```

4. **Request format:**

Prompt: "Give three benefits of solar energy as a numbered list."

```python
    # File: prompt4_format.py
    from lib.helper_ollama import ollama
    prompt = "Give three advantages of solar energy as a numbered list."
    result = ollama.generate(prompt)
    print(result)
    ```

5. **Combined task:**

Prompt: "You are a travel advisor. Recommend me 3 travel destinations in Italy and give a short reason for each in the form of a table."

```python
    # File: prompt5_combined.py
    from lib.helper_ollama import ollama
    prompt = "You are a travel advisor. Recommend me 3 travel destinations in Italy and give a short explanation for each in a table."
    result = ollama.generate(prompt)
    print(result)
    ```

### 10 questions and solutions about prompts

1. **What is a prompt?**

*Solution:* The prompt/prompt that a human gives to an LLM.
2. **Name two important elements of a good prompt.**

*Solution:* Role, context, task, format (name two each)
3. **Why is prompt wording important?**

*Solution:* It affects the quality and accuracy of the answer.
4. **How ​​to specify the desired output format?**

*Solution:* By explicitly describing it in the prompt (e.g. “as a table”).
5. **What happens if a prompt is too vague?**

*Solution:* The model often gives inaccurate or unwanted answers.
6. **How ​​do you add context to a prompt?**

*Solution:* By adding background information or examples.
7. **What is an example of a prompt with a role?**

*Solution:* "You are a teacher. Explain..."
8. **How ​​to get the model to give a structured answer?**

*Solution:* By specifying the format (e.g. bulletpoints, JSON)
9. **What is Prompt Engineering?**

*Solution:* The art of designing prompts so that the model delivers optimal results.
10. **How ​​can you specifically control the response of an LLM?**

*Solution:* Through precise, clear and formatted prompts.

---

## Unit 3 — Roles in Prompting & Prompt Engineering: Basics

### Description & Basics

Prompt engineering is the targeted design of inputs (prompts) in order to obtain optimal results from LLMs. A central concept here is **roles**: Modern LLM APIs such as OpenAI or Ollama use messages with different roles to clearly separate contexts and tasks. The most important roles are:

- **system:** Defines the identity and behavior of the model (e.g. “You are a helpful tutor.”)
- **user:** Contains the user's actual request.
- **assistant:** (Optional) Previous replies from the model to continue conversations.
- **tool/function:** (In advanced frameworks) For special function calls.

Combining these roles can structure conversations, control context, and improve the quality of responses. Different formulations and roles lead to different results. Prompt engineering also includes testing, comparing and optimizing prompts.

**Why are roles important?**

- They help to structure communication with the model.
- They make it possible to separate contexts and tasks.
- They make conversations understandable and reproducible.

### 5 Examples of Roles in Prompting (with Python Code)

1. **Set system role:**

**System**: "You are a helpful math teacher."

**User**: "Explain the Pythagorean theorem."

```python
    # File: rolls1_system.py
    from lib.helper_ollama import ollama
    prompt = "System: You are a helpful math teacher.\nUser: Explain the Pythagorean theorem."
    result = ollama.generate(prompt)
    print(result)
    ```

2. **User role with context:**

**System**: "You are a travel expert."

**User**: "Recommend three travel destinations in Japan."

```python
    # File: roles2_user.py
    from lib.helper_ollama import ollama
    prompt = "System: You are a travel expert.\nUser: Recommend three travel destinations in Japan."
    result = ollama.generate(prompt)
    print(result)
    ```

3. **Conversation Assistant Role:**

**System**: "You are a chatbot."

**User**: “What is AI?”

**Assistant**: "Artificial intelligence is..."

**User**: "Give an example of AI in everyday life."

```python
    # File: rolls3_assistant.py
    from lib.helper_ollama import ollama
    prompt = "System: You are a chatbot.\nUser: What is AI?\nAssistant: Artificial intelligence is...\nUser: Give an example of AI in everyday life."
    result = ollama.generate(prompt)
    print(result)
    ```

4. **Comparison of Prompts:**
    - Prompt 1: “Briefly summarize the text.”
    - Prompt 2: "Create a detailed summary in 5 sentences."

```python
    # File: rolls4_comparison.py
    from lib.helper_ollama import ollama
    text = "Artificial intelligence is a branch of computer science ..."
    prompt1 = f"Summarize the text briefly.\nText: {text}"
    prompt2 = f"Create a detailed summary in 5 sentences.\nText: {text}"
    result1 = ollama.generate(prompt1)
    result2 = ollama.generate(prompt2)
    print("Short:", result1)
    print("Lang:", result2)
    ```

5. **Tool/Function Role (Advanced):**

**System**: "You can solve arithmetic problems."

**User**: "Calculate 23 + 42."

**Tool/Function**: "65"

```python
    # File: rolls5_tool.py
    from lib.helper_ollama import ollama
    prompt = "System: You can solve calculation problems.\nUser: Calculate 23 + 42.\nTool/Function: 65"
    result = ollama.generate(prompt)
    print(result)
    ```

### 10 questions and solutions about roles and prompt engineering

1. **What is Prompt Engineering?**

*Solution:* The targeted design of prompts to get optimal results from LLMs.
2. **What role defines the behavior of the model?**

*Solution:* The system role.
3. **What does the user role stand for?**

*Solution:* For the user's request.
4. **How ​​to structure conversations with LLMs?**

*Solution:* By using different roles (system, user, assistant).
5. **What is the benefit of the Assistant role?**

*Solution:* It allows for ongoing conversations and context.
6. **How ​​to improve the quality of answers?**

*Solution:* Through clear role distribution and precise prompts.
7. **What is an example of a system role prompt?**

*Solution:* “You are a kind teacher.”
8. **Why is separating context and task important?**

*Solution:* To avoid misunderstandings and receive targeted answers.
9. **How ​​to test and compare prompts?**

*Solution:* Through different formulations and analysis of the results.
10. **What is a typical error in prompt engineering?**

*Solution:* Unclear roles or tasks, lack of context.

---

## Unit 4 — Prompting Principles

### Comprehensive description & basics

To get the best results from LLMs, there are various prompting principles and strategies. They help to specifically control the answers, avoid errors and use the creativity of the model. The most important principles are:

- **Zero-Shot Prompting:** The model only receives the task, but no examples. It has to solve the task “right away”.
- **Few-Shot Prompting:** The prompt also contains examples of how the task should be solved. The model can be based on this.
- **Role Prompting:** The model is put into a specific role (e.g. “You are a doctor…”) to influence the response.
- **Chain-of-Thought (CoT):** The model is asked to think and reason step by step.
- **Self-Consistency:** Multiple answers are generated to select the best or most consistent one.
- **Output format prompting:** The desired output format is explicitly specified (e.g. JSON, table, bulletpoints).

**Why are these principles important?**

- They increase the reliability and traceability of the answers.
- They help to avoid mistakes and misunderstandings.
- They enable structured, formatted and creative results.

### 5 Examples of Prompting Principles (with Python Code)

1. **Zero-Shot Prompting:**

Prompt:

```prompt
        "Translate the following sentence into French: 'I love AI.'"
    ```

```python
    # File: principle1_zeroshot.py
    from lib.helper_ollama import ollama
    prompt = "Translate the following sentence into French: 'I love AI.'"
    result = ollama.generate(prompt)
    print(result)
    ```

2. **Few-Shot Prompting:**

Prompt:

```prompt "Translation into French:\German: Hello → French: Bonjour\German: Thank you → French: Merci\nGerman: I love AI → French:" ```

```python
    # File: principle2_fewshot.py
    from lib.helper_ollama import ollama
    prompt = "Translate into French:\nGerman: Hello → French: Bonjour\nGerman: Thank you → French: Merci\nGerman: I love AI → French:"
    result = ollama.generate(prompt)
    print(result)
    ```

3. **Role Prompting:**

Prompt:

```prompt
        "You are a doctor. Explain the symptoms of flu to a patient in simple language."
    ```

```python
    # File: principle3_role.py
    from lib.helper_ollama import ollama
    prompt = "You are a doctor. Explain the symptoms of flu to a patient in simple language."
    result = ollama.generate(prompt)
    print(result)
    ```

4. **Chain-of-Thought Prompting:**

Prompt:

```prompt
        "Solve the problem step by step: An apple costs €2, an orange costs €3. How much does it cost to buy 4 apples and 2 oranges?"
    ```

```python
    # File: principle4_chainofthought.py
    from lib.helper_ollama import ollama
    prompt = "Solve the problem step by step: An apple costs €2, an orange costs €3. How much does it cost to buy 4 apples and 2 oranges?"
    result = ollama.generate(prompt)
    print(result)
    ```

5. **Output Format Prompting:**

Prompt:

```prompt
    "Answer in JSON format: {\"Name\": \"<string>\", \"Age\": <int>} Question: Person's name is Alice and she is 30 years old."
    ```

```python
    # File: principle5_format.py
    from lib.helper_ollama import ollama
    prompt = "Answer in JSON format: {\"Name\": \"<string>\", \"Age\": <int>} Question: Person's name is Alice and she is 30 years old."
    result = ollama.generate(prompt)
    print(result)
    ```

### 10 questions and solutions about prompting principles

1. **What is Zero-Shot Prompting?**

*Solution:* The model only receives the task, but no examples.
2. **How ​​does Few-Shot Prompting help?**

*Solution:* Using examples, the model can better understand and solve the task.
3. **What is Role Prompting?**

*Solution:* The model is placed in a specific role to influence the answer.
4. **What is chain-of-thought prompting used for?**

*Solution:* The model is asked to think and reason step by step.
5. **What is Self-Consistency?**

*Solution:* Multiple answers are generated to select the best one.
6. **How ​​to control the output format?**

*Solution:* By explicitly specifying it in the prompt (e.g. “in JSON format”).
7. **Why are examples helpful in the prompt?**

*Solution:* You show the model how the task should be solved.
8. **What is a disadvantage of zero-shot prompting?**

*Solution:* The answer may be inaccurate or unexpected because there are no examples.
9. **How ​​to encourage model creativity?**

*Solution:* Through open tasks and creative roles.
10. **What is a common error in prompting principles?**

*Solution:* Missing examples, unclear roles or no format given.

---

st.title("Prompt Playground")
st.title("Prompt Comparison")
p1 = st.text_area("Prompt 1")
p2 = st.text_area("Prompt 2")

## Unit 5 — Prompt Playground & Prompt Comparison (Streamlit App)

### Comprehensive description & basics

A prompt playground is an interactive application that allows you to try out prompts directly and see the answers from LLMs immediately. This is particularly helpful for testing the effect of small changes to the prompt and understanding how different models respond to identical or slightly modified prompts. A prompt playground promotes experimental learning and is a central tool in prompt engineering.

**Advantages of a prompt playground:**

- Immediate feedback on prompts
- Comparison of different models and parameters
- Promoting creativity and experimentation
- Ideal for workshops, teaching and development

**Prompt comparison:**
With a comparison function you can directly compare two (or more) prompts and analyze the differences in the answers. This helps to understand the effect of formulations, roles or parameters.

### 5 examples of Playground experiments (with Python/Streamlit code)

1. **Prompt Variation:**

Prompt 1:

```prompt
    "Summarize the text in 1 sentence."
    ```

Prompt 2:

```prompt
    "Summarize the text in 3 bullet points."
    ```

```python
    # File: playground1_variation.py
    from lib.helper_ollama import ollama
    text = "Artificial intelligence is a branch of computer science ..."
    prompt1 = f"Summarize the text into 1 sentence.\nText: {text}"
    prompt2 = f"Summarize the text into 3 bullet points.\nText: {text}"
    result1 = ollama.generate(prompt1)
    result2 = ollama.generate(prompt2)
    print("1 sentence:", result1)
    print("3 Bulletpoints:", result2)
    ```

2. **Model comparison:**

Prompt:

```prompt
    "Explain the difference between a dog and a cat."
    ```

Models:

```text
    llama2 vs. mistral
    ```

```python
    # File: playground2_modellvergleich.py
    from lib.helper_ollama import ollama
    prompt = "Explain the difference between a dog and a cat."
    result_llama2 = ollama.generate(prompt, model="llama2")
    result_mistral = ollama.generate(prompt, model="mistral")
    print("llama2:", result_llama2)
    print("mistral:", result_mistral)
    ```

3. **Parameter experiment:**

Prompt:

```prompt
    "Write a creative story about a robot."
    - Temperature: 0.2 vs. 1.2
    ```

```python
    # File: playground3_parameter.py
    from lib.helper_ollama import ollama
    prompt = "Write a creative story about a robot."
    result_low = ollama.generate(prompt, temperature=0.2)
    result_high = ollama.generate(prompt, temperature=1.2)
    print("Temp 0.2:", result_low)
    print("Temp 1.2:", result_high)
    ```

4. **Format Experiment:**

Prompt:

```prompt
    "Output the response as a JSON object."
    ```

```python
    # File: playground4_format.py
    from lib.helper_ollama import ollama
    prompt = "Output the answer as a JSON object: What is AI?"
    result = ollama.generate(prompt)
    print(result)
    ```

5. **Role Experiment (Streamlit):**

Prompt:

```prompt
    "You are a doctor. Explain the symptoms of the flu."

Prompt:

```prompt
    "You are an elementary school teacher. Explain the symptoms of the flu."
    - **Streamlit code:**

```python
    # File: playground5_rolle_streamlit.py
    import streamlit as st
    from lib.helper_ollama import ollama

st.title("Role Experiment")
    role = st.selectbox("Select role", ["Doctor", "Elementary school teacher"])
    if role == "Doctor":
        prompt = "You are a doctor. Explain the symptoms of the flu."
    else:
        prompt = "You are an elementary school teacher. Explain the symptoms of the flu."
    if st.button("Generate response"):
        result = ollama.generate(prompt)
        st.write(result)
    ```

### 10 questions and solutions about Prompt-Playground & comparison

1. **What is a prompt playground?**

*Solution:* An app where you can try out prompts and see the answers from LLMs directly.
2. **What is the purpose of the comparison function in the Playground?**

*Solution:* To directly compare the effects of different prompts or models.
3. **How ​​can you test the creativity of the answers?**

*Solution:* By varying the “Temperature” parameter.
4. **What is a benefit of instant feedback?**

*Solution:* You can quickly customize prompts and learn what works.
5. **How ​​to test different output formats?**

*Solution:* By specifying the desired format in the prompt (e.g. JSON, table).
6. **Why is a playground useful for workshops?**

*Solution:* It promotes practical, experimental learning.
7. **How ​​can you compare models in Playground?**

*Solution:* By selecting different models and identical prompts.
8. **What is a typical error in prompt experimentation?**

*Solution:* Too many changes at once, no clear goal.
9. **How ​​can you test the effect of rollers?**

*Solution:* By specifying different roles in the prompt.
10. **How ​​to document the results?**

*Solution:* By copying and comparing the answers, if necessary screenshots or notes.

---

## Unit 6 — Temperature and Control of Creativity

### Comprehensive description & basics

LLMs offer various parameters that can be used to control response behavior. The most important are:

- **Temperature:** Controls how “creative” or “random” the answers are. Low values ​​(e.g. 0.0) result in very predictable, factual answers. Higher values ​​(e.g. 1.0 or more) make the answers more creative but also more unpredictable.
- **Max Tokens:** Limit the maximum length of the response.
- **Top-k / Top-p:** Control how many of the most likely next words are included in the selection (Top-k: fixed number, Top-p: cumulative probability).

**Why is this important?**

- For technical, precise tasks, a low temperature is usually chosen.
- A higher temperature makes sense for creative tasks (stories, brainstorming).
- With Max Tokens you can prevent the model from responding for too long.

### 5 Examples of Temperature & Creativity (with Python Code)

1. **Temperature 0.0 (deterministic):**

Prompt:

```prompt
    "Explain what a computer is."
    ```

```python
    # File: temp1_deterministic.py
    from lib.helper_ollama import ollama
    prompt = "Explain what a computer is."
    result = ollama.generate(prompt, temperature=0.0)
    print(result)
    ```

2. **Temperature 1.2 (creative):**

Prompt:

```prompt
    "Make up a story about a talking cat."
    ```

```python
    # File: temp2_kreativ.py
    from lib.helper_ollama import ollama
    prompt = "Make up a story about a talking cat."
    result = ollama.generate(prompt, temperature=1.2)
    print(result)
    ```

3. **Comparison of different temperatures:**

Prompt:

```prompt
    "Name three advantages of solar energy."
    ```

```python
    # File: temp3_vergleich.py
    from lib.helper_ollama import ollama
    prompt = "Name three advantages of solar energy."
    result_0 = ollama.generate(prompt, temperature=0.0)
    result_1 = ollama.generate(prompt, temperature=1.0)
    print("Temp 0.0:", result_0)
    print("Temp 1.0:", result_1)
    ```

4. **Limit Max Tokens:**

Prompt:

```prompt
    "Summarize the following text in 10 words: ..."
    ```

```python
    # File: temp4_maxtokens.py
    from lib.helper_ollama import ollama
    text = "Artificial intelligence is a branch of computer science ..."
    prompt = f"Summarize the following text into 10 words: {text}"
    result = ollama.generate(prompt, max_tokens=20)
    print(result)
    ```

5. **Top-k/Top-p Variation:**

Prompt:

```prompt
    "Write a joke about robots."
    ```

```python
    # File: temp5_topk_topp.py
    from lib.helper_ollama import ollama
    prompt = "Write a joke about robots."
    result_k1 = ollama.generate(prompt, top_k=1)
    result_k10 = ollama.generate(prompt, top_k=10)
    print("Top-k=1:", result_k1)
    print("Top-k=10:", result_k10)
    ```

### 10 questions and solutions about temperature and creativity

1. **What does the "Temperature" parameter do?**

*Solution:* It controls how creative or random the answer is.
2. **When should you choose a low temperature?**

*Solution:* For technical, precise tasks.
3. **What happens at high temperatures?**

*Solution:* The answers become more creative, but also more unpredictable.
4. **What is “Max Tokens” for?**

*Solution:* Limiting the maximum answer length.
5. **What is the difference between Top-k and Top-p?**

*Solution:* Top-k: fixed number of next words; Top-p: cumulative probability.
6. **How ​​to prevent the model from taking too long to respond?**

*Solution:* By setting Max Tokens.
7. **What is a disadvantage of too high a temperature?**

*Solution:* The answers may become chaotic or nonsensical.
8. **How ​​can you specifically test creativity?**

*Solution:* By varying the temperature and comparing the results.
9. **When does a high temperature make sense?**

*Solution:* For creative tasks such as stories, brainstorming.
10. **How ​​does top-k affect the answer?**

*Solution:* The higher top-k, the more possible words are considered, resulting in more diversity.

---

prompt = "Explain the difference between Python and Java."

## Unit 7 — Comparison of different models

### Comprehensive description & basics

There are many different LLMs, varying in architecture, training data, size and specialization. Well-known models are Llama2, Mistral and Codellama. Each model has its own strengths and weaknesses. Comparing different models helps to find the right model for a task and understand the differences in style, accuracy and creativity.

**Typical differences:**

- **Llama2:** Very good all-round language model, extensive and detailed answers.
- **Mistral:** Compact, fast, often shorter and more concise answers.
- **Codellama:** Specially trained for programming tasks, usually delivers better code.

**Why compare?**

- To choose the best model for a task
- To identify strengths and weaknesses
- To test the effect of parameters and prompts

### 5 Examples of Model Comparisons (with Python Code)

1. **Text summary:**

Prompt:

    ```prompt
    "Summarize the following text in 3 sentences: ..."
    ```

    ```python
    # File: models1_summary.py
    from lib.helper_ollama import ollama
    text = "Artificial intelligence is a branch of computer science ..."
    prompt = f"Summarize the following text into 3 sentences: {text}"
    result_llama2 = ollama.generate(prompt, model="llama2")
    result_mistral = ollama.generate(prompt, model="mistral")
    print("llama2:", result_llama2)
    print("mistral:", result_mistral)
    ```

2. **Code generation:**

    Prompt:

    ```prompt
    "Write a Python function for the Fibonacci numbers."
    ```

    ```python
    # File: models2_code.py
    from lib.helper_ollama import ollama
    prompt = "Write a Python function for the Fibonacci numbers."
    result_llama2 = ollama.generate(prompt, model="llama2")
    result_codellama = ollama.generate(prompt, model="codellama")
    print("llama2:", result_llama2)
    print("codellama:", result_codellama)
    ```

3. **Creative tasks:**

Prompt:

```prompt
    "Make up a story about a robot."
    ```

```python
    # File: modelle3_kreativ.py
    from lib.helper_ollama import ollama
    prompt = "Make up a story about a robot."
    result_llama2 = ollama.generate(prompt, model="llama2")
    result_mistral = ollama.generate(prompt, model="mistral")
    print("llama2:", result_llama2)
    print("mistral:", result_mistral)
    ```

4. **Test expertise:**

Prompt:

```prompt
    "Explain the difference between Python and Java."
    ```

```python
    # File: modelle4_fachwissen.py
    from lib.helper_ollama import ollama
    prompt = "Explain the difference between Python and Java."
    result_llama2 = ollama.generate(prompt, model="llama2")
    result_mistral = ollama.generate(prompt, model="mistral")
    print("llama2:", result_llama2)
    print("mistral:", result_mistral)
    ```

5. **Formatted Output:**

    Prompt:

    ```prompt
    "Output the answer as a table."
    ```

    ```python
    # File: models5_format.py
    from lib.helper_ollama import ollama
    prompt = "Output the answer as a table."
    result_llama2 = ollama.generate(prompt, model="llama2")
    result_mistral = ollama.generate(prompt, model="mistral")
    print("llama2:", result_llama2)
    print("mistral:", result_mistral)
    ```

### 10 questions and solutions to compare models

1. **Why should you compare different LLMs?**

*Solution:* To find the best model for a task and identify differences.
2. **Which model specializes in programming?**

*Solution:* Codellama.
3. **What is an advantage of Mistral?**

*Solution:* Compact, quick, concise answers.
4. **How ​​do Llama2 and Mistral differ when it comes to summaries?**

*Solution:* Llama2 is often more detailed, Mistral is shorter.
5. **Which model usually produces better Python code?**

*Solution:* Codellama.
6. **How ​​can you practically compare models?**

*Solution:* Send the same prompt to different models and compare answers.
7. **What is a disadvantage of all-round models?**

*Solution:* They are not optimized for special tasks.
8. **How ​​to test the creativity of different models?**

*Solution:* By creative prompts and comparing answers.
9. **What is a typical error when comparing models?**

*Solution:* Use different prompts or parameters.
10. **How ​​to test formatting skills?**

*Solution:* Through prompts with explicit format specifications (e.g. table, JSON).

---

## Unit 8 — Faults and Limitations of LLMs

### Comprehensive description & basics

LLMs are powerful, but they have clear limitations and make typical mistakes. They cannot look up real facts, but rather generate answers based on probabilities and patterns from the training data. The most important sources of error include:

- **Hallucinations:** The model invents plausible but false information.
- **Bias:** Prejudices and stereotypes from the training data are adopted.
- **Mathematical Errors:** LLMs are not calculating machines and often make errors in complex calculations.
- **Context Window:** The model can only remember a limited amount of text. Prompts that are too long will be cut off.
- **Outdated knowledge:** The model only knows information up to the status of its training date.

**Why is this important?**

- One should always check LLM answers critically.
- LLMs are only suitable to a limited extent for safety-critical or fact-based tasks.
- Prompt engineering can help reduce errors, but not completely eliminate them.

### 5 Examples of Errors & Limitations (with Python Code)

1. **Hallucination:**

    Prompt:

    ```prompt
    "What is the capital of France in Africa?"
    ```

    ```python
    # File: error1_hallucination.py
    from lib.helper_ollama import ollama
    prompt = "What is the capital of France in Africa?"
    result = ollama.generate(prompt)
    print(result)
    ```

2. **Bias:**

    Prompt:

    ```prompt
        "Describe a typical programmer."
        ```

    ```python
    # File: error2_bias.py
    from lib.helper_ollama import ollama
    prompt = "Describe a typical programmer."
    result = ollama.generate(prompt)
    print(result)
    ```

3. **Mathematical error:**

    Prompt:

    ```prompt
    "What is 12345x6789?"
    ```

    ```python
    # File: error3_mathe.py
    from lib.helper_ollama import ollama
    prompt = "What is 12345 x 6789?"
    result = ollama.generate(prompt)
    print(result)
    ```

4. **Context Limit:**

    Prompt:

    ```prompt
    Very long text, followed by a question at the beginning of the text.
    ```

    ```python
    # File: error4_context.py
    from lib.helper_ollama import ollama
    text = "This is a very long text..." * 1000
    prompt = f"{text}\nWhat is at the beginning of the text?"
    result = ollama.generate(prompt)
    print(result)
    ```

5. **Outdated Knowledge:**

    Prompt:

    ```prompt
    "Who is the current Chancellor of Germany?" (according to training time)
    ```

    ```python
    # File: error5_deprecated.py
    from lib.helper_ollama import ollama
    prompt = "Who is the current Chancellor of Germany?"
    result = ollama.generate(prompt)
    print(result)
    ```

### 10 questions and solutions about mistakes & limitations

1. **What is a hallucination in LLMs?**

*Solution:* The model invents plausible but false information.
2. **What is bias?**

*Solution:* Inherited biases or stereotypes from the training data.
3. **Why do LLMs make calculation errors?**

*Solution:* They are not specialized calculating machines.
4. **What is the context window?**

*Solution:* The maximum amount of text the model can process at one time.
5. **How ​​to recognize hallucinations?**

*Solution:* Through critical examination and counter-research.
6. **Why is outdated knowledge a problem?**

*Solution:* The model does not know about any events after the training time.
7. **How ​​can you reduce bias in prompting?**

*Solution:* Through neutral, balanced prompts and critical examination of the answers.
8. **What is a typical mistake with long prompts?**

*Solution:* The model forgets the beginning or important details.
9. **How ​​to avoid mathematical errors?**

*Solution:* Check results using a calculator or specialized software.
10. **Why should you always check LLM answers?**

*Solution:* Due to possible errors, hallucinations and bias.

---

## Unit 9 — Prompt Debugging & Optimization

### Comprehensive description & basics

Prompt debugging is the targeted analysis and improvement of prompts to increase the quality and consistency of LLM answers. Often LLMs provide unexpected, inaccurate or incorrect answers because the prompt is too vague, too complex or ambiguous. Prompt optimization means systematically revising, testing and refining prompts until the desired result is reliably achieved.

**Typical problems:**

- Unclear task
- Missing or imprecise format specifications
- Too little context
- Prompts that are too complex or convoluted
- Conflicting requirements

**Debugging Strategies:**

- Quickly simplify and build step by step
- Add examples (few shot)
- Specify output format explicitly
- Analyze incorrect answers and adjust them promptly
- Document and compare results

### 5 examples of prompt debugging & optimization

1. **Unclear task:**
    - Original prompt: "Explain."
    - Debugging: specify the task, e.g. B. "Explain the term 'neural network' for beginners."

2. **Missing format:**
    - Original prompt: "List benefits of solar energy."
    - Debugging: "Name three advantages of solar energy as a numbered list."

3. **Too little context:**
    - Original prompt: "Summarize."
    - Debugging: "Summarize the following text into 2 sentences: ..."

4. **Simplify complex prompt:**
    - Original prompt: "Explain AI, ML and Deep Learning and give examples."
    - Debugging: Split into multiple prompts or query step-by-step.

5. **Add examples:**
    - Original prompt: "Translate into French."
    - Debugging: "Translate into French:\nGerman: Hello → French: Bonjour\nGerman: Thank you → French: Merci\nGerman: I love AI → French:"

### 10 questions and solutions about prompt debugging & optimization

1. **What is Prompt Debugging?**

*Solution:* The targeted analysis and improvement of prompts.
2. **Why is prompt debugging important?**

*Solution:* To increase the quality and reliability of the answers.
3. **How ​​can you avoid unclear tasks?**

*Solution:* Through precise and clear formulations.
4. **What is a typical error in prompts?**

*Solution:* Missing format specifications or too little context.
5. **How ​​can you systematically improve prompts?**

*Solution:* Adjust, test and compare step by step.
6. **Why are examples helpful in the prompt?**

*Solution:* You show the model how the task should be solved.
7. **How ​​to avoid conflicting requirements?**

*Solution:* Provide clear, non-conflicting instructions.
8. **What is an advantage of output format specifications?**

*Solution:* The answers are more structured and easier to process further.
9. **How ​​to document the results?**

*Solution:* Save, compare and analyze answers.
10. **What is a disadvantage of overly complex prompts?**

*Solution:* The model may become overwhelmed or provide inaccurate answers.

---

## Unit 10 — Ethics & Safety in Prompting

### Comprehensive description & basics

When working with LLMs, it is essential to consider ethical and safety-related aspects. LLMs can inherit biases from training data, generate problematic or dangerous content, or be used for abuse. Prompting can help minimize risks by providing clear instructions and constraints and critically examining answers.

**Important Topics:**

- Handling sensitive or personal data
- Avoiding discriminatory, offensive or dangerous content
- Transparency and traceability of the answers
- Responsible and safe use of LLMs

**Safety Measures:**

- Design prompts so that no harmful or illegal instructions are executed
- Filters and moderation for generated content
- References to ethical boundaries and responsible use in the prompt

**Why is this important?**

- To prevent harm, discrimination and abuse
- To increase trust in AI systems
- To comply with legal and social requirements

### 5 Examples of Ethics and Safety in Prompting

1. **Avoid sensitive context:**

Prompt:

```prompt
    "Don't give out personal information."

2. **Prevent discrimination:**

Prompt:

```prompt
    “Be careful not to use prejudices or stereotypes.”

3. **Block Dangerous Instructions:**

Prompt:

```prompt
    "Do not give instructions on illegal or dangerous actions."

4. **Promote Transparency:**

Prompt:

```prompt
    "Explain how you came to your answer."

5. **Emphasize responsibility:**

Prompt:

```prompt
    "Please note that the answer is not a substitute for medical advice."

### 10 questions and solutions about ethics & safety in prompting

1. **Why are ethics important when working with LLMs?**

*Solution:* To prevent harm, discrimination and abuse.
2. **How ​​to protect sensitive data?**

*Solution:* Do not use or share personal information in the prompt.
3. **How ​​can you avoid discrimination in prompting?**

*Solution:* Through neutral, respectful formulations and explicit instructions.
4. **What is a dangerous instruction?**

*Solution:* Instructions on illegal, harmful or risky actions.
5. **How ​​to promote transparency?**

*Solution:* Ask the model to justify its answer.
6. **Why are filters and moderation important?**

*Solution:* To detect and block problematic content.
7. **What is an example of responsible prompting?**

*Solution:* Note that the answer is not a substitute for medical or legal advice.
8. **How ​​to prevent misuse of LLMs?**

*Solution:* Through technical and organizational measures, e.g. B. Access restrictions.
9. **What is a common mistake when it comes to ethics?**

*Solution:* Uncritical acceptance of the model answers without checking.
10. **How ​​can you increase the traceability of the answers?**

*Solution:* Ask the model to reveal its sources or reasoning.

---

## Unit 11 — Practical Examples of Prompts

### Comprehensive description & basics

This unit introduces various practical prompts that cover typical use cases of LLMs. The examples show how to design prompts for summaries, roles, corrections, code explanations and structured output. The aim is to demonstrate the diversity and flexibility of prompts and to provide inspiration for your own experiments.

**Why are practical examples important?**

- They help to understand the effect of formulations.
- They show how to customize prompts for different tasks.
- They promote creativity and understanding of the possibilities of LLMs.

### 5 Practical Prompt Examples (with Python Code)

1. **Summarize text:**

Prompt:

```prompt
    "Summarize the following text into 3 bullet points:\nText: ..."
    ```

```python
    # File: practical1_summarize.py
    from lib.helper_ollama import ollama
    text = "Artificial intelligence is a branch of computer science ..."
    prompt = f"Summarize the following text into 3 bullet points:\nText: {text}"
    result = ollama.generate(prompt)
    print(result)
    ```

2. **Act as a role:**

Prompt:

```prompt
    "You are a travel advisor. Recommend me 3 places in Italy."
    ```

```python
    # File: practical2_role.py
    from lib.helper_ollama import ollama
    prompt = "You are a travel advisor. Recommend me 3 places in Italy."
    result = ollama.generate(prompt)
    print(result)
    ```

3. **Proofreading:**

Prompt:

```prompt "Correct misspellings in the following text: 'This is an example'." ```

```python
    # File: practical3_correction.py
    from lib.helper_ollama import ollama
    prompt = "Correct spelling errors in the following text: 'This is an example'."
    result = ollama.generate(prompt)
    print(result)
    ```

4. **Explain code:**

Prompt:

```prompt
    "Explain this Python code step by step:\n\nfor i in range(5): print(i)"
    ```

```python
    # File: practically4_code_erklaeren.py
    from lib.helper_ollama import ollama
    prompt = "Explain this Python code step by step:\n\nfor i in range(5): print(i)"
    result = ollama.generate(prompt)
    print(result)
    ```

5. **Force JSON output:**

Prompt:

```prompt
    "Analyze the following sentence: 'AI is fascinating.' Answer in JSON format: {\"Language\": \"German\", \"Mood\": \"positive\"}"
    ```

```python
    # File: practical5_json.py
    from lib.helper_ollama import ollama
    prompt = "Analyze the following sentence: 'AI is fascinating.' Answer in JSON format: {\"Language\": \"German\", \"Mood\": \"positive\"}"
    result = ollama.generate(prompt)
    print(result)
    ```

### 10 questions and solutions to practical prompts

1. **How ​​to request a summary as bullet points?**

*Solution:* By specifying the desired format in the prompt (e.g. "summarize into 3 bullet points").
2. **How ​​do you get the model to take a role?**

*Solution:* Through a clear role description in the prompt (e.g. "You are a travel advisor...").
3. **How ​​can you use the model for proofreading?**

*Solution:* With a prompt like "Correct spelling mistakes in the following text: ...".
4. **How ​​to have code explained?**

*Solution:* By a prompt like "Explain this Python code step by step: ...".
5. **How ​​to force structured output (e.g. JSON)?**

*Solution:* By explicitly specifying the format in the prompt.
6. **What is a benefit of role prompts?**

*Solution:* The answer is appropriate for the target group and in the appropriate style.
7. **How ​​to test the creativity of the model?**

*Solution:* Through open, creative tasks.
8. **How ​​to control response length?**

*Solution:* By specifying the desired length or number of points.
9. **How ​​to get the model to a table?**

*Solution:* By the statement "Output the answer as a table".
10. **How ​​to combine multiple tasks into one prompt?**

*Solution:* By listing multiple requirements in the prompt (e.g. role, task, format).

---

## Unit 12 — Summary

After Day 2, students can:

- explain how LLMs work and what their limitations are,
- formulate prompts specifically and compare the answers,
- control the parameters (temperature, tokens),
- experiment with several models,
- build a prompt playground in Streamlit,
- understand what a prompt is and how it should be structured (role, context, task, format),
- use the different roles (system, user, assistant),
- apply the most important prompting principles: zero/few-shot, role, chain-of-thought, self-consistency, format prompting,
- Formulate prompts for specific tasks such as summary, roles, code explanation or JSON output.

---

## Unit 13 — 5 mini projects

### Mini Project 1: Universal Prompt Playground

**Task:** Build a Streamlit app that tests various prompt parameters.

**Solution:**

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

### Mini Project 2: Role-Player Chatbot

**Task:** Create a chatbot that can take on different roles.

**Solution:**

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

### Mini Project 3: Few-Shot Learning Demo

**Task:** Demonstrate Few-Shot Learning with examples of text classification.

**Solution:**

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

### Mini Project 4: Chain-of-Thought Problem Solver

**Task:** Use chain-of-thought for complex problem solving.

**Solution:**

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

### Mini Project 5: JSON Data Extractor

**Task:** Extract structured data from body text in JSON format.

**Solution:**

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
