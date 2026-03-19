# 🤖 Proyecto RAG: Asistente Inteligente Local

Este repositorio contiene la implementación de un sistema de **Generación Aumentada por Recuperación (RAG)**. El objetivo es permitir realizar consultas en lenguaje natural sobre documentos locales (datos personalizados) utilizando modelos de lenguaje (LLMs) ejecutados de forma totalmente local con **Ollama**.

## 📋 Descripción del Proyecto

El sistema utiliza una arquitectura RAG para extraer información de archivos de texto y generar respuestas precisas. El flujo consiste en cargar documentos de la carpeta `/data`, transformarlos en **embeddings** y almacenarlos en una base de datos vectorial (**ChromaDB**) para realizar búsquedas por similitud semántica.

## 🛠️ Tecnologías Utilizadas

| Herramienta | Función |
| :--- | :--- |
| **Ollama** | Ejecución local de LLMs y generación de embeddings |
| **LlamaIndex** | Orquestación entre documentos, vectores y el modelo |
| **ChromaDB** | Base de datos vectorial persistente |
| **Streamlit** | Interfaz de usuario web interactiva |

## 🚀 Instalación y Ejecución

Sigue estos pasos en tu terminal para preparar el entorno virtual, instalar las dependencias y lanzar la aplicación:

```powershell
# 1. Descargar modelos en Ollama
ollama pull llama3
ollama pull nomic-embed-text

# 2. Configurar entorno y ejecutar
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
streamlit run interfaz.py

Acceso a la aplicación: Una vez ejecutado, la interfaz estará disponible en su navegador en: http://localhost:8501

📂 Estructura del Repositorio
app.py           # Motor lógico del sistema (procesamiento y consulta por terminal).
interfaz.py      # Aplicación web interactiva con Streamlit.
data/            # Directorio que contiene los archivos de conocimiento (.txt).
chroma_db/       # Base de datos vectorial persistente (generada automáticamente).
requirements.txt # Listado de dependencias del proyecto.
.gitignore       # Archivos excluidos del repositorio (como venv/).


⚙️ Decisiones Técnicas
Persistencia Local: Se ha configurado ChromaDB para que el índice sea persistente 
en la carpeta chroma_db/, evitando la re-indexación constante y optimizando el 
uso de recursos de hardware.

Privacidad Total: Todo el procesamiento ocurre íntegramente en el hardware local, 
sin enviar datos a APIs externas ni servicios en la nube.

Interfaz Streamlit: Se ha desarrollado una interfaz sencilla e intuitiva para 
facilitar la interacción del usuario final con el sistema RAG de forma visual.