import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    base_url="https://api.cow.rip/api/v1",
    api_key="sk-quardo-NSbNs8ah8s9tP6NZCuYVNPNPIuBEllEWjD9z3yeB2TTtH47O"
)

# Set page title
st.set_page_config(page_title="Streamlit Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response from OpenAI
    response = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[{"role": "user", "content": prompt}],
    )
    bot_reply = response.choices[0].message.content

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
