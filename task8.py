# Simple rule-based chatbot using if-else

def chatbot():
    print("Hello! I'm ChatBot. Type 'exit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == "exit":
            print("ChatBot: Goodbye! Have a nice day.")
            break
        
        elif "hello" in user_input or "hi" in user_input:
            print("ChatBot: Hello there! How can I help you today?")
        
        elif "your name" in user_input:
            print("ChatBot: I'm just a simple chatbot built using Python.")
        
        elif "how are you" in user_input:
            print("ChatBot: I'm just code, but thanks for asking!")
        
        elif "weather" in user_input:
            print("ChatBot: I can't check real-time weather yet, but it's always sunny in here!")
        
        elif "help" in user_input:
            print("ChatBot: Sure! You can ask me about my name, how I am, or say hello.")
        
        elif "bye" in user_input:
            print("ChatBot: Bye! Talk to you later.")
            break

        elif "joke" in user_input:
         print("ChatBot: Why did the programmer quit his job? Because he didn't get arrays.")


        elif "joke" in user_input:
            print("ChatBot: Why don’t scientists trust atoms? Because they make up everything!")

        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%I:%M %p")
            print(f"ChatBot: The current time is {current_time}.")

        elif "date" in user_input:
            from datetime import datetime
            current_date = datetime.now().strftime("%B %d, %Y")
            print(f"ChatBot: Today's date is {current_date}.")

        elif "who made you" in user_input or "who created you" in user_input:
            print("ChatBot: I was created by a Python enthusiast!")

        elif "thanks" in user_input or "thank you" in user_input:
            print("ChatBot: You're welcome!")

        elif "what can you do" in user_input:
            print("ChatBot: I can tell jokes, give the time and date, and answer simple questions!")

        elif "motivate me" in user_input or "motivation" in user_input:
            print("ChatBot: You are capable of amazing things. Just keep going!")

        elif "bye" in user_input:
            print("ChatBot: Bye! Talk to you later.")
            break


        
    
        else:
            print("ChatBot: Sorry, I don't understand that. Try asking something else.")

# Run the chatbot
chatbot()
