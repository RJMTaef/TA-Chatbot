from load_docs import load_documents, split_documents
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

docs = load_documents("course_materials")
split_docs = split_documents(docs)

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(split_docs, embedding)
vectorstore.save_local("ta_vectorstore")
print("✅ Vectorstore created and saved.")
