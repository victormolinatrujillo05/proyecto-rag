import chromadb
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

# 1. Conectamos con Ollama (usando lo que ya tienes)
llm = Ollama(model="llama3", request_timeout=120.0)
embed_model = OllamaEmbedding(model_name="nomic-embed-text")

# 2. Leemos tu archivo datos.txt
print("--- Paso 1: Leyendo tus datos ---")
documents = SimpleDirectoryReader("./data").load_data()

# 3. Preparamos la base de datos (Aquí se creará la carpeta chroma_db)
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("mi_coleccion")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# 4. Creamos el índice (Indexación)
print("--- Paso 2: Creando la carpeta chroma_db ---")
index = VectorStoreIndex.from_documents(
    documents, 
    storage_context=storage_context, 
    embed_model=embed_model
)

# 5. Hacemos la pregunta
print("--- Paso 3: Consultando a la IA ---")
query_engine = index.as_query_engine(llm=llm)
respuesta = query_engine.query("¿Cuántos Balones de Oro tiene Cristiano?")

print(f"\nRESULTADO FINAL: {respuesta}")