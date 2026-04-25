# AI Logistics Customer Support Chatbot

A full-stack generative AI chatbot that simulates a logistics customer support system. The application allows users to interact with an AI assistant in a ChatGPT-style interface to track shipments, ask questions, and receive contextual responses based on shipment data.

---

## Features

- ChatGPT-style web interface (real-time messaging)
- Shipment tracking using mock logistics database (`shipments.json`)
- AI-powered responses using a local LLM (Ollama) 
- Context-aware chatbot that understands user queries
- Full-stack architecture (FastAPI backend + HTML/CSS/JS frontend)
- Conversation memory for multi-turn dialogue
- Lightweight and runs locally

---

## Project Structure
```
ai-logistics-chatbot/
│
├── api.py # FastAPI backend
├── shipments.json # Mock logistics database
├── requirements.txt # Python dependencies
│
├── static/
│ └── index.html # Chat UI frontend
│
└── README.md
```
---

## Tech Stack

- **Backend:** FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **AI Model:** Ollama (Mistral)
- **Data:** JSON-based mock shipment database

---

## How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/AI-Logistics-Chatbot-Project.git
cd AI-Logistics-Chatbot-Project
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run the backend server
```
python -m uvicorn api:app --reload
```

### 4. Open the application

Go to:
```
http://127.0.0.1:8000
```

## 5. AI Setup

Install Ollama: https://ollama.com

Then run:

```
ollama run minstral
```

The backend will connect to the local model automatically.

## System Architecture

User → Web UI → FastAPI Backend → LLM (Ollama/OpenAI) → Response → UI

## Project Purpose

This project was built for CIS 3100 - Generative AI

