
from langchain_groq import ChatGroq
from hr_assistant import config


def get_llm():
    """Returns an instance of the ChatGroq model configured with the specified model name and temperature."""
    return ChatGroq(model=config.LLM_MODEL_NAME, temperature=0)
