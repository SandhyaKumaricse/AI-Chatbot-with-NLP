#  Task 3 - AI Chatbot with Natural Language Processing

## 📄 Description

This task involved creating a basic **AI chatbot** that uses **Natural Language Processing (NLP)** to understand and respond to user queries. The goal was to build a rule-based conversational agent using Python and NLP libraries like **NLTK** or **spaCy**, without incorporating any external AI models or advanced machine learning.

The chatbot was developed to recognize specific user inputs, preprocess the text using tokenization and lemmatization, and return predefined responses. The focus was on simplicity, language understanding, and interaction handling — strictly based on the original internship instructions.

## 🧰 Tools & Technologies Used

* **Programming Language:** Python 3.12
* **Libraries Used:**

  * `nltk` – for tokenization and lemmatization
* **Editor:** Visual Studio Code (VS Code)
* **Environment:** Windows 10 Terminal

## 🏗️ Implementation Summary

1. Installed necessary NLTK components like `punkt` and `wordnet`.
2. Defined a small rule-based knowledge base containing user queries and expected responses.
3. Preprocessed user input using:

   * Lowercasing
   * Punctuation removal
   * Tokenization and lemmatization
4. Matched processed user input against known keywords or phrases.
5. Displayed appropriate responses directly in the terminal.

This chatbot is terminal-based, lightweight, and entirely rule-driven, making it easy to understand and customize for specific domains.

## 🌍 Real-World Applications

* **Customer Service Bots:** For answering FAQs with defined answers.
* **Educational Assistants:** To support students with predefined topic guidance.
* **Retail & E-commerce:** To guide users through shopping processes using scripted flows.
* **Basic Interfaces:** Ideal for command-line apps or embedded chat tools with known commands.

## ✅ Deliverables

* Python script: `task_3.py`
* Works entirely in the terminal with no external files required

---

This task helped solidify core NLP concepts like lemmatization and tokenization and demonstrated how even basic techniques can create useful conversational agents. It's a foundational stepping stone toward more complex chatbot systems.
