# Constructs the LangGraph workflow, connects all nodes,
# and defines the conditional branching logic.

from langgraph.graph import StateGraph, END
from src.graph.state import CodeReviewState
from src.nodes import (
    language_detection_node,
    syntax_check_node,
    quality_review_node,
    security_review_node,
    optimization_node,
    refactor_node,
    report_generator_node,
    error_report_node,
)


def route_after_syntax_check(state: CodeReviewState) -> str:
    """
    Conditional routing function called after the Syntax Check node.

    If a syntax error exists, the graph routes to the error branch.
    Otherwise, it continues to the main review pipeline.

    Args:
        state: The current shared state with 'has_syntax_error' set.

    Returns:
        The name of the next node to execute.
    """
    if state.get("has_syntax_error", False):
        print("[Router] Syntax error detected → routing to error report.")
        return "error_report"
    else:
        print("[Router] No syntax errors → continuing to full review.")
        return "quality_review"


def build_graph() -> StateGraph:
    """
    Builds and compiles the complete LangGraph review workflow.

    Graph structure:
    START
      └─► language_detection
            └─► syntax_check
                  ├─► [has error] error_report ──► END
                  └─► [no error]  quality_review
                                    └─► security_review
                                          └─► optimization
                                                └─► refactor
                                                      └─► report_generator ──► END

    Returns:
        A compiled, executable LangGraph graph.
    """
    # Initialize the graph with our shared state type
    graph = StateGraph(CodeReviewState)

    # --- Register all nodes ---
    graph.add_node("language_detection", language_detection_node)
    graph.add_node("syntax_check", syntax_check_node)
    graph.add_node("error_report", error_report_node)
    graph.add_node("quality_review", quality_review_node)
    graph.add_node("security_review", security_review_node)
    graph.add_node("optimization", optimization_node)
    graph.add_node("refactor", refactor_node)
    graph.add_node("report_generator", report_generator_node)

    # --- Define the main linear flow ---
    graph.set_entry_point("language_detection")
    graph.add_edge("language_detection", "syntax_check")

    # --- Conditional branching after syntax check ---
    graph.add_conditional_edges(
        source="syntax_check",
        path=route_after_syntax_check,
        path_map={
            "error_report": "error_report",
            "quality_review": "quality_review",
        },
    )

    # --- Error branch: terminates immediately ---
    graph.add_edge("error_report", END)

    # --- Happy path: continue through all review nodes ---
    graph.add_edge("quality_review", "security_review")
    graph.add_edge("security_review", "optimization")
    graph.add_edge("optimization", "refactor")
    graph.add_edge("refactor", "report_generator")
    graph.add_edge("report_generator", END)

    return graph.compile()