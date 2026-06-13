import streamlit as st
from langchain_community.chat_models import ChatOllama

# create model
chat = ChatOllama(model="llama3")

# title
st.title("AI Chatbot")

# store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# input at bottom
user_input = st.chat_input("Type your message")

if user_input:
    # store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # get response
    response = chat.invoke(st.session_state.messages)
    bot_reply = response.content

    # store bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })

    with st.chat_message("assistant"):
        st.write(bot_reply)