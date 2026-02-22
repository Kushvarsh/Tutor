import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Maths Tutor",
    page_icon="📚",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stChatMessage {
            border-radius: 15px;
            padding: 10px;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #2E86C1;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: gray;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">📚 AI Mathematics Tutor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask any maths question (Answers in max 5 lines)</div>', unsafe_allow_html=True)

# Initialize LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.8
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="""You are a Mathematics Tutor.
        Solve the question step-by-step in maximum 5 lines only.
        Use clear mathematical steps.
        Write only the solution and final answer.
        No extra explanation.""")
    ]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your maths question here... (Type 'exit' to stop)")

if user_input:

    # If user types exit → stop app
    if user_input.strip().lower() == "exit":
        st.warning("Session Ended. Thank you for using AI Maths Tutor 🙏")
        st.stop()

    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Add to LLM messages
    st.session_state.messages.append(HumanMessage(content=user_input))

    # Get response
    with st.spinner("Solving..."):
        result = llm.invoke(st.session_state.messages)

    response = result.content

    # Show AI response
    st.chat_message("assistant").markdown(response)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

    # Add AI message to memory
    st.session_state.messages.append(AIMessage(content=response))


# Footer
st.markdown("---")
st.markdown("✨ Developed as a Smart Limited-Line Maths Tutor")