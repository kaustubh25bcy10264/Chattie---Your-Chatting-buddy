import spacy
from utils import clean_text, contains_math_expression

nlp = spacy.load("en_core_web_sm")

def get_intent(user_input: str) -> str:

    text = clean_text(user_input)
    _ = nlp(text)

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "greeting"
    
    if any(word in text for word in ["bye", "goodbye", "later"]):
        return "farewell"
    
    if "help" in text or "assist" in text:
        return "help"
    
    if "thank" in text or "thanks" in text:
        return "thanks"
    
    if "weather" in text:
        return "weather"
    
    if "time" in text or "date" in text:
        return "time"
    
    if "joke" in text:
        return "joke"
    
    if "fact" in text:
        return "fact"
    
    if contains_math_expression(text):
        return "calculator"
    
    if "ai" in text or "artificial intelligence" in text:
        return "academic"

    return "unknown"
