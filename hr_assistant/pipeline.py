from hr_assistant import config
from hr_assistant.document_loader import load_document
from hr_assistant.splitter import split_into_chunks
from hr_assistant.vector_store import(
    build_vector_store,
    save_vector_store,
    load_vector_store,
    vector_store_exists,
    get_retriever
)
from hr_assistant.llm import get_llm
from hr_assistant.tools import create_serch_tool
from hr_assistant.agent import create_hr_agent


def build_vector_store_for_document(file_path: str = config.DATA_FILE_PATH):
    """
    Builds a vector store for the HR assistant. 
    If a vector store already exists, it loads it; otherwise, 
    it creates a new one from the provided document.
    """
    if vector_store_exists():
        return load_vector_store()

    documents = load_document(file_path)
    chunks = split_into_chunks(documents)

    vector_store = build_vector_store(chunks)
    save_vector_store(vector_store)

    return vector_store


def build_hr_assistant(file_path: str = config.DATA_FILE_PATH):
    """
    Builds the HR assistant by creating a vector store, retriever, search tool, and agent
    """
    config.check_api_keys()

    vector_store = build_vector_store_for_document(file_path)
    retriever = get_retriever(vector_store)
    search_tool = create_serch_tool(retriever)

    llm = get_llm()

    agent = create_hr_agent(llm, [search_tool])

    return agent


def ask(agent, question: str) -> str:
    """
    Asks a question to the HR assistant agent and returns the response.
    """
    response = agent.invoke({"messages": [{"role": "user", "content": question }]})
    return response["messages"][-1].content