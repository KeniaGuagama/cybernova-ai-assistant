import time
import chromadb
from sentence_transformers import SentenceTransformer
from langchain_ollama import ChatOllama


# =====================================================
# CARGA DE MODELOS
# =====================================================

print("Cargando modelo de embeddings...")

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


print("Conectando con ChromaDB...")

client = chromadb.PersistentClient(
    path="vectorstore"
)


collection = client.get_collection(
    name="cybernova_docs"
)


print("Cargando modelo IA...")

llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)


print("✅ CyberNova listo.\n")



# =====================================================
# FILTRO DE CIBERSEGURIDAD
# =====================================================

security_keywords = [

    "seguridad",
    "ciberseguridad",
    "incidente",
    "ataque",
    "phishing",
    "malware",
    "virus",
    "ransomware",
    "contraseña",
    "password",
    "autenticación",
    "acceso",
    "privacidad",
    "datos",
    "información",
    "riesgo",
    "vulnerabilidad",
    "firewall",
    "red",
    "correo",
    "sospechoso",
    "política",
    "politica",
    "usuario",
    "sistema",
    "empresa"

]



def is_security_question(question):

    question = question.lower()

    return any(
        word in question
        for word in security_keywords
    )



# =====================================================
# BUSQUEDA VECTORIAL
# =====================================================

def search_documents(question):


    vector = embedding_model.encode(
        question,
        normalize_embeddings=True
    ).tolist()


    results = collection.query(
        query_embeddings=[vector],
        n_results=2
    )


    documents = results["documents"][0]


    return "\n\n".join(documents)



# =====================================================
# AGENTE CYBERNOVA
# =====================================================

def ask_agent(question):


    inicio = time.time()



    # BLOQUEAR PREGUNTAS FUERA DEL DOMINIO

    if not is_security_question(question):

        return (
            "No tengo información disponible sobre ese tema."
        )



    # Buscar información

    context = search_documents(question)



    tiempo_busqueda = time.time()



    prompt = f"""

Eres CyberNova AI Assistant.

Tu función es responder únicamente consultas
relacionadas con ciberseguridad empresarial.


REGLAS:

- Usa solamente la información del contexto.
- No uses conocimiento externo.
- No inventes respuestas.
- Si la información no aparece en el contexto responde:

"No tengo información disponible sobre ese tema."


CONTEXTO:

{context}


PREGUNTA:

{question}


RESPUESTA:
"""


    response = llm.invoke(prompt)



    tiempo_final = time.time()



    print(
        f"🔎 Búsqueda: {tiempo_busqueda-inicio:.2f}s | "
        f"🤖 IA: {tiempo_final-tiempo_busqueda:.2f}s | "
        f"⏱ Total: {tiempo_final-inicio:.2f}s"
    )



    return response.content





# =====================================================
# PRUEBA CONSOLA
# =====================================================

if __name__ == "__main__":


    print("=" * 60)
    print("🛡 CyberNova AI Assistant")
    print("Escribe 'salir' para terminar.")
    print("=" * 60)



    while True:


        question = input("\nPregunta: ")



        if question.lower() == "salir":
            break



        answer = ask_agent(question)



        print("\nRespuesta:\n")
        print(answer)