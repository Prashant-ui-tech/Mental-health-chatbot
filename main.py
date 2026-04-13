from fastapi import FastAPI
from dotenv import load_dotenv
from models import ChatRequest
from chat_engine import get_response
from crises import detect_crisis, contains_crisis_keywords, SAFETY_MESSAGE
from logger import log_chat
from doc_engine import query_documents
from fastapi.middleware.cors import CORSMiddleware




load_dotenv()

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Powered Mental Health Chatbot!"}


@app.post("/chat")
def chat_with_memory(request: ChatRequest):
    session_id = request.session_id
    user_query = request.query

    # 🔹 Crisis detection (IMPROVED)
    crisis = detect_crisis(user_query)

    if crisis["is_crisis"]:
        log_chat(session_id, user_query, SAFETY_MESSAGE, True)
        return {"response": SAFETY_MESSAGE, "crisis": True}

    # 🔹 Normal response
    response = get_response(session_id, user_query)

    log_chat(session_id, user_query, response, False)

    return {"response": response, "crisis": False}


@app.post("/doc-chat")
def chat_with_documents(request: ChatRequest):
    session_id = request.session_id
    user_query = request.query

    # 🔥 ADD THIS (crisis check)
    if contains_crisis_keywords(user_query):
        log_chat(session_id, user_query, SAFETY_MESSAGE, is_crisis=True)
        return {"response": SAFETY_MESSAGE}

    # normal doc response
    response = query_documents(user_query)
    log_chat(session_id, user_query, response, is_crisis=False)
    return {"response": response}