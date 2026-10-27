
import random
from datetime import datetime

responses = {
    "hello": ["Hello! How are you?", "Hi! How can I help you?"],
    "hi": ["Hi there!", "Hello! Nice to talk to you."],
    "how are you": ["I am fine! How are you?", "Doing great!"],
    "your name": ["I am Python Chatbot."],
    "help": ["You can ask me about my name, time, date, or say hello."],
    "bye": ["Goodbye! Have a great day!"]
}

print("=" * 35)
print("       PYTHON CHATBOT")
print("=" * 35)
print("Chatbot: Hello! Type 'help' to see what I can do.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("Chatbot:", random.choice(responses["bye"]))
        break

    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        print("Chatbot: Current time is", current_time)

    elif "date" in user_input:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Chatbot: Today's date is", current_date)

    else:
        found_response = False

        for keyword, replies in responses.items():
            if keyword in user_input:
                print("Chatbot:", random.choice(replies))
                found_response = True
                break

        if not found_response:
            print("Chatbot: Sorry, I don't understand. Type 'help' for options.")
