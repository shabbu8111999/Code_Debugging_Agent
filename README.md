# 🐞 Code Debugging Agent

### A Python AI-powered debugging assistant that detects bugs, explains errors in simple terms, and suggests fixed code automatically. Built with LangChain, OpenAI, and optionally deployable via Streamlit for an interactive interface.



## 🚀 Features

Detects syntax and runtime errors in Python code.

Provides LLM-powered debugging suggestions.

Suggests auto-fix for buggy code.

Explains errors in plain English for beginners.

Streamlit UI for easy interaction:

Code editor

Execution output panel

LLM debugging suggestions

Auto-fix button

Before/After diff

History of previous attempts

Download fixed code

Optional test runner integration (future feature).

History and diff view for better understanding of changes.

Safe execution with skip-on-syntax-error logic.



## 🏗 Folder Structure

Code_Debugging_Agent/
│── agent/                  # Core agent logic
│   ├── __init__.py
│   ├── agents.py           # Main agent class
│   ├── chains.py           # LLM chains for analysis & fixing
│   ├── executor.py         # Code executor (syntax/runtime)
│   ├── prompts.py          # DEBUG_PROMPT & FIX_PROMPT
│   ├── tools.py            # Safe execution & syntax analysis
│
│── utils/                  # Helper utilities
│   ├── __init__.py
│   ├── logger.py           # Custom logger setup
│   ├── formatter.py        # Traceback & code extraction helpers
│
│── tests/                  # Unit tests
│   ├── __init__.py
│   ├── test_agent.py
│   ├── test_executor.py
│   ├── test_tools.py
│
│── examples/               # Example buggy code
│   ├── bug1.py
│   ├── bug2.py
│   ├── bug3.py
│
│── ui/                     # Streamlit interface
│   ├── app.py              # Streamlit main app
│   ├── components.py       # Optional UI helpers
│   ├── styles.css          # Optional CSS styling
│
│── requirements.txt        # All required Python packages
│── setup.py                # Optional packaging
│── main.py                 # CLI / main runner
│── .env                    # Store OpenAI API key securely



## 💻 Installation

### Note: This project uses uv for environment management instead of pip.

-> Clone the repository

```bash
git clone https://github.com/yourusername/Code_Debugging_Agent.git
cd Code_Debugging_Agent
```

-> Create a virtual environment (using uv)

```bash
uv --init
```

-- This will create a local virtual environment.


-> Install dependencies

```bash
uv pip install -r requirements.txt
```

## 🔑 Setup API Key

Create a .env file at the root of your project:

OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX

Do not include quotes. Restart terminal if environment variable was set using setx.


## 🏃‍♂️ Usage
1️⃣ Run in CLI version or Terminal :
```bash
python main.py
```
This runs the command-line debugger where you can paste Python code and see analysis/output.


2️⃣ Run Streamlit UI :
```bash
streamlit run ui/app.py
```


### After this you can:

Paste buggy code
Run analysis
See execution output & errors
Get LLM suggestions
Auto-fix code
View diff and download the fixed file



## 📂 File Descriptions

### agent/

File	        Description
agents.py	    Main DebuggingAgent class, orchestrates executor + LLM chains
chains.py	    DebugChain handles analysis and fix prompts with LLM
executor.py	    Runs Python code safely and returns output/errors
prompts.py	    DEBUG_PROMPT & FIX_PROMPT templates for LLM
tools.py	    Syntax checker and safe executor with logging


### utils/

File	        Description
logger.py	    Logger setup for info/error messages
formatter.py	Helpers to format tracebacks, extract code blocks, and explain errors


### tests/

Contains unit tests for agent, executor, and tools.


### examples/

Contains small buggy code examples for testing/debugging.


### ui/

File	            Description
app.py	            Streamlit interface
components.py	    UI helpers like diff generator
styles.css	        Optional styling for Streamlit interface



## 📦 Requirements

Example requirements.txt:


### Core LLM framework
langchain
langchain-core
langchain-community


### Python execution & sandboxing
asttokens
execnet
restrictedpython


### LLM Provider
openai
anthropic
transformers


### Utilities
rich
python-dotenv
pydantic
tenacity
loguru
click


### Testing & Dev
pytest
pytest-cov
ruff
mypy
black


### UI Tools
flask
flask-cors
streamlit

## NOTE: Completely depend's on you which UI Tools should you want to use


Install with: 
```bash
 uv pip install -r requirements.txt
```


## 🧩 How It Works

Executor runs Python code safely and collects:

Syntax errors

Runtime errors

Output variables

DebugChain sends code + error to LLM using DEBUG_PROMPT.

LLM returns explanation and suggested fix.

Auto-fix feature uses FIX_PROMPT to return corrected Python code.

Streamlit UI:

Displays results in an interactive format.

Allows downloading fixed code.

Shows before/after diff.

Keeps session history.



### ⚡ Future Improvements

Unit test runner in UI

Multi-pass auto-fix (iterate until clean)

Static analysis integration (flake8/ruff)

Docker sandbox execution for full safety

Voice or multi-LLM suggestions


### 📚 References

LangChain Documentation : https://docs.langchain.com/

OpenAI API : https://platform.openai.com/docs/api-reference/introduction

Streamlit Documentation : https://docs.streamlit.io/



## 👨‍💻 Author

### Shabareesh Nair – AI Engineer | Python Enthusiast