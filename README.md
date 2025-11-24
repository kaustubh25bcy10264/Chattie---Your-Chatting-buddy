# Chattie - Your chatting buddy
## 📌 Project Title
Pre-trained NLP Chatbot using spaCy
## 📖 Overview of the Project
This project is a simple yet modular chatbot built with Python.  
It uses **spaCy’s pre-trained NLP model** to detect user intent and respond accordingly.  
The chatbot demonstrates how Natural Language Processing (NLP) can be applied to conversational systems without the need for custom training.  

The project is designed to be **academic-friendly**: easy to run, well-documented, and extensible for future improvements.
---
## ✨ Features
- Responds to greetings, gives farewell, says thanks, and help requests  
- Provides current time and date dynamically  
- Tells random jokes and fun facts if asked  
- Performs simple math calculations safely  
- Explains academic concepts like Artificial Intelligence  
- Weather placeholder (can be extended with an API)  
- Logs all conversations for audit and analysis  
---
## 🛠 Technologies / Tools Used
- **Python 3.8+**  
- **spaCy (en_core_web_sm model)** for NLP intent detection  
- **Logging module** for conversation tracking  
- **Regex + AST** for safe math evaluation  
- **Modular file structure** (main, intents, responses, utils, logger)  
---
## ⚙️ Steps to Install & Run the Project
1. **Clone or download** this project folder.  
2. Make sure you have Python installed (3.8 or higher is recommended).  
3. Install necessary dependencies:
   ```bash
   python -m pip install spacy
   python -m spacy download en_core_web_sm
4. Run the chatbot:
   ```bash
    python main.py
   
## 🧪 Instructions for Testing
1. Start the chatbot by running main.py.
2. Try typing different inputs:
    * “Hello” → Bot greets you
	 * “Bye” → Bot gives farewell to you
	 * “Tell me a joke” → Bot gives a random joke to you
	 * “What is 5+7?” → Bot calculates and gives answer
	 * “Explain AI” → Bot gives an academic definition
3. All interactions are saved in chatbot.log for review.
