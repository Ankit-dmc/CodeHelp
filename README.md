# 🚀 CodeHelp

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/flask-3.x-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](#12-license)

CodeHelp is an AI-powered coding mentor and assistant designed to bridge the gap between writing code and understanding it. Built with Generative AI principles at its core, CodeHelp analyzes source code to provide beginner-friendly explanations, identify potential bugs, suggest performance optimizations, and highlight programming concepts.

---

## 1. Introduction

Learning to code is exciting, but it can also be overwhelming when you run into errors or complex syntax. **CodeHelp** is built to feel like an approachable coding mentor sitting next to you. It helps you:

* **Understand Code:** Break down code logic line by line into simple terms.
* **Find & Fix Bugs:** Pinpoint edge cases and coding bugs with clear advice on how to resolve them.
* **Learn Core Concepts:** Identify the fundamental programming concepts used in your code (e.g., loops, recursion, lists).
* **Demystify Complexity:** Explain time and space complexity ($O(N)$ notations) without the intimidating jargon.

---

## 2. Problem Statement

Many beginner programmers use general-purpose AI tools to write code. While these tools are powerful, they often:
* **Overcomplicate Answers:** Return complex code snippets containing advanced concepts that a beginner hasn't learned yet.
* **Encourage Copy-Pasting:** Give quick solutions without teaching *how* the code works, leading to gaps in knowledge.
* **Neglect Step-by-Step Debugging:** Point out syntax errors without explaining *why* they happened or how to prevent them.

**CodeHelp** acts as a teacher rather than just a code generator, focusing on comprehension, step-by-step guidance, and teaching good practices.

---

## 3. Features

* 📖 **Intelligent Code Explanations:** Receive structured summaries of what the code does in plain language.
* 🐛 **Bug & Edge Case Detection:** Identify logical errors, potential runtime bugs, and boundary conditions.
* ⚡ **Optimization Suggestions:** Learn how to make code run faster or use less memory.
* 💾 **Complexity Metrics:** See estimated Time and Space complexities accompanied by intuitive explanations.
* 🎯 **Difficulty Rating:** Get an assessment of whether the analyzed code is Easy, Medium, or Hard.
* 📚 **Concept Highlighting:** View a curated list of fundamental programming topics used in the script.
* 🌍 **Multi-Language Support:** Works with Python, C, C++, Java, JavaScript, and more.

---

## 4. Why Use CodeHelp Instead of Regular AI?

| Regular AI | CodeHelp |
| :--- | :--- |
| Designed for general tasks (writing essays, translating languages, writing bulk code). | Specifically designed for programmers, students, and educators. |
| Often delivers overly broad, highly advanced, or complex answers. | Keeps explanations simple, clean, and beginner-focused. |
| Hands you the solution directly, promoting a copy-paste habit. | Focuses on teaching and helping you build a deeper understanding. |
| Rarely explains the underlying concept or complexity reasoning. | Explains the step-by-step logic, concepts, and time/space complexity. |

---

## 5. Built on Generative AI Principles

CodeHelp leverages modern Generative AI concepts to parse and interpret code like a human instructor:

* **Large Language Models (LLMs):** Uses advanced models (such as `llama-3.3-70b-versatile`) to evaluate structure, syntax, and intent.
* **Prompt Engineering:** Employs precise system formatting instructions to enforce structured JSON output, ensuring consistent rendering of analysis results.
* **Context-Aware Responses:** Tailors responses strictly to a student persona, translating complex algorithms into readable analogies.
* **Natural Language Understanding (NLU):** Bridges the gap between raw computer code and readable human language.

---

## 6. Tech Stack

* **Backend:** [Python](https://www.python.org/) with [Flask](https://flask.palletsprojects.com/) (Web Server)
* **API Integration:** [Groq SDK](https://console.groq.com/) (Fast inference interface)
* **Frontend:** Semantic [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML), [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) (with Dark Mode styling), and [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) (handles loading/disabled states on form submission)

---

## 7. Installation Guide

### Prerequisites
* Python 3.8 or higher installed.
* A free Groq API key. Get one from the [Groq Console](https://console.groq.com/keys).

### Step-by-Step Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ankit-dmc/CodeHelp.git
   cd CodeHelp
   ```

2. **Create a virtual environment:**
   * **macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API Key:**
   Create a `.env` file in the root directory (or set it in your system environment variables):
   * **Linux/macOS:**
     ```bash
     export GROQ_API_KEY="your_groq_api_key_here"
     ```
   * **Windows (Command Prompt):**
     ```cmd
     set GROQ_API_KEY="your_groq_api_key_here"
     ```
   * **Windows (PowerShell):**
     ```powershell
     $env:GROQ_API_KEY="your_groq_api_key_here"
     ```

5. **Run the application:**
   ```bash
   python app.py
   ```
   *Alternatively:*
   ```bash
   flask run
   ```

6. **Open your browser:**
   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to start using CodeHelp!

---

## 8. Project Structure

Here is a breakdown of the repository:

```text
CodeHelp/
│
├── app.py              # Main Flask server containing routes and Groq API logic
├── requirements.txt    # Lists Python package dependencies (Flask, Groq)
│
├── static/
│   └── style.css       # Layout styles and modern dark-mode user interface
│
├── templates/
│   └── index.html      # Form interface and dashboard showing AI response structures
│
└── README.md           # Documentation for the project
```

---

## 9. How Other Developers Can Use & Contribute

We welcome contributions from developers, educators, and students!

1. **Fork** this repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/CodeHelp.git
   ```
3. Set up your virtual environment, install dependencies, and configure the API key as shown in the [Installation Guide](#7-installation-guide).
4. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/amazing-feature
   ```
5. Commit your changes and push them to your fork:
   ```bash
   git push origin feature/amazing-feature
   ```
6. Submit a **Pull Request** explaining your changes!

---

## 10. Acknowledgements

> I built the application's functionality, backend logic, and AI integration myself. Frontend design is not my strongest area, and my original HTML and CSS looked quite boring. To improve the user interface and make the application more presentable, I took some inspiration and assistance from Claude for parts of the HTML and CSS.

---

## 11. Future Improvements

Here is what is planned for future versions of CodeHelp:
- [ ] **Expanded Language Customization:** Adjust explanations depending on targeted skill levels (absolute beginner, intermediate, advanced).
- [ ] **Interactive Playground/Sandbox:** Add runtime execution support to run code securely and see output directly in the browser.
- [ ] **Visual Debugger:** Generate diagrammatic workflows showing how variable values change step-by-step.
- [ ] **Account Auth & History:** Allow users to save their analysis logs and reference previous explanations.
- [ ] **File Upload Support:** Upload entire code scripts (`.py`, `.cpp`, `.java`) instead of copy-pasting code blocks.

---

## 12. License

Distributed under the MIT License. See `LICENSE` for more information.
