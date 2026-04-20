# Entry point for the AI Code Reviewer application.
# Reads user input, initializes the graph, and prints the final results.

from src.graph import build_graph
from src.graph.state import CodeReviewState


def get_code_from_user() -> str:
    """
    Prompts the user to paste a code snippet via the terminal.
    Reads multi-line input until the user types 'END' on its own line.

    Returns:
        The raw code string entered by the user.
    """
    print("\n" + "=" * 60)
    print("   AI Code Reviewer — Powered by LangGraph + GPT")
    print("=" * 60)
    print("Paste your code below.")
    print("When done, type 'END' on a new line and press Enter.\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    return "\n".join(lines)


def main():
    """
    Main execution function:
    1. Collects code from the user
    2. Builds the LangGraph graph
    3. Runs the graph with the initial state
    4. Displays results based on outcome (error or full report)
    """
    raw_code = get_code_from_user()

    if not raw_code.strip():
        print("No code provided. Exiting.")
        return

    # Build the compiled graph
    graph = build_graph()

    # Create initial state — all optional fields default to None/False
    initial_state: CodeReviewState = {
        "raw_code": raw_code,
        "language": None,
        "has_syntax_error": False,
        "syntax_error_details": None,
        "quality_review": None,
        "security_review": None,
        "optimization_suggestions": None,
        "refactored_code": None,
        "final_report": None,
        "error_report": None,
    }

    print("\n Starting code review pipeline...\n")

    # Execute the graph — runs all nodes in sequence
    final_state = graph.invoke(initial_state)

    # Display appropriate output based on which branch was taken
    if final_state.get("has_syntax_error"):
        print("\n" + "=" * 60)
        print(" SYNTAX ERROR REPORT")
        print("=" * 60)
        print(final_state["error_report"])
    else:
        print("\n" + "=" * 60)
        print(" FINAL REVIEW REPORT")
        print("=" * 60)
        print(final_state["final_report"])
        print("\n✅ Full report and refactored code saved to the 'output/' folder.")


if __name__ == "__main__":
    main()