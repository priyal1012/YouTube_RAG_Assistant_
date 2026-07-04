# 🎥 YouTube RAG Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application that enables users to chat with any YouTube video using its transcript. The application extracts the transcript from a YouTube video, converts it into semantic embeddings, stores them in a FAISS vector database, and answers user questions using Google's Gemini Large Language Model.


## 🚀 Feature

* 📺 Extract transcript from any public YouTube video
* ✂️ Split transcripts into semantic chunks
* 🧠 Generate embeddings using BAAI embedding models
* 🔍 Store and retrieve relevant context using FAISS
* 🤖 Answer questions with Google Gemini
* ⚡ Fast semantic search over long video transcripts
* 📝 Simple Streamlit-based interface


## 🏗️ Project Architecture

```
YouTube Video
      │
      ▼
YouTube Transcript API
      │
      ▼
Text Chunking
      │
      ▼
Sentence Transformer Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Relevant Context Retrieval
      │
      ▼
Google Gemini LLM
      │
      ▼
Generated Answer
```


## 🛠️ Tech Stack

| Technology             | Purpose               |
| ---------------------- | --------------------- |
| Python                 | Programming Language  |
| Streamlit              | Web Application       |
| LangChain              | RAG Pipeline          |
| FAISS                  | Vector Database       |
| Sentence Transformers  | Text Embeddings       |
| Google Gemini API      | Large Language Model  |
| YouTube Transcript API | Transcript Extraction |


## 📂 Project Structure

YouTube_RAG_Assistant/
│
├── app.py
├── Youtube_rag_using_langchain.ipynb
├── YT_chatbot.ipynb
├── .gitignore
└── README.md
```


## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/priyal1012/YouTube_RAG_Assistant_.git
cd YouTube_RAG_Assistant_


### Create a virtual environment

```bash
python -m venv venv


Activate it

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Paste a YouTube video URL.
2. The application extracts the transcript.
3. The transcript is divided into meaningful chunks.
4. Each chunk is converted into embeddings.
5. Embeddings are indexed using FAISS.
6. User questions retrieve the most relevant transcript chunks.
7. Gemini generates an answer grounded in the retrieved context.

---

## 🎯 Example Questions

* Summarize this video.
* What are the key concepts discussed?
* Explain the main idea in simple terms.
* What tools are mentioned?
* What are the important takeaways?
* Generate interview questions from this video.

---

## 📈 Future Improvements

* Support videos without transcripts using Whisper.
* Conversation memory.
* Multi-video knowledge base.
* Source citations with timestamps.
* PDF export of chat history.
* Hybrid Search (BM25 + Vector Search).
* Advanced RAG techniques (re-ranking, contextual compression).

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 👩‍💻 Author

**Priyal**

GitHub: https://github.com/priyal1012

---

## ⭐ If you found this project useful

Give this repository a ⭐ and consider sharing it with others.
