"""
Response module.
This file is storing everything what the Chatbot should say for each intent.
Some replies of Chatbot Chattie- the chatting buddy, are fixed, while some? are dynamic (like time, jokes, calculator etc etc).
"""

import datetime
import random
from utils import evaluate_expression_safely

def get_response(intent: str, user_input: str = "") -> str:

    if intent == "greeting":
        return "Hello 👋! Nice to meet you."
    
    if intent == "farewell":
        return "Goodbye! Keep coding and learning 🚀"
    
    if intent == "help":
        return "Sure—tell me what you need help with."
    
    if intent == "thanks":
        return "You're welcome! Happy to support."
    
    if intent == "weather":
        return "I can’t fetch live weather yet, but let’s imagine it’s sunny ☀️."
    
    if intent == "time":
        now = datetime.datetime.now()
        return f"⏰ Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}."
    
    if intent == "joke":
        return random.choice([
            "Why don’t programmers like nature? Too many bugs 🐛.",
            "I told my computer I needed a break, and it said: ‘Going to sleep.’ 😴"
        ])
    
    if intent == "fact":
        return random.choice([
            "Did you know? The first chatbot, ELIZA, was built in the 1960s.",
            "Fun fact: The term ‘Artificial Intelligence’ was coined in 1956."
        ])
    
    if intent == "calculator":
        result = evaluate_expression_safely(user_input)
        return result if isinstance(result, str) else f"Answer: {result}"
    
    if intent == "academic":
        return ("Artificial Intelligence is about making machines smart enough to do tasks "
                "that usually need human intelligence. In this chatbot, we use spaCy NLP "
                "to detect intent and respond accordingly.")
    
    return "Hmm 🤔, I didn’t quite get that. Could you just rephrase that for me?"
