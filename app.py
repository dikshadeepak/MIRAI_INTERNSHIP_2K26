import streamlit as st
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Diksha's Signal Station",
    page_icon="📡",
    layout="centered",
    initial_sidebar_state="expanded"
)
#-------------css-----------------
st.markdown("""
<style>
/*optional*/

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
/*optionalend*/



/* Reduce top spacing */
.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
}

/* Animated Background */
.stApp{
background:linear-gradient(-45deg,
#ff6b6b,
#feca57,
#48dbfb,
#1dd1a1,
#5f27cd);

background-size:400% 400%;
animation:gradient 15s ease infinite;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}
            
/* Rainbow Sidebar */
section[data-testid="stSidebar"]{
    background: linear-gradient(
        180deg,
        #5f27cd 0%,
        #6a11cb 20%,
        #2575fc 40%,
        #00c9ff 60%,
        #1dd1a1 80%,
        #10ac84 100%
    );
}

/* Sidebar Text */
section[data-testid="stSidebar"] *{
    color: white !important;
}


/* Title */
h1{
    color:white !important;
    text-align:center;
    font-size:42px !important;
    font-weight:bold;
}

/* Text */
p,label,.stMarkdown{
    color:white !important;
}

/* Text Inputs */
.stTextInput input{
    background:white;
    border-radius:12px;
    border:2px solid #4facfe;
    padding:10px;
    color:black;
}

/* Button */
.stButton>button{
    width:100%;
    height:50px;
    background:linear-gradient(90deg,#00c6ff,#0072ff);
    color:white;
    border:none;
    border-radius:12px;
    font-size:20px;
    font-weight:bold;
    transition:.3s;
}

.stButton>button:hover{
    transform:scale(1.02);
    box-shadow:0 0 20px cyan;
}

/* Metric Cards */
div[data-testid="metric-container"]{
    background:rgba(255,255,255,.12);
    border-radius:15px;
    padding:12px;
}

/* Progress Bar */
.stProgress > div > div > div{
    background:#00E5FF;
}

/* Expander */
details{
    background:rgba(255,255,255,.12);
    border-radius:12px;
    padding:12px;
}

details summary{
    color:white !important;
    font-weight:bold;
}

details *{
    color:black !important;
}

/* Footer */
.footer{
    text-align:center;
    color:white;
    font-size:16px;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.title("📡 Signal Station")

    st.success("🟢 System Online")

    st.write("---")

    st.subheader("🚀 Features")

    st.write("✅ Secure Transmission")

    st.write("✅ Token Cost Estimator")

    st.write("✅ Mood Detection")

    st.write("✅ Character Counter")

    st.write("✅ Progress Indicator")

    st.write("✅ Transmission Summary")

    st.write("---")

    st.info("Designed & Developed by\n\n**Diksha Deepak**")

st.markdown('<div class="main-card">', unsafe_allow_html=True)

# ---------------- TASK 1 ----------------
st.title("📡 Diksha's Signal Station")

st.write(
    "Welcome to your personal communication portal. "
    "Enter your details below and securely transmit your message."
)

st.caption(
    "🕒 " + datetime.now().strftime("%d %B %Y | %I:%M %p")
)

# ---------------- TASK 2 ----------------
user_name = st.text_input("👤 Enter Your Name")

user_message = st.text_input("💬 Enter Your Message")

st.caption(f"✍ Characters Typed : {len(user_message)}")

st.progress(min(len(user_message)/200,1.0))
# ---------------- TASK 3 ----------------
if st.button("🚀 Transmit"):

    # ---------------- TASK 4 ----------------
    if user_name.strip() == "":
        st.error("Please provide your name.")

    elif user_message.strip() == "":
        st.warning("Please type a message to transmit.")

    # ---------------- TASK 5 ----------------
    else:

        st.success(
            f"Transmission successful! Greetings, {user_name}. "
            f"We received your message: {user_message}"
        )

        # ---------------- ADVANCED CHALLENGE ----------------
        total_characters = len(user_message)
        token_count = total_characters / 4

        st.info(
            f"System Check: Your message will consume approximately "
            f"{token_count:.2f} tokens from our context window."
        )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="📝 Characters",
                value=total_characters
            )

        with col2:
            st.metric(
                label="🪙 Estimated Tokens",
                value=f"{token_count:.2f}"
            )

        st.divider()

        # ---------------- MESSAGE ANALYSIS ----------------
        positive_words = [
            "happy", "great", "good", "excellent",
            "love", "awesome", "fantastic",
            "wonderful", "nice", "amazing"
        ]

        negative_words = [
            "sad", "bad", "hate", "angry",
            "worst", "terrible", "upset",
            "poor", "boring"
        ]

        message = user_message.lower()

        if any(word in message for word in positive_words):
            st.success("😊 Message Sentiment : Positive")

        elif any(word in message for word in negative_words):
            st.error("😔 Message Sentiment : Negative")

        else:
            st.info("😐 Message Sentiment : Neutral")

        st.divider()

        # ---------------- EXTRA INFORMATION ----------------
        st.subheader("📊 Transmission Statistics")

        st.write(f"👤 **Sender:** {user_name}")
        st.write(f"💬 **Characters:** {total_characters}")
        st.write(f"🪙 **Estimated Tokens:** {token_count:.2f}")
        st.write(
            f"📅 **Transmission Time:** "
            f"{datetime.now().strftime('%d %B %Y | %I:%M:%S %p')}"
        )

        st.progress(min(token_count / 100, 1.0))

        st.divider()

        # ---------------- TRANSMISSION SUMMARY ----------------
        with st.expander("📨 View Transmission Summary"):

            st.markdown("### 📡 Secure Transmission Report")

            st.write(f"**👤 Name:** {user_name}")

            st.write(f"**💬 Message:**")

            st.code(user_message)

            st.write(f"**🔠 Character Count:** {total_characters}")

            st.write(f"**🪙 Estimated Tokens:** {token_count:.2f}")

            st.write(
                f"**🕒 Time:** "
                f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
            )

        st.balloons()

st.divider()

st.subheader("💡 AI Communication Tips")

tips = [
    "✨ Keep your message clear and concise.",
    "📝 Shorter messages consume fewer AI tokens.",
    "🔒 Never include sensitive personal information.",
    "🤖 AI models process text based on token count.",
    "📡 Review your message before transmitting."
]

for tip in tips:
    st.write(tip)

# ---------------- QUICK FACT ----------------
st.info(
    "📚 Did you know?\n\n"
    "Large Language Models (LLMs) don't read text word by word. "
    "Instead, they process text as **tokens**, where approximately "
    "**1 token ≈ 4 characters**."
)

# ---------------- FUN FACT ----------------
with st.expander("🌟 Fun Fact About AI"):
    st.write("""
Artificial Intelligence models like ChatGPT estimate the cost of processing
your input based on the number of tokens. Writing concise prompts not only
improves responses but also reduces computational cost.
""")

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
