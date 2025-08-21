from agent.agents import DebuggingAgent

def test_agent_debug(monkeypatch):
    agent = DebuggingAgent()

    def fake_analyze(code, error):
        return "Fake debug response"

    agent.chain.analyze = fake_analyze

    result = agent.run_debug("print('hi')")
    assert "Fake debug response" in result
