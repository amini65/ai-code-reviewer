# Node 7: Assembles all review outputs into a single, polished Markdown report.

from src.graph.state import CodeReviewState
from src.utils.llm_client import get_llm
from src.utils.markdown_writer import save_report


def report_generator_node(state: CodeReviewState) -> CodeReviewState:
    """
    Combines outputs from all previous nodes into one comprehensive
    Markdown report and saves it to disk.

    The report includes:
    - Executive summary
    - Language detection result
    - Quality review findings
    - Security audit findings
    - Optimization suggestions
    - Refactored code

    Args:
        state: The final shared state with all review fields populated.

    Returns:
        Updated state with 'final_report' field populated.
    """
    llm = get_llm(temperature=0.3)

    prompt = f"""You are a technical writer. Create a polished, professional
Markdown report summarizing a complete code review session.

Structure the report with these sections:
1. # AI Code Review Report
2. ## Summary (2-3 sentence executive overview)
3. ## Detected Language
4. ## Code Quality Analysis
5. ## Security Audit
6. ## Optimization Suggestions
7. ## Conclusion & Next Steps

Here is the raw data for each section:

**Language:** {state.get('language')}

**Quality Review:**
{state.get('quality_review', 'N/A')}

**Security Review:**
{state.get('security_review', 'N/A')}

**Optimization Suggestions:**
{state.get('optimization_suggestions', 'N/A')}

Make it clean, professional, and easy to read.
"""

    response = llm.invoke(prompt)
    report = response.content.strip()

    # Save report and refactored code to disk
    refactored = state.get("refactored_code", "# Refactored code not available")
    file_path = save_report(report, refactored)

    print(f"[Node 7] Final report saved to: {file_path}")

    return {**state, "final_report": report}