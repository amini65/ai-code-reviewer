# Node 3: Reviews code quality, SOLID principles, and Clean Code practices.

from src.graph.state import CodeReviewState
from src.utils.llm_client import get_llm


def quality_review_node(state: CodeReviewState) -> CodeReviewState:
    """
    Evaluates the code against Clean Code and SOLID principles.

    SOLID:
      S - Single Responsibility Principle
      O - Open/Closed Principle
      L - Liskov Substitution Principle
      I - Interface Segregation Principle
      D - Dependency Inversion Principle

    Args:
        state: The current shared state.

    Returns:
        Updated state with 'quality_review' field populated.
    """
    llm = get_llm(temperature=0.2)

    prompt = f"""You are a senior {state['language']} engineer reviewing code quality.
Analyze the following code for:
- Naming conventions (clear, descriptive variable/function names)
- Function length and single responsibility
- Code duplication (DRY principle)
- Readability and maintainability
- SOLID principles violations (if applicable)
- Missing or inadequate comments/docstrings

Format your response as Markdown with a severity rating
(🔴 Critical / 🟡 Warning / 🟢 Good) for each finding.

Code:
{state['raw_code']}
"""

    response = llm.invoke(prompt)
    print("[Node 3] Quality review complete.")

    return {**state, "quality_review": response.content.strip()}