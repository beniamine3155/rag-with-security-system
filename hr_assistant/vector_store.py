
# from langchain_community.vectorstores import FAISS
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

from hr_assistant import config
from hr_assistant.embeddings import get_embeddings_model
from hr_assistant.logger import get_logger
import os

logger = get_logger(__name__)


def build_vector_store(chunks):
    """Loads the document chunks into a Qdrant vector store."""
    logger.info("Building Qdrant vector store from document chunks.")
    embeddings_model = get_embeddings_model()
    vector_store = QdrantVectorStore.from_documents(
        chunks,
        embedding=embeddings_model,
        url = config.QDRANT_URL,
        api_key = config.QDRANT_API_KEY,
        collection_name = config.QDRANT_COLLECTION_NAME
    )
    logger.info("Uploaded to Qdrant Collection")
    return vector_store 


def load_vector_store():
    """Loads the Qdrant vector store from the specified collection."""
    logger.info("Loading Qdrant vector store from collection '%s'.", config.QDRANT_COLLECTION_NAME)
    embeddings_model = get_embeddings_model()
    return QdrantVectorStore.from_documents(
        documents=[],
        embedding=embeddings_model,
        url = config.QDRANT_URL,
        api_key = config.QDRANT_API_KEY,
        collection_name = config.QDRANT_COLLECTION_NAME
    )
   


def vector_store_exists():
    """Checks if the Qdrant collection exists."""
    logger.info("Checking if Qdrant collection '%s' exists.", config.QDRANT_COLLECTION_NAME)
    client = QdrantClient(
        url = config.QDRANT_URL,
        api_key = config.QDRANT_API_KEY
    )
    return client.collection_exists(config.QDRANT_COLLECTION_NAME)


def get_retriever(vector_store, k: int=config.TOP_K_RESULTS):
    """Returns a retriever from the provided vector store with the specified number of top results to return."""
    logger.info("Creating retriever with top %d results.", k)
    return vector_store.as_retriever(search_kwargs={"k": k})
