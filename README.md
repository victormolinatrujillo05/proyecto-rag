# 🤖 Proyecto RAG: Asistente Inteligente Local (Cristiano Ronaldo)

Este repositorio contiene la implementación de un sistema de **Generación Aumentada por Recuperación (RAG)**. El objetivo es permitir realizar consultas en lenguaje natural sobre documentos locales (datos personalizados) utilizando modelos de lenguaje (LLMs) ejecutados de forma totalmente local con **Ollama**.

## 📋 Descripción del Proyecto

El sistema utiliza una arquitectura RAG para extraer información de archivos de texto y generar respuestas precisas. El flujo de trabajo consiste en cargar documentos de la carpeta `/data`, transformarlos en **embeddings** y almacenarlos en una base de datos vectorial (**ChromaDB**) para realizar búsquedas por similitud semántica.

## 🛠️ Tecnologías Utilizadas

| Herramienta | Función |
| :--- | :--- |
| **Ollama** | Ejecución local de Llama 3 y embeddings |
| **LlamaIndex** | Orquestación entre documentos, vectores y el modelo |
| **ChromaDB** | Base de datos vectorial persistente |
| **Streamlit** | Interfaz de usuario web interactiva |

## 🚀 Instalación y Configuración

### 1. Requisitos Previos
Es necesario tener instalado [Ollama](https://ollama.com/) y haber descargado los modelos necesarios:
```powershell
ollama pull llama3
ollama pull nomic-embed-text

### 2. Configuración del Entorno y Ejecución

Sigue estos comandos en tu terminal para preparar el entorno virtual e instalar las dependencias:
# Crear el entorno virtual
python -m venv venv

# Activar el entorno (Windows)
.\venv\Scripts\activate

# Instalar librerías necesarias
pip install -r requirements.txt

# Ejecutar la interfaz web
streamlit run interfaz.py

Una vez ejecutado, la aplicación estará disponible en: http://localhost:8501

📂 Estructura del Repositorio
app.py: Motor lógico del sistema (procesamiento y consulta por terminal).

interfaz.py: Aplicación web interactiva con Streamlit.

data/: Directorio que contiene los archivos de conocimiento (datos.txt).

chroma_db/: Base de datos vectorial persistente (generada automáticamente).

requirements.txt: Listado de dependencias del proyecto.

.gitignore: Archivos excluidos del repositorio (como venv/).

⚙️ Decisiones Técnicas
Persistencia Local: Se ha configurado ChromaDB para que el índice sea persistente en la carpeta chroma_db/, evitando la re-indexación constante.

Privacidad Total: Todo el procesamiento ocurre en el hardware local, sin enviar datos a APIs externas ni servicios en la nube.

Interfaz Streamlit: Se ha desarrollado una UI sencilla para facilitar la interacción del usuario final con el sistema RAG.