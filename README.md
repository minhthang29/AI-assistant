# OptiBot – AI Documentation Assistant (RAG)

## Overview
OptiBot is a documentation-based AI assistant built using (OpenAI Assistants API + Vector Store).  
The assistant answers questions strictly based on provided documentation, ensuring accurate and non-hallucinated responses.
This project demonstrates a complete Retrieval-Augmented Generation (RAG) pipeline without frontend code.

## Key Features
- Documentation scraping & preprocessing
- Markdown-based knowledge storage
- OpenAI Vector Store for semantic search
- Assistant configured via Playground (no UI code)
- Answers grounded in source documents only

## Tech Stack
- Python 3.11
- OpenAI Assistants API
- Vector Store (File Search)
- Docker
- Markdown

## Project Structure
```text
project-bot/
├── scraper/
│   ├── fetch_articles.py        # Scrape help articles from documentation
│   └── convert_markdown.py      # Convert HTML to Markdown and store source URL
│
├── uploader/
│   └── upload_vector_store.py   # Create vector store and upload markdown files
│
├── data/
│   └── markdown/                # Generated markdown documentation
│
├── main.py                      # Entry point (runs once and exits)
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Dockerized execution
├── .env.sample                  # Environment variable template
└── README.md                    # Project documentation
```

## How It Works
1. Scrape documentation content
2. Convert content to Markdown files
3. Upload Markdown files to an OpenAI Vector Store
4. Attach Vector Store to an Assistant
5. Assistant answers questions using document retrieval

## Assistant Behavior
- Uses only uploaded documents
- Returns structured bullet-point answers
- Refuses to answer if information is not found
- Optionally cites article URLs

## Setup (Quick)
Setup – how to run locally and docker
```bash
pip install -r requirements.txt
python main.py

docker build -t optibot .
docker run --env-file .env optibot
