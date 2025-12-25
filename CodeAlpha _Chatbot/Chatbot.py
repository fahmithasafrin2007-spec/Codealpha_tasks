# Task 4: Advanced Rule-Based Chatbot

def chatbot_response(user_input):
    """Return chatbot response based on user input."""
    user_input = user_input.lower()  # Convert input to lowercase

    # Greetings
    if user_input in ["hello", "hi", "hey", "hiya"]:
        return "Hello! How can I help you today?"
    
    # Asking about well-being
    elif user_input in ["how are you", "how are you?", "how do you do"]:
        return "I'm doing great! How about you?"
    elif user_input in ["i am fine", "i am good", "i am okay"]:
        return "That's good to hear!"
    
    # Farewells
    elif user_input in ["bye", "goodbye", "see you", "exit"]:
        return "Goodbye! Have a wonderful day!"
    
    # Asking name / identity
    elif user_input in ["what is your name", "who are you", "your name?"]:
        return "I'm ChatBuddy, your friendly chatbot for this internship!"
    
    # Asking age or creation
    elif user_input in ["how old are you", "your age"]:
        return "I don't have an age like humans, but I was created recently!"
    elif user_input in ["when were you created", "creation date"]:
        return "I was created for this internship task, just for you!"
    
    # Simple knowledge questions
    elif user_input in ["what is python", "define python"]:
        return "Python is a popular programming language used for web, software, AI, and more."
    elif user_input in ["what is ai", "define ai", "ai meaning"]:
        return "AI stands for Artificial Intelligence. It allows machines to mimic human intelligence."
  
    # Default response
    else:
        return "Sorry, I didn't understand that. Can you try asking differently?"

def run_chatbot():
    """Run the chatbot in a loop until the user says 'bye'."""
    print("=== Welcome to ChatBuddy ===")
    print("You can type 'bye' to exit the chat.\n")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        
        if user_input.lower() in ["bye", "goodbye", "see you", "exit"]:
            break

# Start the chatbot
run_chatbot()
