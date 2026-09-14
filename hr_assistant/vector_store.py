
from langchain_community.vectorstores import FAISS
from hr_assistant import config
from hr_assistant.embeddings import get_embeddings_model
import os


def build_vector_store(chunks):
    """Builds a vector store from the provided document chunks using FAISS and the specified embeddings model."""
    embeddings_model = get_embeddings_model()
    return FAISS.from_documents(chunks, embeddings_model)


def save_vector_store(vector_store, path: str=config.VECTOR_STORE_PATH):
    """Saves the provided vector store to the specified path."""
    vector_store.save_local(path)


def load_vector_store(path: str = config.VECTOR_STORE_PATH):
    """Loads a vector store from the specified path using FAISS and the specified embeddings model."""
    embeddings_model = get_embeddings_model()
    return FAISS.load_local(path, embeddings_model, allow_dangerous_deserialization=True)


def vector_store_exists(path: str= config.VECTOR_STORE_PATH):
    """Checks if a vector store exists at the specified path by looking for the index file."""
    return os.path.exists(os.path.join(path, "index.faiss"))


def get_retriever(vector_store, k: int=config.TOP_K_RESULTS):
    """Returns a retriever from the provided vector store with the specified number of top results to return."""
    return vector_store.as_retriever(search_kwargs={"k": k})
