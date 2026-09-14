from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config

def get_embeddings_model():
    embeddings = JinaEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)
    return embeddings