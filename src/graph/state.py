# Defines the shared state that flows through all LangGraph nodes.
# Every node reads from and writes to this TypedDict.

from typing import Optional
from typing_extensions import TypedDict


class CodeReviewState(TypedDict):
    """
    Sheard state passed between all nodes n the review graph.
    Ech node may read existing fields and add or update fields.
    """

    #Input: the raw code submitted by user
    raw_code: str 

    # Deteced programing language (e.g., "")
    language: Optional[str]

    # Whether the syntax check found errors
    has_syntax_error: bool

    #Details of syntax errors if any were found
    syntax_error_details: Optional[str]

    # Output from the Code Quaity Review node
    quality_review: Optional[str]

    # Output from the Security Review node
    security_review: Optional[str]

    # Output from the Optimization Suggestion node
    optimaization_suggestions: Optional[str]

    # The refactored version of the original code
    refactored_code: Optional[str]

    # The final Markdown report combining all reviews
    final_report: Optional[str]

    # Used when a syntax error stops the pipeline early
    error_report: Optional[str]