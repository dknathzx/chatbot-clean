# The rules — you can add as many as you want!
rules = {
    "hi": "Hey! How can I help you?",
    "hello": "Hello! What can I do for you?",
    "how are you": "I'm doing great! I'm your personal bot.",
    "what is your name": "I'm your personal chatbot, built by you!",
    "joke": "Why do programmers hate nature? It has too many bugs!",
    "bye": "Goodbye! Have a great day!",
    "help": "You can say: hi, joke, time, bye",
}

def get_response(user_input):
    cleaned = user_input.lower().strip()

    # Check time
    if "time" in cleaned:
        import datetime
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."

    # Match rules
    for pattern, response in rules.items():
        if pattern in cleaned:
            return response

    # Default
    return "I don't understand that yet. Type 'help' to see what I can do."