# Node 2: Checks for syntax errors in the code.
# This node determines whether the graph continues normally or
# routes to the Error Report node (the branching decision point).

from src.graph.state import CodeReviewState
from src.utils.llm_client import get_llm


def syntax_check_node(state: CodeReviewState) -> CodeReviewState:
    """
    Analyzes the code for syntax errors.
    Sets 'has_syntax_error' (bool) and optionally 'syntax_error_details'.

    Args:
        state: The current shared state.

    Returns:
        Updated state with syntax check results.
    """
    llm = get_llm(temperature=0.0)

    prompt = f"""You are a {state['language']} compiler/interpreter.
Check the following code for syntax errors only.

If there are NO syntax errors, respond with exactly: NO_ERROR

If there ARE syntax errors, respond with exactly this format:
HAS_ERROR
<brief description of each error and the line it occurs on>

Code:
{state['raw_code']}
"""

    response = llm.invoke(prompt)
    content = response.content.strip()

    # Parse the structured response
    if content.startswith("NO_ERROR"):
        has_error = False
        error_details = None
        print("[Node 2] Syntax check passed: no errors found.")
    else:
        has_error = True
        # Everything after the first line is the error description
        error_details = content.replace("HAS_ERROR", "").strip()
        print(f"[Node 2] Syntax error found: {error_details[:80]}...")

    return {
        **state,
        "has_syntax_error": has_error,
        "syntax_error_details": error_details,
    }