import re
from typing import Optional

def format_result(result: str) -> str:
    border = "=" * 40
    return f"{border}\n{result}\n{border}"

def humanize_traceback(tb: str) -> str:
    """
    Turn a Python traceback into a terse, friendly explanation.
    Very basic heuristics; extend as needed.
    """
    if not tb:
        return ""
    if "SyntaxError" in tb:
        # Extract the message after 'SyntaxError:'
        m = re.search(r"SyntaxError:\s*(.*)", tb)
        return f"Syntax error: {m.group(1)}" if m else "Syntax error in your code."
    if "NameError" in tb:
        m = re.search(r"NameError:\s*name '([^']+)' is not defined", tb)
        if m:
            return f"Undefined name: `{m.group(1)}`. Did you forget to define or import it?"
        return "You used a name that isn't defined."
    if "TypeError" in tb:
        return "Type error: an operation received a value of the wrong type."
    if "ZeroDivisionError" in tb:
        return "Division by zero: check your denominator."
    # Fallback: first non-empty line after last 'Traceback' block
    lines = [ln for ln in tb.splitlines() if ln.strip()]
    last = lines[-1] if lines else tb
    return f"Runtime error: {last}"

def extract_first_code_block(text: str) -> Optional[str]:
    """
    Extract first fenced code block. Supports ```python ...``` or ``` ...```.
    """
    if not text:
        return None
    m = re.search(r"```(?:python)?\s*([\s\S]*?)```", text, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return None
