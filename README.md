# MCP-Server
Your AI assistant helps users plan travel based on preferences like:  Budget  Travel dates  Interests (nature, history, food)  Visa-free countries (optional)  The assistant uses OpenAI’s GPT model to respond, but keeps context via MCP to make the conversation multi-turn and personalized.

# 🧠 LLM Chat API using Meta LLaMA 3 (Groq)

A lightweight Flask API that connects to Meta’s LLaMA 3-70B model using Groq’s blazing-fast inference backend. Built for developers who want an easy local endpoint to chat with an LLM.

---

## 🚀 Features

- 🦙 Meta LLaMA 3-70B via Groq
- ⚡ Ultra-fast response time
- 🧪 REST API with Flask
- 🔐 API key management with `.env`
- 🧰 Compatible with Postman or curl

---

## 📦 Requirements

- Python 3.9+
- Groq API key from [https://console.groq.com](https://console.groq.com)

---

## 📁 Project Structure

llm-chat-api/
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 🛠 Setup

```bash
# Clone repo
git clone https://github.com/your-username/llm-chat-api.git
cd llm-chat-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
🔐 Add your Groq API key
Create a .env file:

ini
Copy
Edit
GROQ_API_KEY=your-groq-api-key-here
▶️ Run the API
bash
Copy
Edit
python app.py
Visit: http://127.0.0.1:5000

🧪 Usage
Endpoint
http
Copy
Edit
POST /chat
Content-Type: application/json
Example Request
json
Copy
Edit
{
  "session_id": "user-123",
  "message": "Hello!"
}
Example Response
json
Copy
Edit
{
  "reply": "Hello! How can I assist you today?"
}
🧪 curl Test
bash
Copy
Edit
curl -X POST http://127.0.0.1:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id":"user-123","message":"Hello"}'
📄 .gitignore
gitignore
Copy
Edit
.env
venv/
__pycache__/
*.pyc
📄 requirements.txt
txt
Copy
Edit
flask
python-dotenv
openai
📘 License
MIT License

🙌 Credits
Meta LLaMA 3

Groq API

yaml
Copy
Edit

---

Let me know if you want to add badges, Docker setup, or GitHub Actions next


