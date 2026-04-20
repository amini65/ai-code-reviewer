# Single source of truth for creating the LLM instance.
# All nodes import from here to avoid creating multiple connections.


import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()


def get_llm(temperature: float=0.2) -> ChatOpenAi:

    """
    Returns a configured ChatOpenAi instance.

    Args:
        temperature: Controls randomness. lower = more deterministic.
                        For code analysis, keep this low (0.0 - 0.3).

    Returns:
            A ChatOpenAi instance ready to use.
    """
    api_key= os.getenv("OPEN_API_KEY")


    if not api_key:
        raise EnvironmentError(
            "OPENAI_API_KEY not found."
            "Please copy .env.example to .env and set your key."
        )
    

    return ChatOpenAI(
        model="gpt-4o-mini",  # Cost-effective, strong for code tasks
        temperature=temperature,
        api_key=api_key,
    )
