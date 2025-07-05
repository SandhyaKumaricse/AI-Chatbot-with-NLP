import nltk
nltk.download('punkt')
nltk.download('wordnet')
import random
import string


nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()

# Sample knowledge base (which can be extended easily)
knowledge_base = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! Ask me anything.",
    "what is your purpose": "I am here to assist you with basic questions.",
    "kaise ho": 'Main theek hoon, aap kaise hain?',
    "what is your name": "I am a simple chatbot built with NLTK.",
    "what is my name": "Your name is Sandhya",
    "how are you": "I'm just code, but thanks for asking!",
    "bye": "Goodbye! Have a great day.",
    "help": "You can ask me things like 'What is your name', 'How are you', or say 'bye'."
}

# Preprocess input
def preprocess(sentence):
    sentence = sentence.lower()
    sentence = ''.join([char for char in sentence if char not in string.punctuation])
    tokens = nltk.word_tokenize(sentence)
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(lemmas)

# Generates response
def get_response(user_input):
    processed = preprocess(user_input)
    for key in knowledge_base:
        if key in processed:
            return knowledge_base[key]
    return "Sorry, I don't understand that yet."


def chat():
    print("Bot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Bot: Goodbye!")
            break
        response = get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chat()
