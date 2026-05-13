import re

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    responses = {
        r"\b(1|hello|hi|hey)\b": "Hello! Welcome to RedBus. How can I assist you today?",
        r"\b(2|how are you)\b": "I'm doing great! I'm here to help you book your bus tickets.",
        r"\b(3|book ticket|bus booking|book bus)\b": "Sure! Please provide your departure and destination cities.",
        r"\b(4|cancel ticket|cancellation)\b": "You can cancel your ticket from 'My Bookings' section. Need help with it?",
        r"\b(5|refund status|refund)\b": "Refunds are processed within 5-7 working days after cancellation.",
        r"\b(6|available buses|search buses)\b": "Please provide your source, destination, and date of journey.",
        r"\b(7|ticket price|fare)\b": "Ticket prices vary by route and bus type. Please specify your route.",
        r"\b(8|offers|discounts)\b": "We have exciting discounts! Use code 'BUS10' to get 10% off on your first booking.",
        r"\b(9|payment options|payment methods)\b": "We accept UPI, credit/debit cards, net banking, and wallets.",
        r"\b(10|bus timings|departure time)\b": "Please tell me the route so I can share available timings.",
        r"\b(11|customer care|support)\b": "You can contact our customer care at 1800-123-1234.",
        r"\b(12|track bus|live location)\b": "Tracking is available 1 hour before the scheduled departure.",
        r"\b(13|luggage policy|baggage)\b": "Most buses allow up to 15kg of luggage per passenger.",
        r"\b(14|sleeper bus|ac bus|non ac bus)\b": "Yes, we have AC, Non-AC, Sleeper, and Semi-Sleeper buses.",
        r"\b(15|rating|reviews)\b": "You can check bus ratings and customer reviews before booking.",
        r"\b(16|reschedule ticket|change journey)\b": "Some buses allow rescheduling. Would you like me to check?",
        r"\b(17|popular routes)\b": "Popular routes include Mumbai-Pune, Bangalore-Chennai, Delhi-Jaipur.",
        r"\b(18|bus operator|travel agency)\b": "We partner with top operators like VRL, SRS, KSRTC.",
        r"\b(19|bye|exit)\b": "Goodbye! Safe travels!"
    }

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    return "I'm sorry, I couldn't understand that. Please ask about RedBus services."


# Chatbot loop
print("Welcome to the RedBus Chatbot! Type 'exit' to end the conversation.")

while True:
    user_message = input("You: ")

    if user_message.lower() in ["bye", "exit"]:
        print("Chatbot: Goodbye! Safe travels!")
        break

    response = chatbot_response(user_message)
    print("Chatbot:", response)





# ============================================================
# Chatbot System (Rule-Based Chatbot)
# ============================================================

# This is a Rule-Based Chatbot.
# It gives replies based on predefined rules.

# Main Concepts Used:
# 1. Chatbot
# 2. Rule-Based AI
# 3. Regular Expressions (re)
# 4. Dictionary
# 5. Functions
# 6. Looping

# Main Working:
# User Input
# → Pattern Matching
# → Response Generation

# re module:
# Used for Regular Expression
# and pattern matching.

# lower():
# Converts input into lowercase.

# strip():
# Removes extra spaces.

# Dictionary:
# Stores chatbot patterns and responses.

# while True:
# Creates continuous conversation loop.

# Advantages:
# - Fast responses
# - Easy implementation
# - User friendly

# Limitations:
# - No self-learning
# - Fixed responses only

# Time Complexity : O(N)
# Space Complexity : O(N)

# Where:
# N = Number of chatbot patterns


#2. Which module is used?
#   ANS -> re  (Regular Expression)

#3. What is regex?
#Regex means:
#Regular Expression
#Used for pattern matching.

#5. Why use dictionary?
#To store:
#    -patterns
#    -responses
#efficiently.

# ============================================================