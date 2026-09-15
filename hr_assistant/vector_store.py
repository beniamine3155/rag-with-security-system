
from langchain_community.vectorstores import FAISS
from hr_assistant import config
from hr_assistant.embeddings import get_embeddings_model
from hr_assistant.logger import get_logger
import os

logger = get_logger(__name__)


def build_vector_store(chunks):
    """Builds a vector store from the provided document chunks using FAISS and the specified embeddings model."""
    logger.info("Building vector store from document chunks.")
    embeddings_model = get_embeddings_model()
    vector_store = FAISS.from_documents(chunks, embeddings_model)
    logger.info("Vector store built successfully.")
    return vector_store


def save_vector_store(vector_store, path: str=config.VECTOR_STORE_PATH):
    """Saves the provided vector store to the specified path."""
    logger.info("Saving vector store to path: %s", path)
    vector_store.save_local(path)


def load_vector_store(path: str = config.VECTOR_STORE_PATH):
    """Loads a vector store from the specified path using FAISS and the specified embeddings model."""
    logger.info("Loading vector store from path: %s", path)
    embeddings_model = get_embeddings_model()
    return FAISS.load_local(path, embeddings_model, allow_dangerous_deserialization=True)


def vector_store_exists(path: str= config.VECTOR_STORE_PATH):
    """Checks if a vector store exists at the specified path by looking for the index file."""
    logger.info("Checking if vector store exists at path: %s", path)
    return os.path.exists(os.path.join(path, "index.faiss"))


def get_retriever(vector_store, k: int=config.TOP_K_RESULTS):
    """Returns a retriever from the provided vector store with the specified number of top results to return."""
    logger.info("Creating retriever with top %d results.", k)
    return vector_store.as_retriever(search_kwargs={"k": k})
