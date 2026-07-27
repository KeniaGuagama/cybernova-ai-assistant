
# 🛡️ CyberNova AI Assistant

CyberNova AI Assistant es un asistente inteligente desarrollado con Python, Streamlit y tecnologías RAG (Retrieval-Augmented Generation) para responder preguntas sobre ciberseguridad utilizando documentos corporativos.

## 🚀 Características

- Responde preguntas basadas en documentos.
- Búsqueda semántica mediante ChromaDB.
- Modelo de lenguaje ejecutado localmente con Ollama.
- Interfaz web desarrollada con Streamlit.
- Base de conocimiento en formato Markdown y CSV.

---

## 🛠️ Tecnologías utilizadas

- Python
- Streamlit
- LangChain
- Ollama
- Qwen 2.5 1.5B
- ChromaDB
- Sentence Transformers
- all-MiniLM-L6-v2

---

## 📂 Estructura del proyecto

```
cybernova-ai-assistant/
│
├── assets/
│   └── cybernova_logo.png
│
├── documents/
│   ├── gestion_incidentes.md
│   ├── politica_seguridad.md
│   └── faq_seguridad.csv
│
├── src/
│   ├── app.py
│   ├── chatbot.py
│   └── load_documents.py
│
├── vectorstore/
│
├── requirements.txt
│
└── README.md
```

---

## ▶️ Instalación

Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/cybernova-ai-assistant.git
```

Entrar al proyecto

```bash
cd cybernova-ai-assistant
```

Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno

Windows

```bash
venv\Scripts\activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Cargar los documentos

```bash
python src/load_documents.py
```

Ejecutar la aplicación

```bash
streamlit run src/app.py
```

---

## 📚 Base de conocimiento

El asistente utiliza documentos corporativos para responder preguntas.

- Política de Seguridad de la Información
- Gestión de Incidentes
- FAQ de Seguridad

---

## 💬 Preguntas de ejemplo

- ¿Qué es un incidente de seguridad?
- ¿Cómo reporto phishing?
- ¿Qué es ransomware?
- ¿Qué es un firewall?
- ¿Qué es la autenticación multifactor?
- ¿Puedo compartir mi contraseña?
- ¿Qué hago si pierdo mi laptop corporativa?

---

## 📸 Capturas

Agregar aquí las capturas de la aplicación funcionando.

---

## ☁️ Deploy

La aplicación fue desplegada en Oracle Cloud Infrastructure (OCI).

Agregar aquí la URL pública del despliegue.

---

## 👩‍💻 Autora

**Kenia Irlanda Guagama Gil**

Ingeniera Informática

