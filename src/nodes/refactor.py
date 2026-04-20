# Node 6: Produces a clean, refactored version of the original code
# incorporating all findings from previous review nodes.

from src.graph.state import CodeReviewState
from src.utils.llm_client import get_llm


def refactor_node(state: CodeReviewState) -> CodeReviewState:
    """
    Generates a refactored version of the code that addresses:
    - All quality issues found in the quality review
    - All security vulnerabilities found in the security review
    - All performance suggestions from the optimization node

    The refactored code should be production-ready.

    Args:
        state: The current shared state (includes all previous reviews).

    Returns:
        Updated state with 'refactored_code' field populated.
    """
    llm = get_llm(temperature=0.2)

    prompt = f"""You are a senior {state['language']} engineer.
Rewrite the following code, fixing ALL issues identified in the reviews below.
The refactored code must:
- Be clean, readable, and well-documented
- Follow SOLID and Clean Code principles
- Fix all security vulnerabilities
- Apply all performance optimizations
- Preserve the original functionality completely

--- ORIGINAL CODE ---
{state['raw_code']}

--- QUALITY ISSUES TO FIX ---
{state.get('quality_review', 'N/A')}

--- SECURITY ISSUES TO FIX ---
{state.get('security_review', 'N/A')}

--- OPTIMIZATIONS TO APPLY ---
{state.get('optimization_suggestions', 'N/A')}

Return ONLY the refactored code (no explanation, no markdown fences).
"""

    response = llm.invoke(prompt)
    print("[Node 6] Refactoring complete.")

    return {**state, "refactored_code": response.content.strip()}