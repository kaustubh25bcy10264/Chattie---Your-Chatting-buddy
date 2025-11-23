"""
Logger module.
This file records every conversation into chatbot.log.
"""

import logging

logging.basicConfig(
    filename="chatbot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log_interaction(user_input: str, intent: str, response: str):

    logging.info(f"User: {user_input} | Intent: {intent} | Response: {response}")
