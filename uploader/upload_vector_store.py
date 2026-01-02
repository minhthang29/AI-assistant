import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

VECTOR_STORE_NAME = "optisigns_support_docs"

def create_vector_store():
    return client.vector_stores.create(name=VECTOR_STORE_NAME)


def upload_file(vector_store_id, file_path):
    file = client.files.create(
        file=open(file_path, "rb"),
        purpose="assistants"
    )

    client.vector_stores.files.create(
        vector_store_id=vector_store_id,
        file_id=file.id
    )
