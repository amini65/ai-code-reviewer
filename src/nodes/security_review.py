# Node 4: Analyzes the code for common security vulnerabilities.

from src.graph.state import CodeReviewState
from src.utils.llm_client import get_llm


def security_review_node(state: CodeReviewState) -> CodeReviewState:
    """
    Scans the code for security vulnerabilities such as:
    - SQL injection
    - Hardcoded credentials or secrets
    - Unsafe use of eval() or exec()
    - Insecure deserialization
    - Missing input validation
    - OWASP Top 10 issues

    Args:
        state: The current shared state.

    Returns:
        Updated state with 'security_review' field populated.
    """
    llm = get_llm(temperature=0.1)  # Very low temp for accurate security analysis

    prompt = f"""You are a security engineer performing a code audit on {state['language']} code.
Identify ALL security vulnerabilities, risks, and bad practices.

For each issue found, provide:
- Issue name
- Severity: CRITICAL / HIGH / MEDIUM / LOW
- Affected line(s) or section
- Why it's dangerous
- Recommended fix

If no issues are found, state "No security issues detected."

Use Markdown formatting.

Code:
{state['raw_code']}
"""

    response = llm.invoke(prompt)
    print("[Node 4] Security review complete.")

    return {**state, "security_review": response.content.strip()}