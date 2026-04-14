# 🧠 AstraRAG — Agentic AI Science Tutor

AstraRAG is an **agentic Retrieval-Augmented Generation (RAG) system** designed as a science learning assistant that answers questions grounded in **Class 12 Biology textbooks**, with plans to extend into Physics and Chemistry as a full AI science tutor.

It combines **tool-using agents, vector search, and explainable retrieval** to generate context-aware, source-grounded responses.

---

## 🚀 Key Features

- 🧩 Agentic AI workflow using CrewAI
- 📚 Retrieval-Augmented Generation (RAG) over textbook knowledge
- 🔍 Vector search with ChromaDB
- 🤖 Multi-step reasoning with tool usage (retrieval + synthesis)
- 🧠 Source-grounded answers with transparency
- 💬 Real-time chat interface (Streamlit)
- ⚙️ Backend API using FastAPI
- 🐳 Fully containerized with Docker
- ☁️ Deployed on AWS EC2 for production inference

---

## 🏗️ System Architecture

User Query  
→ Streamlit Frontend  
→ FastAPI Backend  
→ Agentic Crew (Planner + QA Agent)  
→ RAG Tool (ChromaDB Vector Search)  
→ LLM Reasoning Layer  
→ Final Answer + Sources  

---

## 📊 Screenshots

### 🔹 Chat Interface QA
![Chat UI](imgs/img1)

### 🔹 Follow-up
![RAG Output](imgs/img2)

---

## 🧠 How It Works

1. **Document Ingestion**
   - Class 12 Biology textbook is chunked and embedded
   - Stored in ChromaDB vector database

2. **Query Processing**
   - User query is passed to an agentic QA system
   - Agent decides when to use retrieval tools

3. **Retrieval-Augmented Generation**
   - Relevant textbook chunks are retrieved
   - LLM synthesizes answer grounded in retrieved context

4. **Response Generation**
   - Final answer includes:
     - Explanation
     - Sources used
     - Tool usage transparency

---

## 🛠️ Tech Stack

- **LLMs & Agents:** CrewAI, Groq LLMs
- **RAG Framework:** LlamaIndex
- **Vector DB:** ChromaDB
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Containerization:** Docker
- **Deployment:** AWS EC2
- **Embeddings:** HuggingFace Transformers
