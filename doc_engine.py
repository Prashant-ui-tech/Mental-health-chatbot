from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

# 🔥 FIX: Set local LLM (Phi via Ollama)
Settings.llm = Ollama(model="phi")

# Load documents
documents = SimpleDirectoryReader("data").load_data()

# Free local embedding model (FAST)
embed_model = HuggingFaceEmbedding(model_name="all-MiniLM-L6-v2")

# Create index
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

# Query engine
query_engine = index.as_query_engine(llm=Settings.llm)

def query_documents(query: str):
    response = query_engine.query(query)
    return str(response)