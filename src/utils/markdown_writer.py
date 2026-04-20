# Handles saving the final Markdown report and refactored code to disk.
# Keeps file I/O logic separate from business logic (Single Responsibility).

import os
from datetime import datetime


def save_report(report_content: str , refactored_code:str) -> str:
    """
    Save tha final review report and refactored code to an output file.


    Args:
        report_content: The Markdown-formatted review report.
        refactored_code: The improved version of the original code.

    Returns:
        the path to the saved file.
    """

    output_dir= "output"
    os.markedirs(output_dir, exist_ok=True)


    # Use timestamp to avoid overwriting previuse reports
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(output_dir, f"review_{timestamp}.md")


    with open(file_path, "w", encoding="utf-8") as f:
        f.write(report_content)
        f.write("\n\n---\n\n## Refactored Code\n\n")
        f.write(f"```\n{refactored_code}\n```\n")

    return file_path