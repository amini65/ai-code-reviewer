# Node 5: Suggests performance and efficiency improvements.

from src.graph.state import CodeReviewState
from src.utils.llm_client import get_llm


def optimization_node(state: CodeReviewState) -> CodeReviewState:
    """
    Identifies opportunities to improve code performance, efficiency,
    and resource usage.

    Looks for:
    - Inefficient algorithms (e.g., O(n²) where O(n) is possible)
    - Unnecessary loops or repeated computations
    - Memory leaks or excessive memory use
    - Language-specific optimizations (e.g., list comprehensions in Python)
    - Better standard library usage

    Args:
        state: The current shared state.

    Returns:
        Updated state with 'optimization_suggestions' field populated.
    """
    llm = get_llm(temperature=0.3)

    prompt = f"""You are a performance optimization expert for {state['language']}.
Analyze this code and suggest concrete improvements for:
- Time complexity (Big-O)
- Space complexity
- Language-specific idioms and best practices
- Use of built-in functions vs manual implementations
- I/O efficiency

For each suggestion, show a BEFORE and AFTER code example.
Use Markdown formatting.

Code:
{state['raw_code']}
"""

    response = llm.invoke(prompt)
    print("[Node 5] Optimization suggestions complete.")

    return {**state, "optimization_suggestions": response.content.strip()}