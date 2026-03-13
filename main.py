from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import ChatRequest, ChatResponse
from llm_service import get_llm_response
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    user_message = request.message.lower()

    # Handle date/time locally
    if "time" in user_message:
        current_time = datetime.now().strftime("%H:%M:%S")
        reply = f"The current time is {current_time}."

    elif "date" in user_message or "today" in user_message:
        today = datetime.now().strftime("%Y-%m-%d")
        reply = f"Today's date is {today}."

    else:
        # fallback to LLM
        reply = get_llm_response(request.message)

    return ChatResponse(
        user_message=request.message,
        bot_response=reply
    )