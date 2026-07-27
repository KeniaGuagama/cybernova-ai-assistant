# 🛡️ CyberNova AI Assistant

(assets/cybernova_logo.png)

## Asistente inteligente de ciberseguridad basado en RAG

CyberNova AI Assistant es un asistente inteligente desarrollado con **Python, Streamlit y arquitectura RAG (Retrieval-Augmented Generation)**, diseñado para responder consultas relacionadas con ciberseguridad utilizando una base de conocimiento empresarial.

El sistema combina búsqueda semántica, modelos de lenguaje e información documental para proporcionar respuestas contextualizadas a partir de documentos corporativos como políticas de seguridad, gestión de incidentes y preguntas frecuentes.

---

# 🚀 Características principales

✅ **Asistente conversacional de ciberseguridad**  
Responde preguntas utilizando información almacenada en documentos especializados.

✅ **Arquitectura RAG (Retrieval-Augmented Generation)**  
Recupera información relevante antes de generar respuestas mediante inteligencia artificial.

✅ **Búsqueda semántica**  
Utiliza embeddings para encontrar información relacionada dentro de la base documental.

✅ **Base de conocimiento empresarial**
Soporta documentos en formatos Markdown y CSV.

✅ **Interfaz web interactiva**
Aplicación desarrollada con Streamlit con diseño personalizado y experiencia conversacional.

✅ **Procesamiento local con modelos de IA**
Utiliza Ollama con el modelo Qwen 2.5 1.5B para generación de respuestas.

---

# 🏗️ Arquitectura del sistema

Usuario
│
▼
Interfaz Streamlit
│
▼
Sistema RAG
│
├── Sentence Transformers
│ │
│ ▼
│ Embeddings
│
├── ChromaDB
│ │
│ ▼
│ Recuperación documental
│
▼
Modelo LLM
(Ollama + Qwen 2.5 1.5B)
│
▼
Respuesta contextualizada


---

# 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| Streamlit | Desarrollo de interfaz web |
| LangChain | Integración con modelos de lenguaje |
| Ollama | Ejecución local del modelo IA |
| Qwen 2.5 1.5B | Modelo de lenguaje |
| ChromaDB | Base de datos vectorial |
| Sentence Transformers | Generación de embeddings |
| all-MiniLM-L6-v2 | Modelo de embeddings |

---

# 📂 Estructura del proyecto

cybernova-ai-assistant/
│
├── assets/
│ └── cybernova_logo.png
│
├── documents/
│ ├── gestion_incidentes.md
│ ├── politica_seguridad.md
│ └── faq_seguridad.csv
│
├── src/
│ ├── app.py
│ ├── chatbot.py
│ └── load_documents.py
│
├── vectorstore/
│
├── requirements.txt
│
└── README.md


---

# ⚙️ Instalación y ejecución

## Clonar repositorio

bash
git clone https://github.com/KeniaGuagama/cybernova-ai-assistant.git

# Acceder al proyecto
cd cybernova-ai-assistant

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Windows)
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Cargar documentos a la base vectorial
python src/load_documents.py

# Ejecutar aplicación
streamlit run src/app.py


📚 Base de conocimiento
CyberNova utiliza documentos corporativos como fuente de información:

🔐 Política de Seguridad de la Información
🚨 Gestión de Incidentes de Seguridad
❓ FAQ de Seguridad

Estos documentos permiten responder consultas relacionadas con:

✅ Reporte de incidentes.
✅ Protección de contraseñas.
✅ Seguridad de información.
✅ Phishing.
✅ Buenas prácticas de seguridad.

💬 Ejemplos de consultas

¿Qué es un incidente de seguridad?
¿Cómo reporto phishing?
¿Qué debo hacer si pierdo mi laptop corporativa?
¿Puedo compartir mi contraseña?
¿Qué medidas establece la política de seguridad?

📸 Evidencias

Agregar capturas de pantalla mostrando:

Interfaz del asistente.
(assets/Captura 1.png)

Respuestas generadas por el sistema.
(assets/Captura 2.png)
(assets/Captura 3.png)
(assets/Captura 4.png)


👩‍💻 Autora

Kenia Irlanda Guagama Gil
Ingeniera Informática

Proyecto desarrollado como aplicación práctica de Inteligencia Artificial, RAG y ciberseguridad.
