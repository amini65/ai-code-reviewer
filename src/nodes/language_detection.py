# Node 1: Detects the programming language of the submitted code.

from src.graph.state import CodeReviewState
from src.utils.llm_client import get_llm


def language_detection_node(state: CodeReviewState) -> CodeReviewState:
    """
    Identifies the programming language of the provided code snippet.
    Adds 'language' to the shared state.

    Args:
        state: The current shared state containing 'raw_code'.

    Returns:
        Updated state with 'language' field populated.
    """
    llm = get_llm(temperature=0.0)  # Zero temperature: factual answer only

    prompt = f"""Identify the programming language of the following code.
Reply with ONLY the language name (e.g., Python, JavaScript, Java).
No explanation, no extra text.

Code:
{state['raw_code']}
"""

    response = llm.invoke(prompt)
    detected_language = response.content.strip()

    print(f"[Node 1] Language detected: {detected_language}")

    return {**state, "language": detected_language}