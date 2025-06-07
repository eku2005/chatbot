import streamlit as st
from chatbot_core import ChatbotAssistant, get_stocks

if "chatbot" not in st.session_state:
    assistant = ChatbotAssistant("intents.json", function_mappings={"stocks": get_stocks})
    assistant.parse_intents()
    assistant.load_model("chatbot_model.pth", "dimensions.json")
    st.session_state.chatbot = assistant
    st.session_state.chat_history = []

st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("AI Chatbot")

for speaker, msg in st.session_state.chat_history:
    with st.chat_message(speaker):
        st.markdown(msg)

user_input = st.chat_input("Type your message...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    response = st.session_state.chatbot.process_message(user_input)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("assistant", response))