import re
from langchain_openai import ChatOpenAI
from agent.prompts import DEBUG_PROMPT, FIX_PROMPT

class DebugChain:
    def __init__(self, model="gpt-4o-mini", temperature=0):
        self.llm = ChatOpenAI(model=model, temperature=temperature)

    def analyze(self, code: str, error: str) -> str:
        prompt = DEBUG_PROMPT.format(code=code, error=error or "(no error)")
        resp = self.llm.invoke(prompt)
        return resp.content

    def fix(self, code: str, error: str, syntax_feedback: str) -> str:
        prompt = FIX_PROMPT.format(code=code, error=error or "", syntax_feedback=syntax_feedback or "")
        resp = self.llm.invoke(prompt)
        return resp.content