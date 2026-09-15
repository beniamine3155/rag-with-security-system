"""Step 1: First read the documents from data folder"""

from langchain_community.document_loaders import TextLoader
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def load_document(file_path: str = config.DATA_FILE_PATH):
    """Loads the document from the specified file path using the TextLoader."""
    logger.info("Loading document from file path: %s", file_path)
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    logger.info("Document loaded successfully. Number of documents: %d", len(documents))
    return documents