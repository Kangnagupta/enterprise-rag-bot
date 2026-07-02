# 🤖 Enterprise RAG IT Helpdesk Bot

A custom Retrieval-Augmented Generation (RAG) AI chatbot built to act as an automated IT Helpdesk assistant. The bot leverages an open-source Large Language Model (TinyLlama) and a vector database (ChromaDB) to answer employee IT questions strictly based on internal company documentation. 

The application is fully containerized with Docker and deployed live on AWS ECS (Fargate) for scalable, serverless hosting.

### 🔴 Live Demo
**Try the live bot here:** [http://13.127.157.101:8501](http://13.127.157.101:8501)
*(Note: Please allow 15-20 seconds on the first load for the AI model to initialize into the server's active memory).*

### 🛠️ Tech Stack
* **Frontend:** Streamlit (Python)
* **AI Model:** TinyLlama-1.1B-Chat (via Hugging Face Transformers)
* **Vector Database:** ChromaDB
* **Containerization:** Docker
* **Cloud Infrastructure:** Amazon Web Services (AWS ECS & ECR)
* **Compute:** AWS Fargate (Serverless container execution)

### ✨ Key Features
* **Document-Grounded Memory:** Answers are generated exclusively from the provided IT documentation.
* **Fallback Logic:** Politely declines to answer questions outside the scope of its database to prevent AI hallucinations.
* **Resource Optimization:** Uses `@st.cache_resource` to load the 1.1 Billion parameter AI model only once upon server boot, preventing memory crashes and reducing latency on AWS.