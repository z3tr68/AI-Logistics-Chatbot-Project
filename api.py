from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import re
import requests
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI()

conversation_memory = {}


# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Call ollama locally
def call_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"] 


# Load shipment data
with open("shipments.json") as f:
    shipments = json.load(f)


# Helper Functions
def find_shipment(tracking_number):
    for s in shipments:
        if s["tracking_number"].lower() == tracking_number.lower():
            return s
    return None


# API Routes
@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/shipment/{tracking_number}")
def get_shipment(tracking_number: str):
    shipment = find_shipment(tracking_number)
    if shipment:
        return shipment
    return {"error": "Shipment not found"}


@app.post("/chat")
def chat(payload: dict):
    session_id = payload.get("session_id", "default")
    message = payload.get("message","")
    
    # Init memory
    if session_id not in conversation_memory:
        conversation_memory[session_id] = []

    history = conversation_memory[session_id]

    # Try to detect tracking number in message
    tracking_match = re.search(r"TRK\d+", message.upper())
    shipment_context = ""

    if tracking_match:
        shipment = find_shipment(tracking_match.group())
        if shipment:
            shipment_context = f"""
Shipment Context:
- Status: {shipment['status']}
- Location: {shipment['current_location']}
- Destination: {shipment['destination']}
- ETA: {shipment['estimated_delivery']}
- Delay: {shipment['delay']}
- Delay reason: {shipment['delay_reason']}
"""

    prompt = f"""
You are a helpful logistics customer support assistant.

Rules:
- Be concise and friendly
- Help users track packages, answer questions, and explain delays
- If shipment context is provided, use it
- If not, respond generally and ask clarifying questions

{shipment_context}

User message: {message}

Respond clearly and helpfully.
"""
    
    reply = call_llm(prompt)
    return {"response": reply}
    

app.mount("/static", StaticFiles(directory="static", html=True), name="static")