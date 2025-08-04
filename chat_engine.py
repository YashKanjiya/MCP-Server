from app.context_store import get_context, update_context
from app.models import ChatRequest
import os
import openai

openai.api_key = os.getenv("GROQ_API_KEY")

def call_gpt(prompt: list) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt
    )
    return response['choices'][0]['message']['content']

def process_message(request: ChatRequest) -> str:
    session_id = request.session_id
    query = request.query

    history = get_context(session_id)
    history.append({"role": "user", "content": query})
    
    response = call_gpt(history)
    
    history.append({"role": "assistant", "content": response})
    update_context(session_id, history)
    
    return response

def process_travel_message(request: ChatRequest) -> str:
    session_id = request.session_id
    query = request.query

    history = get_context(session_id)

    if not history:
        # Start with a system message that biases the assistant toward travel advice
        history.append({
            "role": "system",
            "content": "You are a helpful travel assistant. Answer questions related to travel, tourism, weather, destinations, and trip planning in detail."
        })

    history.append({"role": "user", "content": query})
    
    response = call_gpt(history)
    
    history.append({"role": "assistant", "content": response})
    update_context(session_id, history)

    return response
