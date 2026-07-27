import os
import pandas as pd


DOCUMENTS_PATH = "documents"


def load_markdown_files():

    documents = []

    for file in os.listdir(DOCUMENTS_PATH):

        if file.endswith(".md"):

            path = os.path.join(DOCUMENTS_PATH, file)

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            documents.append({
                "name": file,
                "content": content
            })

    return documents


def load_csv_files():

    documents = []

    for file in os.listdir(DOCUMENTS_PATH):

        if file.endswith(".csv"):

            path = os.path.join(DOCUMENTS_PATH, file)

            df = pd.read_csv(path)

            content = df.to_string()

            documents.append({
                "name": file,
                "content": content
            })

    return documents



if __name__ == "__main__":

    docs = load_markdown_files()
    docs.extend(load_csv_files())


    print("Documentos encontrados:")
    
    for doc in docs:
        print("---------------------")
        print(doc["name"])
        print(doc["content"][:300])