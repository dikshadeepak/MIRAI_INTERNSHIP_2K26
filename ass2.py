import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
import time


st.set_page_config(page_title="MY CHATBOT", page_icon="🤖")

st.markdown("""
<style>
/* Hide Streamlit Header & Footer */
header[data-testid="stHeader"]{
    background:transparent;
    height:0px;
}

footer{
    visibility:hidden;
}

div[data-testid="stToolbar"]{
    display:none;
}
/*optionale
/* Background */
.stApp{
    background-color: black;
    color: white;
}


h1,h2,h3,h4,h5,h6,p,label{
    color: white !important;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background-color:#FF3131;
}

[data-testid="stSidebar"] *{
    color: white !important;
}


.stTextInput input{
    background-color: black !important;
    color: white !important;
    border: 1px solid white !important;
}


.stSelectbox *{
    color: black !important;
}

/* Buttons (SEND + Sidebar buttons) */
.stButton > button{
    background-color: black !important;
    color: white !important;
    border: 1px solid white !important;
}

.stButton > button:hover{
    background-color: black !important;
    color: white !important;
    border: 1px solid white !important;
}

.stButton > button:focus,
.stButton > button:active{
    background-color: black !important;
    color: white !important;
    border: 1px solid white !important;
    box-shadow: none !important;
    outline: none !important;
}

/* Success, Warning, Info messages */
.stSuccess,
.stWarning,
.stInfo{
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

st.title("MY CHATBOT")

# ------------------ Sidebar ------------------
st.sidebar.title("⚙ SELECT PERSONALITY")

personality = st.sidebar.selectbox(
    "WHO IS THE PERSONALITY WE ARE TALKING TO TODAY?",
    [
        "a common indian man who is frustrated by indian government",
        "a crazy Salman Khan fan",
        "a little boy who believes the world is a game that only adults play",
        "a strict school teacher who always gives life lessons",
        "a friendly grandmother who gives caring advice",
        "a sarcastic college student who jokes about everything",
        "a motivational life coach who inspires everyone",
        "a detective who thinks every question is a mystery",
        "a pirate who speaks like a sea captain",
        "a Bollywood movie critic",
        "a stand-up comedian who turns everything into a joke",
        "an excited cricket commentator",
        "a famous chef who compares everything to cooking",
        "a wise monk who answers with calmness and wisdom",
        "a scientist who explains everything logically",
        "a superhero who believes every problem can be solved",
        "an alien visiting Earth for the first time",
        "a time traveler from the year 3000",
        "a history professor who relates everything to historical events",
        "a news reporter giving live updates",
        "a strict job interviewer asking professional questions",
        "a travel guide who describes places beautifully",
        "a fitness trainer who encourages healthy habits",
        "a poet who answers in poetic language",
        "a robot learning human emotions"
    ]
)

# Clear Chat Button
if st.sidebar.button("🧹 CLEAR CHAT"):
    st.session_state.history = []

# ------------------ Gemini ------------------
load_dotenv()

client = genai.Client(api_key=os.getenv("api_key"))

# ------------------ Chat History ------------------
if "history" not in st.session_state:
    st.session_state.history = []

user_message = st.text_input("START THE CONVERSATION:")

# ------------------ Send Button ------------------
if st.button("SEND"):

    if user_message:

        ai_inst = f"""
You are acting as {personality}.

Stay completely in character.

User: {user_message}
"""

        with st.spinner(f"Calling {personality}..."):

            time.sleep(1)      # Response Animation

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=ai_inst
            )

        st.success("Call Picked!")

        st.session_state.history.append(("YOU", user_message))
        st.session_state.history.append(("AI", response.text))

    else:
        st.warning("Enter a message!")

# ------------------ Chat History ------------------
st.subheader("💬 CHAT HISTORY")

for sender, message in st.session_state.history:
    st.write(f"**{sender}:** {message}")

# ------------------ Character Statistics ------------------
st.subheader("📊 CHARACTER STATISTICS")

st.write("Current Personality :", personality)
st.write("Total Messages :", len(st.session_state.history)//2)

# ---------------- FOOTER ----------------
st.markdown("</div>", unsafe_allow_html=True)

st.divider()

st.markdown(
"""
<div class="footer">

### ❤️ Designed & Developed by Diksha Deepak

📡 **Diksha's Signal Station** | Built with **Python + Streamlit**

Thank you for using this application! 🚀

</div>
""",
unsafe_allow_html=True)   
