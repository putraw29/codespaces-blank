import streamlit as st
import random
import transformers

# Set the title of the page
st.title("Streamlit AI Chatbot")

# Initialize the chatbot
model = transformers.AutoModelForSeq2SeqLM.from_pretrained("distilbert-base-uncased")

# Function for generating a bot response
def get_bot_response(user_input):
    bot_response = model.generate(
        text=user_input,
        max_length=128,
        temperature=0.7,
        top_k=5,
        do_sample=True,
    )
    return bot_response

# Display the chat history
for message in chat_history:
    st.write(message)

# Get the user's input
user_input = st.text_input("Your input:")

# Add the user's input to the chat history
chat_history.append(f"User: {user_input}")

# Generate a bot response
bot_response = get_bot_response(user_input)

# Display the bot's response
st.write(f"Bot: {bot_response}")
