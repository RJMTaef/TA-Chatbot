from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from transformers import pipeline

def load_vectorstore():
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local("ta_vectorstore", embedder)

def load_llm():
    pipe = pipeline(
        "text-generation",
        model="distilgpt2",
        device=-1,              # -1 = force CPU, no CUDA check
        max_new_tokens=256,
        do_sample=True,
        temperature=0.4
    )
    return HuggingFacePipeline(pipeline=pipe)

def build_qa_chain():
    vs = load_vectorstore()
    llm = load_llm()
    return RetrievalQA.from_chain_type(llm=llm, retriever=vs.as_retriever(), chain_type="stuff")
