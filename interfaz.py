import streamlit as st
import chromadb
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

st.title("⚽ Mi IA de Cristiano Ronaldo")
st.write("Hazle preguntas al sistema RAG sobre el archivo de texto.")

# Configuración (Igual que en app.py)
llm = Ollama(model="llama3", request_timeout=120.0)
embed_model = OllamaEmbedding(model_name="nomic-embed-text")

# Cargar la base de datos que ya creamos
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("mi_coleccion")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store(vector_store, embed_model=embed_model)

# Caja de texto para preguntar
pregunta = st.text_input("Escribe tu pregunta aquí:")

if pregunta:
    with st.spinner("Pensando..."):
        query_engine = index.as_query_engine(llm=llm)
        respuesta = query_engine.query(pregunta)
        st.success(f"Respuesta: {respuesta}")