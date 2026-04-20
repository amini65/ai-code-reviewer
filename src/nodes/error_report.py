# Error Branch Node: Only reached when syntax errors are detected.
# Produces a targeted error report and terminates the pipeline.

from src.graph.state import CodeReviewState
from src.utils.llm_client import get_llm


def error_report_node(state: CodeReviewState) -> CodeReviewState:
    """
    Generates a clear, beginner-friendly report of the syntax errors.
    This node is the terminal node for the error branch.

    Args:
        state: The current shared state (must contain 'syntax_error_details').

    Returns:
        Updated state with 'error_report' field populated.
    """
    llm = get_llm(temperature=0.3)

    prompt = f"""A {state['language']} code snippet has syntax errors.
Write a clear, friendly Markdown report explaining:
1. What errors were found
2. Why each error is a problem
3. How to fix each error (with corrected code examples)

Detected errors:
{state['syntax_error_details']}

Original code:
{state['raw_code']}
"""

    response = llm.invoke(prompt)
    report = response.content.strip()

    print("[Error Node] Error report generated.")

    return {**state, "error_report": report}