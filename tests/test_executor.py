from agent.executor import CodeExecutor

def test_executor_run():
    code = "x=1+2"
    executor = CodeExecutor()
    result = executor.run(code)
    assert "✅" in result["syntax"]
