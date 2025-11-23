from intents import get_intent
from responses import get_response
from logger import log_interaction

def chatbot():
    print("Hey there! I am your friend, Chattie, the chatting buddy. How you doing? wanna have a small chitchat? Type 'exit' or 'quit' if you want to stop.")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Chattie: See you! Bye for now buddy! I will be waiting here for you, whenever you felt like you wanna talk, remember that your buddy is here waiting for you, always! Hope you enjoyed our chat...")
            break

        intent = get_intent(user_input)

        response = get_response(intent, user_input)

        log_interaction(user_input, intent, response)

        print("Chattie:", response)

if __name__ == "__main__":
    chatbot()
