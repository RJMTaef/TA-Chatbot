import streamlit as st
from ta_chatbot import build_qa_chain

st.set_page_config(page_title="TA Assistant ChatBot", layout="wide")
st.title("📚 TA Assistant ChatBot")

qa = build_qa_chain()

query = st.text_input("Ask a question about your course:")
if query:
    with st.spinner("Thinking..."):
        result = qa.run(query)
        st.success("Answer:")
        st.write(result)
