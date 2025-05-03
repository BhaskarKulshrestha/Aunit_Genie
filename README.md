# 🧠 GenAI ABAP AUnit Test Generator

**Generate AUnit test cases for ABAP reports using Generative AI (powered by Ollama/LLM). Just paste or upload ABAP code, and let the magic happen.**

---

## 🚀 Features

- 🔍 Paste ABAP report code or upload `.abap`/`.txt` file
- ⚙️ Automatically extracts logic and creates a prompt
- 🤖 Uses a local Ollama LLM (LLaMA3 or compatible) to generate AUnit test cases
- 📜 Displays formatted ABAP AUnit code
- 💾 Download test cases as `.abap` file
- 📊 Shows progress bar with randomly generated funny quote during processing

---

## 📁 Project Structure

```plaintext
genai-abap-tester/
│
├── app.py                 # Streamlit UI App
├── ai_generator.py        # Prompt creation & AI interaction with Ollama
├── abap_parser.py         # Extracts business logic from ABAP code
├── utils.py               # Random quote generator
├── requirements.txt       # Python dependencies
└── README.md              # You're here!
```


--------------------------------------------
