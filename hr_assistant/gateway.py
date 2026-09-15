
import json

from langchain_openai import ChatOpenAI
from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL

from hr_assistant import config
from hr_assistant.logger import get_logger


logger = get_logger(__name__)



PRIMARY_PROVIDER = "@hrpolicy"



def get_gateway_llm() -> ChatOpenAI:
    """Return a chat model routed through Portkey (no config/fallback - see module docstring)."""
    logger.info("Routing LLM calls through Portkey (provider=%s)", PRIMARY_PROVIDER)
    headers = createHeaders(api_key=config.PORTKEY_API_KEY, provider=PRIMARY_PROVIDER)
    return ChatOpenAI(
        api_key="portkey",  # dummy value - the real auth is in the headers
        base_url=PORTKEY_GATEWAY_URL,
        model=config.LLM_MODEL_NAME,
        default_headers=headers,
    )