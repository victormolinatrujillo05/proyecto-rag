# 🧠 Proyecto RAG: Asistente Inteligente Local

## 📌 Descripción

Este proyecto implementa un sistema de **Retrieval-Augmented Generation (RAG)** para consultar documentos locales utilizando modelos de lenguaje (LLMs) ejecutados de forma completamente local mediante **Ollama**.

El asistente permite cargar documentos propios, indexarlos y realizar consultas inteligentes, combinando recuperación de información con generación de respuestas contextuales. Todo el procesamiento se realiza en local, garantizando privacidad y control total de los datos.

---

## 🚀 Tecnologías Utilizadas

| Tecnología     | Descripción                                                                 |
|----------------|-----------------------------------------------------------------------------|
| Ollama         | Ejecución local de modelos de lenguaje (LLMs)                               |
| LlamaIndex     | Framework para construir sistemas RAG                                       |
| ChromaDB       | Base de datos vectorial para almacenamiento de embeddings                   |
| Streamlit      | Interfaz web interactiva para el usuario                                    |

---

## ⚙️ Instalación

```bash
# Descargar modelos necesarios
ollama pull llama3
ollama pull nomic-embed-text

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
streamlit run interfaz.py

🌐 Acceso

Una vez iniciada la aplicación, estará disponible en:

👉 http://localhost:8501

📁 Estructura del Repositorio
├── app.py
├── interfaz.py
├── data/
├── chroma_db/
├── requirements.txt
└── .gitignore
🧩 Decisiones Técnicas

Persistencia local en ChromaDB: Permite almacenar y reutilizar embeddings sin necesidad de recalcularlos.

Privacidad total (100% local): No se envían datos a servicios externos, todo el procesamiento ocurre en tu máquina.

Interfaz intuitiva con Streamlit: Facilita la interacción con el sistema RAG sin necesidad de conocimientos técnicos avanzados.