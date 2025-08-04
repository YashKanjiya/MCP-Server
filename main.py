from fastapi import FastAPI
from app.models import ChatRequest, ChatResponse
from app.chat_engine import process_message, process_travel_message

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response_text = process_message(request)
    return ChatResponse(response=response_text)

@app.post("/travel", response_model=ChatResponse)
async def travel_chat(request: ChatRequest):
    response_text = process_travel_message(request)
    return ChatResponse(response=response_text)
