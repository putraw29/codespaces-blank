import streamlit as st
import pandas as pd
import numpy as np

# Create a list to store the chat messages
messages = []

# Create a function to add a new message to the chat
def add_message(message):
    messages.append(message)

# Create a function to display the chat messages
def display_messages():
    st.write("Chat Messages")
    st.table(messages)

# Create a sidebar to select the user
st.sidebar.title("Select User")
user1 = st.sidebar.selectbox("User 1", ["User 1", "User 2"])
user2 = st.sidebar.selectbox("User 2", ["User 1", "User 2"])

# Create a button to send a message
if st.button("Send Message"):
    message = st.text_input("Message")
    add_message(f"{user1}: {message}")

# Display the chat messages
display_messages()
