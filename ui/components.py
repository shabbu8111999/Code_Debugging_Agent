from typing import Iterable
import difflib

def unified_diff(a: str, b: str, a_name="original.py", b_name="fixed.py") -> str:
    return "\n".join(
        difflib.unified_diff(
            a.splitlines(), b.splitlines(),
            fromfile=a_name, tofile=b_name, lineterm=""
        )
    )

def has_changes(a: str, b: str) -> bool:
    return a.strip() != b.strip()
