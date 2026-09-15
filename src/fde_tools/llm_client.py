import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)


def call_llm(provider: str, model: str, messages: list, **kwargs) -> str:
    """
    Generic method to make LLM calls to different providers.

    Args:
        provider: "openai" or "gemini"
        model: Model name (e.g., "gpt-4", "gemini-3.6-flash")
        messages: List of message dicts with 'role' and 'content'
        **kwargs: Additional parameters like temperature, max_tokens, etc.

    Returns:
        The response content as a string
    """
    if provider.lower() == "openai":
        client = OpenAI()
    elif provider.lower() == "gemini":
        client = OpenAI(
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        )
    else:
        raise ValueError(f"Unsupported provider: {provider}. Use 'openai' or 'gemini'.")

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        **kwargs
    )

    return response.choices[0].message.content
