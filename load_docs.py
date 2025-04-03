from pathlib import Path
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents(folder_path):
    docs = []
    for pdf_path in Path(folder_path).glob("*.pdf"):
        loader = PyPDFLoader(str(pdf_path))
        pages = loader.load()
        docs.extend(pages)
    return docs

def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(docs)
