from agent.tools import analyze_syntax, safe_exec

class CodeExecutor:
    def __init__(self):
        pass

    def run(self, code: str) -> dict:
        syntax_feedback = analyze_syntax(code)

        # If syntax is bad, don't run
        if syntax_feedback.strip().startswith("❌"):
            return {
                "syntax": syntax_feedback,
                "output": "",
                "error": ""  # no runtime attempt if syntax fails
            }

        output, error = safe_exec(code)
        return {
            "syntax": syntax_feedback or "",
            "output": output or "",
            "error": error or "",
        }
