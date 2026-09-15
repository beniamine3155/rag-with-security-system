
from langchain_groq import ChatGroq
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def get_llm():
    """Returns an instance of the ChatGroq model configured with the specified model name and temperature."""
    logger.info("Initializing LLM model: %s", config.LLM_MODEL_NAME)
    return ChatGroq(model=config.LLM_MODEL_NAME, temperature=0)
