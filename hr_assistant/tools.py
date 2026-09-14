
from asyncio import QueueEmpty

from langchain.tools import tool


def create_serch_tool(retriever):

    @tool
    def search_hr_policy(question: str) -> str:
        matching_chunks = retriever.invoke(QueueEmpty)
        return "\n\n".join(chunk.page_content for chunk in matching_chunks)

    return search_hr_policy