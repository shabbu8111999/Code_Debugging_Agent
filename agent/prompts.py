from langchain.prompts import PromptTemplate


DEBUG_PROMPT = PromptTemplate(
    input_variables=["code", "error"],
    template = """
    You are a Python Debugging Assisstant.
    The User provided this Code:

    ```python
    {code}
    ```

    {error}

    Task:

    1.Explain the likely cause of the bug in clear terms.
    2.Suggest a corrected version of the code.
    3.Provide any extra tips if necessary.
    """
)

FIX_PROMPT = PromptTemplate(
input_variables=["code", "error", "syntax_feedback"],
template="""You are a precise Python code fixer.

Code:
```python
{code}
```

Error:
{error}

Syntax Feedback:
{syntax_feedback}

Please provide the fixed code.
"""
)