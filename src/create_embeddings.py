import os
import chromadb
from sentence_transformers import SentenceTransformer
from load_documents import load_markdown_files, load_csv_files


# Cargar documentos
documents = load_markdown_files()
documents.extend(load_csv_files())


# Modelo de embeddings
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# Crear base vectorial
client = chromadb.PersistentClient(
    path="vectorstore"
)


collection = client.get_or_create_collection(
    name="cybernova_docs"
)


# Guardar documentos
for index, doc in enumerate(documents):

    embedding = model.encode(
        doc["content"]
    ).tolist()


    collection.add(
        ids=[str(index)],
        embeddings=[embedding],
        documents=[doc["content"]],
        metadatas=[
            {
                "source": doc["name"]
            }
        ]
    )


print("✅ Documentos almacenados en ChromaDB")

