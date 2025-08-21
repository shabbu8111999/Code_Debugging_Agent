import os
import difflib
import streamlit as st
from dotenv import load_dotenv

from agent.agents import DebuggingAgent
from utils.formatter import humanize_traceback, extract_first_code_block

load_dotenv()

st.set_page_config(page_title="Python Code Debugging Agent", layout="wide")
st.title(" Python Code Debugging Agent")

# Ensure API key present (show hint, don't print the key)
if not os.getenv("OPENAI_API_KEY"):
    st.warning("OPENAI_API_KEY not found. Set it in a .env file or environment variable before running.")
    st.stop()

# Session state
if "history" not in st.session_state:
    st.session_state.history = []

DEFAULT_SNIPPET = """\
def add_numbers(a, b)
    return a + b
"""

with st.sidebar:
    st.header("Options")
    explain_simple = st.checkbox("Explain errors simply", value=True)
    show_diff = st.checkbox("Show before/after diff", value=True)
    keep_history = st.checkbox("Keep history in session", value=True)
    st.markdown("---")
    st.caption("Tip: Use small, focused snippets for best results.")

code = st.text_area("Paste your Python code:", value=DEFAULT_SNIPPET, height=220)

col_run, col_fix, col_clear = st.columns([1,1,1])

agent = DebuggingAgent()

def run_analysis(input_code: str):
    # Use executor directly to show syntax/output/error immediately
    exec_result = agent.executor.run(input_code)
    syntax_feedback = exec_result.get("syntax", "")
    raw_error = exec_result.get("error", "")
    output = exec_result.get("output", "")

    # Simplify traceback (optional)
    if explain_simple and raw_error:
        simplified_error = humanize_traceback(raw_error)
    else:
        simplified_error = raw_error

    # Ask LLM for analysis
    analysis = agent.chain.analyze(input_code, raw_error or "")

    return {
        "syntax": syntax_feedback,
        "output": output,
        "error": raw_error,
        "error_simple": simplified_error,
        "analysis": analysis
    }

def auto_fix(input_code: str, last_error: str, syntax_feedback: str):
    fixed_text = agent.chain.fix(input_code, last_error or "", syntax_feedback or "")
    fixed_code = extract_first_code_block(fixed_text) or fixed_text.strip()
    return fixed_code

with col_run:
    run_clicked = st.button("🔍 Analyze")

with col_fix:
    fix_clicked = st.button("⚡ Auto-Fix")

with col_clear:
    if st.button("🧹 Clear"):
        st.session_state.history = []
        st.experimental_rerun()

if run_clicked or fix_clicked:
    if not code.strip():
        st.warning("Please paste some Python code.")
        st.stop()

    with st.spinner("Analyzing…"):
        result = run_analysis(code)

    st.subheader("Analysis")
    st.markdown("**Syntax Check:**")
    st.code(result["syntax"])

    if result["output"]:
        st.markdown("**Execution Output:**")
        st.code(result["output"])

    if result["error"]:
        st.markdown("**Execution Error (raw):**")
        st.code(result["error"])

    if result["error"] and explain_simple:
        st.markdown("**Execution Error (explained):**")
        st.write(result["error_simple"])

    st.subheader("Debugging Suggestions")
    st.write(result["analysis"])

    fixed_code = None
    if fix_clicked:
        with st.spinner("Proposing a fix…"):
            fixed_code = auto_fix(code, result["error"], result["syntax"])
        st.subheader("Proposed Fixed Code")
        st.code(fixed_code, language="python")

        if show_diff:
            st.subheader("Diff (Original → Fixed)")
            diff = difflib.unified_diff(
                code.splitlines(), (fixed_code or "").splitlines(),
                fromfile="original.py", tofile="fixed.py", lineterm=""
            )
            st.code("\n".join(diff) or "(no differences)")

        st.download_button(
            label="⬇️ Download fixed.py",
            data=fixed_code,
            file_name="fixed.py",
            mime="text/x-python",
            disabled=not bool(fixed_code and fixed_code.strip())
        )

    # History
    if keep_history:
        st.session_state.history.append({
            "code": code,
            "syntax": result["syntax"],
            "error": result["error_simple"] if explain_simple else result["error"],
            "analysis": result["analysis"],
            "fixed": fixed_code
        })

if st.session_state.history:
    st.markdown("---")
    st.subheader("History (this session)")
    for idx, item in enumerate(reversed(st.session_state.history[-5:]), start=1):
        with st.expander(f"Attempt {len(st.session_state.history) - idx + 1}"):
            st.markdown("**Original Code:**")
            st.code(item["code"], language="python")
            st.markdown("**Syntax:**")
            st.code(item["syntax"])
            if item["error"]:
                st.markdown("**Error:**")
                st.code(item["error"])
            st.markdown("**LLM Suggestions:**")
            st.write(item["analysis"])
            if item["fixed"]:
                st.markdown("**Fixed Code:**")
                st.code(item["fixed"], language="python")
