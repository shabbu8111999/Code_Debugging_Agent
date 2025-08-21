import ast
import traceback
from types import SimpleNamespace
from utils.logger import get_logger

logger = get_logger()

def analyze_syntax(code: str) -> str:
    try:
        ast.parse(code)
        return "✅ Syntax looks correct."
    except SyntaxError as e:
        logger.error(f"Syntax error: {e}")
        return f"❌ Syntax Error: {e}"

def safe_exec(code: str) -> tuple[str, str]:
    """
    Executes code and returns (locals_repr, traceback_str).
    WARNING: This runs arbitrary code. For production, sandbox with Docker/RestrictedPython.
    """
    local_vars = {}
    try:
        exec(code, {}, local_vars)
        # Avoid dumping large objects; show keys only
        keys = ", ".join(sorted(local_vars.keys()))
        return f"(locals) {keys}", ""
    except Exception:
        tb = traceback.format_exc()
        logger.error(f"Execution error: {tb}")
        return "", tb
