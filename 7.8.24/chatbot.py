def chatbot():
    responses = {
        "hi": "Hello! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!"
    }

    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("Bot:", responses[user_input])
        else:
            print("Bot: I'm sorry, I don't understand that.")
        if user_input == "bye":
            break

chatbot()
