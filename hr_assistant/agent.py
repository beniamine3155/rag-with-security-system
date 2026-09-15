
from langchain.agents import create_agent
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def create_hr_agent(llm, tools):
    """
    Creates an HR assistant agent with the specified language model and tools.
    """
    logger.info("Creating HR assistant agent with model: %s", config.LLM_MODEL_NAME)
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=config.SYSTEM_PROMPT
    )
    logger.info("HR assistant agent created successfully.")
    return agent