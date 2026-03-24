import os
from dotenv import load_dotenv

from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

DB_PATH = "faiss_index"


def initialize_vector_db():
    # Load document
    loader = Docx2txtLoader("Mrignayanee Chat Bot Data.docx")
    documents = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    docs = splitter.split_documents(documents)

    # Load embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load or create FAISS DB
    if os.path.exists(DB_PATH):
        vector_db = FAISS.load_local(
            DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
    else:
        vector_db = FAISS.from_documents(docs, embeddings)
        vector_db.save_local(DB_PATH)

    return vector_db


def get_context(vector_db, query):
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])
    return context