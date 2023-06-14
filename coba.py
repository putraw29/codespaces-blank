import streamlit as st
from streamlit_chat import message
from streamlit_extras.storage import file_state

# Set the page title
st.set_page_config(page_title='Chat App')

# Create a sidebar with some information about the chat app
with st.sidebar:
  st.title('Chat App')
  st.text('This is a chat app that allows two people to chat with each other. All messages are saved for an unlimited amount of time.')

# Create a chatbox where users can type their messages
chatbox = st.text_input('Type your message here:')

# Send the message to the other user
if chatbox:
  message(chatbox)

# Display the chat history
messages = file_state.get('messages', [])
st.markdown(messages)
