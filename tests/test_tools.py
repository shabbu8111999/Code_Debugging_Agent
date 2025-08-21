import pytest
from agent.tools import analyze_syntax, safe_exec

def test_analyze_syntax_good():
    code = "print('hello')"
    assert "✅" in analyze_syntax(code)

def test_analyze_syntax_bad():
    code = "def x("
    assert "❌" in analyze_syntax(code)

def test_safe_exec():
    code = "a=5\nb=3\nc=a+b"
    out, err = safe_exec(code)
    assert "c" in out
    assert not err
