qa_pairs = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi! Nice to meet you.",
    "what is your name": "I am a basic chatbot built with FastAPI.",
    "how are you": "I am doing well. Thanks for asking.",
    "what can you do": "I can answer a fixed set of questions.",
    "who created you": "I was created as a demo project for students.",
    "what is python": "Python is a popular programming language used for web development, AI, data science, and more.",
    "what is fastapi": "FastAPI is a modern Python framework for building APIs quickly.",
    "bye": "Goodbye! Have a great day.",
    "thank you": "You are welcome!"
}


def get_bot_response(user_message: str) -> str:
    cleaned_message = user_message.strip().lower()

    if cleaned_message in qa_pairs:
        return qa_pairs[cleaned_message]

    return "Sorry, I only understand a fixed set of questions."