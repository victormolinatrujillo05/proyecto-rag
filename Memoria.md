MEMORIA TÉCNICA: ASISTENTE DE IA LOCAL (SISTEMA RAG)
1. Introducción y Objetivos
El presente proyecto consiste en el diseño e implementación de un sistema de Generación Aumentada por Recuperación (RAG) capaz de responder preguntas sobre documentos locales de manera privada y eficiente. El objetivo principal es superar las limitaciones de los modelos de lenguaje (LLMs) convencionales, como las alucinaciones o la falta de conocimiento sobre datos actualizados o privados, sin depender de servicios en la nube.

2. Conceptos Clave y Fundamentos Teóricos
2.1. ¿Qué es un Embedding?
Los embeddings son representaciones numéricas (vectores) de fragmentos de texto. A diferencia de una búsqueda por palabras clave tradicional, los embeddings capturan el significado semántico. En este proyecto, se utiliza el modelo nomic-embed-text para convertir los párrafos de nuestros archivos .txt en listas de números en un espacio multidimensional. Esto permite que el sistema "entienda" que dos frases son similares aunque usen palabras distintas.

2.2. Búsqueda por Similitud Semántica
Cuando el usuario realiza una pregunta, el sistema la convierte también en un embedding y la compara con los vectores almacenados en ChromaDB. Mediante cálculos matemáticos (como la similitud del coseno), el sistema identifica los fragmentos del documento original que más se parecen a la consulta. Esta es la base de la recuperación de información en un sistema RAG.

2.3. ¿Por qué RAG mejora a los LLM?
Un LLM estándar como Llama 3 tiene un conocimiento "congelado" en el momento de su entrenamiento. El RAG mejora esto al:

Reducir Alucinaciones: El modelo solo responde basándose en los hechos extraídos del documento proporcionado.

Privacidad: Los datos nunca salen del equipo local.

Actualización: Basta con cambiar el archivo de texto en la carpeta /data para que la IA sepa cosas nuevas, sin necesidad de re-entrenar el modelo.

3. Arquitectura del Stack Tecnológico
El sistema se apoya en cuatro pilares fundamentales:

Ollama: Actúa como el motor de inferencia, permitiendo ejecutar Llama 3 y el modelo de embeddings de forma local y eficiente.

LlamaIndex: Es el orquestador que conecta los documentos con el modelo. Se encarga de la fragmentación (chunking), la creación del índice y la gestión de la memoria de la conversación.

ChromaDB: Base de datos vectorial persistente que almacena los embeddings. Su papel es crucial para no tener que volver a procesar los documentos cada vez que se abre la aplicación.

Streamlit: Proporciona una interfaz web intuitiva, permitiendo que cualquier usuario interactúe con el sistema sin usar la terminal.

4. Decisiones de Diseño y Problemas Encontrados
4.1. Persistencia de Datos
Inicialmente, el sistema recreaba el índice en cada ejecución, lo que consumía excesivo tiempo de CPU. Se decidió implementar StorageContext en LlamaIndex para forzar la persistencia en el disco local (/chroma_db). Esto optimizó el arranque del sistema en un 80%.

4.2. Limitaciones de Hardware y Soluciones
Durante las pruebas en el entorno local (portátil), se detectaron bloqueos cuando el sistema intentaba procesar documentos demasiado extensos o cuando la RAM disponible era escasa. Para solucionar esto:

Se ajustó el tamaño de los fragmentos de texto (chunk_size) para que el modelo pudiera procesarlos más rápido.

Se incrementó el timeout de las peticiones a Ollama para evitar que la interfaz de Streamlit diera error mientras el modelo generaba la respuesta.

5. Conclusión
La implementación de este sistema RAG demuestra que es posible desplegar soluciones de Inteligencia Artificial potentes y privadas en hardware doméstico. La combinación de LlamaIndex y Ollama ofrece una flexibilidad total para adaptar la IA a cualquier base de conocimientos específica sin los costes asociados a las APIs comerciales.