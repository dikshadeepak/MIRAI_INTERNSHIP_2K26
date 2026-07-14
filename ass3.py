import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="The Memory Vault Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>

/* Hide Streamlit Branding */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* App Background */
.stApp{
    background: linear-gradient(135deg,#0f172a,#111827,#1e293b);
    color:white;
}

/* Main Container */
.block-container{
    padding-top:2rem;
    max-width:900px;
}

/* Title */
h1{
    text-align:center;
    color:white;
    font-size:46px !important;
    font-weight:800;
}

h2,h3{
    color:white;
}

/* Paragraphs */
p{
    color:#d1d5db;
}

/* Chat Input */
[data-testid="stChatInput"]{
    background:rgba(255,255,255,.06);
    border:1px solid rgba(255,255,255,.15);
    border-radius:16px;
    padding:10px;
    backdrop-filter: blur(20px);
}

/* Chat Input Text */
[data-testid="stChatInput"] textarea{
    color:white !important;
}

/* User Chat Bubble */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]){
    background:linear-gradient(90deg,#2563eb,#1d4ed8);
    border-radius:18px;
    padding:15px;
    margin-bottom:15px;
    box-shadow:0 8px 20px rgba(37,99,235,.25);
}

/* Assistant Bubble */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]){
    background:rgba(255,255,255,.06);
    border:1px solid rgba(255,255,255,.12);
    border-radius:18px;
    padding:15px;
    margin-bottom:15px;
    backdrop-filter:blur(20px);
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#111827,#0f172a,#020617);
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* Buttons */
.stButton>button{
    background:linear-gradient(90deg,#3b82f6,#06b6d4);
    color:white;
    border:none;
    border-radius:12px;
    font-weight:bold;
}

/* Success */
[data-testid="stAlert"]{
    border-radius:12px;
}

/* Scrollbar */
::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-thumb{
    background:#3b82f6;
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)
# ---------------- LOAD GEMINI API ----------------
load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    st.error("❌ API_KEY not found in .env file")
    st.stop()

client = genai.Client(api_key=api_key)
with st.sidebar:

    st.title("🤖 Memory Vault")

    st.success("🟢 Gemini Connected")

    st.divider()

    personality = st.selectbox(
        "Choose Personality",
        [
            "Friendly 😊",
            "Professional 💼",
            "Teacher 📚",
            "Motivator 🚀"
        ]
    )

    st.divider()

    st.info("""
### Assignment 3

✅ Stateful Chatbot

✅ Session State

✅ Gemini API

✅ Chat Memory
""")

    st.divider()

    st.caption("❤️ Developed by Diksha Deepak")

# ---------------- APP TITLE ----------------
st.title("🤖 The Memory Vault Chatbot")



# ======================================================
# TASK 1 : INITIALIZE MEMORY VAULT
# ======================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ======================================================
# TASK 2 : DISPLAY CHAT HISTORY
# ======================================================
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ======================================================
# TASK 3 : CHAT INPUT
# ======================================================
if user_message := st.chat_input("Say something..."):

    # Display User Message
    with st.chat_message("user"):
        st.markdown(user_message)

    # ==================================================
    # TASK 4 : SAVE USER MESSAGE
    # ==================================================
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    # Generate Gemini Response
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message
        )

        ai_response = response.text

    except Exception as e:
        ai_response = f"❌ Error: {e}"

    # Display Assistant Message
    with st.chat_message("assistant"):
        st.markdown(ai_response)

    # ==================================================
    # TASK 4 : SAVE ASSISTANT MESSAGE
    # ==================================================
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )
