
from asyncio import QueueEmpty

from langchain.tools import tool


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
        matching_chunks = retriever.invoke(question)
        return "\n\n".join(chunk.page_content for chunk in matching_chunks)

    return search_hr_policy