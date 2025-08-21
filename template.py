import os
import logging
from pathlib import Path

logging.basicConfig(level = logging.INFO, format = ('[%(asctime)s]: %(message)s:'))


list_of_files = [
    "agent/__init__.py",
    "agent/chains.py",
    "agent/tools.py",
    "agent/prompts.py",
    "agent/executor.py",
    "agent/agents.py",
    "utils/__init__.py",
    "utils/logger.py",
    "utils/formatter.py",
    "tests/__init_.py",
    "tests/test_tools.py",
    "tests/test_executor.py",
    "tests/test_agent.py",
    "examples/bug1.py",
    "examples/bug2.py",
    "examples/bug3.py",
    "requirements.txt",
    "setup.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created Directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (not os.path.getsize(filepath) == 0):
        with open (filepath, "w") as f:
            pass
        logging.info(f"Created empty file {filepath}")
    else:
        logging.info(f"{filepath} already exists")
