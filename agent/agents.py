from agent.executor import CodeExecutor
from agent.chains import DebugChain
from utils.logger import get_logger

logger = get_logger()

class DebuggingAgent:
    def __init__(self):
        self.executor = CodeExecutor()
        self.chain = DebugChain()

    def run_debug(self, code: str) -> str:
        logger.info("Running executor...")
        exec_result = self.executor.run(code)
        logger.info("Passing results to LLM chain...")
        return self.chain.analyze(code, exec_result.get("error", ""))

    def run_fix(self, code: str) -> str:
        exec_result = self.executor.run(code)
        fixed = self.chain.fix(
            code=code,
            error=exec_result.get("error", ""),
            syntax_feedback=exec_result.get("syntax", "")
        )
        return fixed
