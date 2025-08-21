from agent.agents import DebuggingAgent
from utils.logger import get_logger

logger = get_logger()

def run():
    logger.info("🚀 Starting Code Debugging Agent...")

    # Example buggy code (normally you’d get from user input / UI)
    buggy_code = """
def add_numbers(a, b)
    return a + b
"""

    agent = DebuggingAgent()
    result = agent.run_debug(buggy_code)
    print("\n--- Debugging Result ---\n")
    print(result)


if __name__ == "__main__":
    run()
