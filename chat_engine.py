from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage


# LLM (FREE)
llm = ChatOllama(
    model="phi",
    temperature=0.7,
    request_timeout=120.0,
    max_tokens=150
)

# Session memory
session_memory_map = {}

def get_response(session_id: str, user_query: str) -> str:
    
    # Initialize memory
    if session_id not in session_memory_map:
        session_memory_map[session_id] = []

    # Crisis detection
    crisis_keywords = ["suicide", "kill myself", "die", "end my life"]
    is_crisis = any(word in user_query.lower() for word in crisis_keywords)

    if is_crisis:
        return "I'm really sorry you're feeling this way. Please talk to someone you trust like your parents, a close friend, or a counselor. You are not alone ❤️"

    # Add user message
    session_memory_map[session_id].append(HumanMessage(content=user_query))

    # Get response
    response = llm.invoke(session_memory_map[session_id])

    # Save AI response
    session_memory_map[session_id].append(AIMessage(content=response.content))

    return response.content