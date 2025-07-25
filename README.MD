# wiki-rag

A Python-based Retrieval-Augmented Generation (RAG) pipeline using Wikipedia as the knowledge base. This project demonstrates how to fetch, preprocess, embed, store, and query Wikipedia content to enhance the capabilities of a large language model (LLM).

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) 
![FastAPI](https://img.shields.io/badge/FastAPI-async--framework-teal) 
![FAISS](https://img.shields.io/badge/FAISS-vector%20store-purple) 
![OpenAI](https://img.shields.io/badge/OpenAI-embeddings-lightgrey) 
![Gemini](https://img.shields.io/badge/Gemini-LLM-yellow) 
![Wikipedia](https://img.shields.io/badge/Wikipedia-API-black)
---

## 🧩 Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Directory Structure](#directory-structure)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Configuration](#configuration)
* [Usage](#usage)
* [Examples](#examples)
* [Contributing](#contributing)
* [Roadmap](#roadmap)
* [License](#license)

---

## Project Overview

`wiki-rag` is a modular pipeline designed to:

1. **Fetch** relevant Wikipedia articles via the MediaWiki API.
2. **Preprocess** and chunk text for efficient embedding and retrieval.
3. **Embed** content using your choice of embedding model (e.g., OpenAI embeddings).
4. **Index** embeddings into a FAISS vector store for similarity search.
5. **Query** the vector store and feed results into a Gemini-based LLM agent for concise, context-aware answers.

This setup enables a lightweight, production‑ready RAG system using open, freely available wiki data.

---

## Features

* 🔍 **Wikipedia Fetcher**: Interface with the MediaWiki API to retrieve pages, categories, or search results.
* 🔧 **Text Preprocessor**: Clean, split, and organize raw text into chunks suitable for embedding.
* 🔢 **Embeddings Module**: Plug in any embedding provider (default: OpenAI).
* 💾 **FAISS Vector Store**: Fast, on-disk or in-memory vector indexing and similarity search.
* 🤖 **LLM Agent**: Use Google Gemini (or another LLM) to generate synthesized responses based on retrieved context.
* ⚙️ **Configurable**: Environment-driven settings for API keys, database URLs, chunk sizes, and more.

---

## Directory Structure

```
wiki-rag/
├── database/            # Database connection and utilities
├── embedder/            # Embedding generation scripts
├── faiss_processor/     # FAISS index building and querying
├── gemini_agent/        # LLM agent orchestration
├── preprocessor/        # Text cleaning, chunking, and metadata
├── warehouse/           # Raw data storage (e.g., local cache of articles)
├── wikipedia_api/       # MediaWiki API wrappers
├── main.py              # Entry point: orchestrates end-to-end pipeline or exposes API
├── requirements.txt     # Python dependencies
└── .gitignore           # Files and directories to ignore
```

---

## Prerequisites

* **Python** ≥ 3.8
* **pip** or **poetry**
* **API Keys**:

  * `OPENAI_API_KEY` (for embeddings)
  * `GEMINI_API_KEY` (for LLM queries)

---

## Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/xreedev/wiki-rag.git
   cd wiki-rag
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

Create a `.env` file in the root directory (and ensure it is in `.gitignore`):

```env
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
# Optional overrides
WIKI_API_URL=https://en.wikipedia.org/w/api.php
EMBED_MODEL=text-embedding-ada-002
CHUNK_SIZE=500
VECTOR_STORE_PATH=./faiss_index
```

---

## Usage

Run the pipeline end-to-end:

```bash
python main.py \
  --query "Evolution of quantum computing" \
  --top_k 5 \
  --source wiki
```

Or start an API server (if implemented in `main.py`):

```bash
uvicorn main:app --reload
```

---

## Examples

1. **Local Search**:

   ```bash
   python main.py --query "Python concurrency" --mode local
   ```
2. **Server Mode**:

   ```bash
   curl \
     -X POST http://localhost:8000/ask \
     -H "Content-Type: application/json" \
     -d '{"question": "What is RAG?"}'
   ```

---

## Contributing

1. Fork the repo.
2. Create a feature branch: `git checkout -b feature/awesome`
3. Commit your changes: `git commit -m "Add awesome feature"`
4. Push: `git push origin feature/awesome`
5. Open a pull request.

Please open issues for bugs or feature requests.

---

## Roadmap

* [ ] Add Docker support for easy deployment
* [ ] Implement automated tests (pytest)
* [ ] CI/CD pipeline (GitHub Actions)
* [ ] Support multi-language wiki sources
* [ ] Real-time streaming responses from LLM

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
