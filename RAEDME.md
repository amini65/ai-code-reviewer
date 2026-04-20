# AI Code Reviewer (LangGraph Multi-step Agent)

A modular Python project built with **LangGraph** that reviews user-submitted code in multiple stages and generates:

- A complete **Markdown code review report**
- A **refactored version** of the original code

The pipeline focuses on:
- Code quality (Clean Code + SOLID)
- Security risks (OWASP-style issues)
- Performance and optimization opportunities

---

## Project Goal

`AI Code Reviewer` is designed as a **multi-step AI agent workflow** where each node has a single responsibility:

1. Detect programming language
2. Check syntax validity
3. Branch:
   - If syntax is invalid -> generate error report and stop
   - If syntax is valid -> continue full review
4. Review code quality
5. Review security risks
6. Suggest optimization improvements
7. Generate refactored code
8. Produce final Markdown report and save output

This architecture keeps the system easy to maintain, test, and extend.

---

## Tech Stack

- Python 3.10+
- LangGraph
- LangChain OpenAI
- python-dotenv
- OpenAI API (model currently set to `gpt-4o-mini`)

---

## Architecture

### Graph Flow

`language_detection -> syntax_check -> (error_report | quality_review -> security_review -> optimization -> refactor -> report_generator)`

### Why LangGraph Here?

- Clear state-driven workflow
- Conditional routing (syntax error branch)
- Easy node-level extensibility
- Better separation of concerns than a single prompt chain

---

## Project Structure

```text
ai-code-reviewer/
├── main.py
├── requirements.txt
├── .env.example
├── RAEDME.me
├── src/
│   ├── graph/
│   │   ├── __init__.py
│   │   ├── builder.py
│   │   └── state.py
│   ├── nodes/
│   │   ├── __init__.py
│   │   ├── language_detection.py
│   │   ├── syntax_check.py
│   │   ├── error_report.py
│   │   ├── quality_review.py
│   │   ├── security_review.py
│   │   ├── optimization.py
│   │   ├── refactor.py
│   │   └── report_generator.py
│   └── utils/
│       ├── llm_client.py
│       └── markdown_writer.py
└── output/
```

---

## Setup

### 1) Clone project

```bash
git clone <your-repo-url>
cd ai-code-reviewer
```

### 2) Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure environment variables

```bash
cp .env.example .env
```

Then set your API key in `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPEN_API_KEY=your_openai_api_key_here
```

> Note: Current code reads `OPEN_API_KEY` while `.env.example` contains `OPENAI_API_KEY`.  
> To avoid runtime issues, define both keys for now.

---

## Run

```bash
python main.py
```

You will be prompted to paste code in terminal.  
Type `END` on a new line to finish input and start the review pipeline.

---

## Output

On success (no syntax errors):
- Console prints final review report
- A timestamped Markdown file is saved in `output/`
- Saved file contains:
  - Full review report
  - Refactored code block

On syntax error:
- Pipeline routes to error branch
- You receive a focused syntax error report with fixes

---

## Node Responsibilities

- `language_detection`: detect language from raw code
- `syntax_check`: validate syntax and set branch decision
- `error_report`: generate friendly syntax-fix report
- `quality_review`: clean code + SOLID analysis
- `security_review`: vulnerability and risk audit
- `optimization`: performance suggestions with before/after ideas
- `refactor`: rewrite code by applying all findings
- `report_generator`: build final Markdown and save artifact

---

## Extending the Project

You can add new review capabilities by:

1. Creating a new node in `src/nodes/`
2. Extending `CodeReviewState` in `src/graph/state.py`
3. Registering and wiring the node in `src/graph/builder.py`
4. Including its output in `report_generator`

Suggested future improvements:
- Add tests for each node and graph-level integration
- Add retry/fallback logic for LLM failures
- Add support for file input (not only terminal paste)
- Add structured JSON output mode
- Add optional static analysis tools (flake8/bandit/mypy)
- Add web API (FastAPI) and simple UI

---

## Development Notes

- Keep node prompts focused and single-purpose
- Use low temperature for deterministic analysis tasks
- Avoid mixing file I/O logic into analysis nodes
- Keep graph state explicit and typed

---

## Troubleshooting

- **Missing API key error**: ensure `.env` exists and contains the required key variables.
- **Import errors**: verify virtual environment is active and dependencies are installed.
- **No output file created**: check write permissions and confirm `output/` can be created.
- **LLM response quality issues**: tune node prompts and temperatures.

---

## License

Choose one and add it to your repository (recommended: MIT).

---

## Contributing

Contributions are welcome.  
If you open a PR, include:
- clear problem statement
- change summary
- test or verification steps

