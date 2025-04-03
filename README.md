# 🎓 TA Assistant ChatBot
An **LLM-powered assistant** that answers questions based on course materials like lecture slides and syllabi using **LangChain**, **FAISS**, and **Streamlit**.

## 💡 Features
- Ask natural-language questions about your course
- Uses PDF lecture notes as knowledge base
- Powered by open-source LLMs like Phi-2 or Mistral
- Built with LangChain + FAISS + HuggingFace
- Easy to run locally or deploy on cloud (AWS/GCP)

## 🚀 Demo
![Demo Screenshot](./screenshot.png)

## 🧰 Tech Stack
| Layer         | Tool                                      |
|---------------|-------------------------------------------|
| Embeddings    | `sentence-transformers/all-MiniLM-L6-v2`  |
| Vector DB     | FAISS                                     |
| LLM           | Phi-2 or Mistral via HuggingFace          |
| Framework     | LangChain                                 |
| Frontend      | Streamlit                                 |
| Hosting       | AWS EC2 / GCP Cloud Run                   |

## 📦 Installation
```bash
git clone https://github.com/your-username/ta-assistant-chatbot
cd ta-assistant-chatbot
pip install -r requirements.txt
```

## 📄 Usage
1. Put your course PDFs into `./course_materials/`
2. Embed them into FAISS:
   ```bash
   python create_vectorstore.py
   ```
3. Start the chatbot:
   ```bash
   streamlit run app.py
   ```

## 🌐 Deployment (Optional)
```bash
docker build -t ta-assistant .
docker run -p 8501:8501 ta-assistant
```

## 🧠 Future Ideas
- Add user chat history
- Allow uploading new PDFs live
- Use larger models or APIs (e.g., OpenAI)

## 📜 License
MIT License
