from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config

def get_embeddings_model():
    """Returns an instance of the JinaEmbeddings model configured with the specified model name."""
    return JinaEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)
   