def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user = input("You: ").lower()
        if user in ["hello", "hi", "hey"]:
            print("Chatbot: Hi there! How can I help you?")
        elif user in ["how are you", "how r u", "how's it going"]:
            print("Chatbot: I'm doing great, thanks for asking! How about you?")
        elif user in ["i am fine", "i'm good", "fine"]:
            print("Chatbot: Glad to hear that!")
        elif user in ["what is your name", "who are you"]:
            print("Chatbot: I'm a simple chatbot created in Python.")
        elif user in ["what can you do", "help"]:
            print("Chatbot: I can chat with you and answer simple questions.")
        elif user in ["bye", "goodbye", "see you"]:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: Hmm, I don't understand that yet.")

chatbot()
