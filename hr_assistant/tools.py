
from langchain.tools import tool
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def create_serch_tool(retriever):
    """
    Creates a search tool for the HR assistant. 
    The tool uses the provided retriever to find relevant information based on user queries.
    """
    @tool
    def search_hr_policy(question: str) -> str:
        """
        Searches the HR policy documents for relevant information based on the user's question.

        """
        logger.info("Searching HR policy for question: %s", question)
        matching_chunks = retriever.invoke(question)
        logger.info("Found %d matching chunks for the question.", len(matching_chunks))
        return "\n\n".join(chunk.page_content for chunk in matching_chunks)

    return search_hr_policy