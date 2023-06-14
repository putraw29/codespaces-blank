import streamlit as st
import pandas as pd
import numpy as np

# Create a data frame to store the chat messages
messages = pd.DataFrame(columns=["sender", "message"])

# Create a function to add a new message to the data frame
def add_message(sender, message):
    messages = messages.append({"sender": sender, "message": message}, ignore_index=True)

# Create a function to display the chat messages
def display_messages():
    st.table(messages)

# Create a function to start a new chat conversation
def start_chat():
    sender = st.text_input("Enter your name:")
    message = st.text_input("Enter your message:")
    add_message(sender, message)
    display_messages()

# Start the chat app
st.title("Chat App")
st.write("This is a chat app where you can chat with another person.")
st.button("Start Chat")

if st.button("Start Chat"):
    start_chat()
