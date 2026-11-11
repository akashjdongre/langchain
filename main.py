from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
import streamlit as st

llm = init_chat_model("claude-sonnet-4-6")

st.title("LangChain Chatbot with Streamlit")
st.markdown("This is a simple chatbot application built using LangChain and Streamlit. You can ask questions and get responses from the chatbot.")

if "message" not in st.session_state:
    st.session_state.message = []

for message in st.session_state.message:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask A Question")

if query:
    st.session_state.message.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    query_result = llm.invoke(query)
    st.chat_message("bot").markdown(query_result.content)
    st.session_state.message.append({"role": "bot", "content": query_result.content})

