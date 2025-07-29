# 🌐 URLer

**GEN AI: URLer – A URL Analyzer with RAG + Google Gemma**

URLer is an intelligent assistant that lets you **analyze and ask questions about any webpage (URL)**. It fetches the page content, processes it using embeddings, and uses **Google's open-source Gemma LLM** to generate insightful answers.

---

## 🌐 Try It Online

🚀 **Live Demo (Powered by Google Gemma + RAG)**  
Try URLer instantly on Hugging Face Spaces:  
🔗 [https://Enoch1359-URLer.hf.space](https://Enoch1359-URLer.hf.space)

ℹ️ URLer uses:
- 🧠 Embedding model: `all-MiniLM-L6-v2`  
- 💬 LLM: [Google Gemma](https://huggingface.co/google/gemma-2b)

---

## 📦 Features

- 🌍 Analyze content from any URL
- 🔍 Retrieval-Augmented Generation (RAG)
- 🧠 Uses lightweight embeddings (`all-MiniLM-L6-v2`)
- 🤖 Powered by Google’s Gemma model for responses

---

## 🧪 Use Cases

- Summarize articles, blogs, and reports
- Ask specific questions about webpage content
- Extract structured insights from unstructured data
- Great for research, learning, or content review

---

## 🛠️ Tech Stack

- `Python `
- `Streamlit` – interactive UI
- 'unstructured' – to extract raw text from web pages (URLs)
- `SentenceTransformers` – for embedding generation
- `ChromaDB` – vector store for semantic search
- `Gemma` – Google’s open-source LLM  
- `dotenv` – for secure API key management
- `Docker` – for containerized setup

---

## ▶️ How to Run Locally

Follow these steps to run URLer locally using Docker:

### 1. Ensure these files are included:
- `app.py` – main Streamlit app
- `requirements.txt` – Python dependencies
- `Dockerfile` – for container setup
- `.env` – already included with example key
- 📸 **Screenshot** included in repo shows how embeddings are generated and serialized

### 2. Edit `.env` file

Open the `.env` file and replace the placeholder with your actual key from **OpenRouter** (or provider supporting Gemma):

```bash
OPENAI_API_KEY=your-openrouter-key-here
