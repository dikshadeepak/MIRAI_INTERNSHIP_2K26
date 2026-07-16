import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
import json


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="  AI Visual Novel",
    page_icon="❤️ ",
    layout="wide"
)
st.markdown("""
<style>

/* Main App */
.stApp{
    background: linear-gradient(135deg,#0f172a,#111827,#1e293b);
}

/* Main Title */
.main-title{
    text-align:center;
    color:white;
    font-size:48px;
    font-weight:800;
    margin-top:5px;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:30px;
}

/* Story Card */
.story-box{
    background:#1f2937;
    border-radius:20px;
    padding:25px;
    color:white;
    border:1px solid #374151;
    box-shadow:0px 5px 20px rgba(0,0,0,0.4);
    font-size:18px;
    line-height:1.8;
}

/* Section Headings */
.section-title{
    text-align:center;
    color:#60a5fa;
    font-size:28px;
    font-weight:700;
    margin-top:25px;
    margin-bottom:15px;
}
            /* Welcome Card */

.welcome-box{
    width:70%;
    margin:30px auto;
    background:rgba(31,41,55,0.85);
    border:1px solid #374151;
    border-radius:20px;
    padding:30px;
    text-align:center;
    box-shadow:0 8px 25px rgba(0,0,0,0.45);
    backdrop-filter:blur(8px);
}

.welcome-title{
    color:white;
    font-size:30px;
    font-weight:700;
    margin-bottom:15px;
}

.welcome-text{
    color:#e5e7eb;
    font-size:19px;
    line-height:1.8;
}

/* Buttons */
.stButton>button{
    width:100%;
    border-radius:12px;
    height:52px;
    font-size:18px;
    font-weight:600;
    background:#2563eb;
    color:white;
    border:none;
}

.stButton>button:hover{
    background:#1d4ed8;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#111827;
}

/* Sidebar text */
[data-testid="stSidebar"] *{
    color:white;
}
            [data-testid="stMarkdownContainer"] p {
    color: white !important;
}

/* Selectbox */
.stSelectbox label{
    color:white;
    font-weight:bold;
}
section[data-testid="stSidebar"] *{
    color:white !important;
}
            /* Selected value inside selectbox */
section[data-testid="stSidebar"] div[data-baseweb="select"] span{
    color:black !important;
}

/* Input text */
section[data-testid="stSidebar"] input{
    color:black !important;
}
</style>
""", unsafe_allow_html=True)
# ---------------- LOAD API KEY ----------------
load_dotenv()

API_KEY = os.getenv("API_KEY2")

# ---------------- CACHE GEMINI CLIENT ----------------
@st.cache_resource
def get_client():
    return genai.Client(api_key=API_KEY)

client = get_client()
def generate_story(choice, genre, art_style):
    system_prompt = f"""
You are an AI Visual Novel Engine.

Story Genre: {genre}
Art Style: {art_style}

You MUST return ONLY valid JSON.

Format:

{{
    "story_text":"Narrate the next scene in 120-150 words.",
    "image_prompt":"A detailed prompt for AI image generation describing the scene in {art_style} style.",
    "options":[
        "Option 1",
        "Option 2",
        "Option 3"
    ]
}}

Rules:

- Return ONLY JSON.
- No markdown.
- No explanation.
- Exactly 3 options.
"""

    prompt = system_prompt + "\n\nUser Choice: " + choice

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text

# ---------------- SIDEBAR ----------------
st.sidebar.title("📖 Story Settings")

genre = st.sidebar.selectbox(
    "Choose Story Genre",
    [
        "Fantasy",
        "Sci-Fi",
        "Mystery",
        "Adventure",
        "Horror",
        "Romance"
    ]
)

art_style = st.sidebar.selectbox(
    "Choose Art Style",
    [
        "Anime",
        "Realistic",
        "Pixel Art",
        "Watercolor",
        "Cyberpunk",
        "Disney Style"
    ]
)

start_story = st.sidebar.button("🚀 Start Story")


# ---------------- SESSION STATE ----------------
if "chat" not in st.session_state:
    st.session_state.chat = None

if "story" not in st.session_state:
    st.session_state.story = ""

if "image_prompt" not in st.session_state:
    st.session_state.image_prompt = ""

if "options" not in st.session_state:
    st.session_state.options = []

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- MAIN PAGE ----------------
st.markdown(
    '<div class="main-title">🎮 AI Multi-Modal Visual Novel</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">Create your own AI-powered adventure with dynamic stories, visuals, and narration.</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="subtitle"> ❤️ Developed by Diksha Deepak</div>',

    unsafe_allow_html=True,
)

st.markdown("""
<div class="welcome-box">
        <div class="welcome-title">👋 Welcome!</div>

        Choose your favorite Story Genre and
        Art Style from the sidebar.
        &
        Click the 🚀 Start Story button to begin your
        AI-generated adventure.
    
</div>
""", unsafe_allow_html=True)
if start_story:

    try:

        response = generate_story(
            "Begin the story.",
            genre,
            art_style
        )
        response = response.replace("```json", "").replace("```", "").strip()

        data = json.loads(response)

        st.session_state.story = data["story_text"]

        st.session_state.image_prompt = data["image_prompt"]

        st.session_state.options = data["options"]

    except Exception as e:
     st.error(f"Error: {e}")
     
if st.session_state.story:
       st.markdown(
        '<div class="section-title">📖 Story</div>',
         unsafe_allow_html=True,
       )

       st.markdown(
          f'<div class="story-box">{st.session_state.story}</div>',
        unsafe_allow_html=True,
        )
    

st.markdown(
    '<div class="section-title">🎯 Choose Your Next Move</div>',
    unsafe_allow_html=True,
)
# ---------------- IMAGE ----------------

if st.session_state.image_prompt:

    try:
        import requests

        image_url = (
            "https://image.pollinations.ai/prompt/"
            + requests.utils.quote(st.session_state.image_prompt)
        )

        st.image(image_url, use_container_width=True)

    except Exception:
        st.toast("Image server is busy, skipping visual...")



# ---------------- TEXT TO SPEECH ----------------

try:

    from gtts import gTTS

    audio_file = "story.mp3"

    tts = gTTS(
        text=st.session_state.story,
        lang="en"
    )

    tts.save(audio_file)

    audio = open(audio_file, "rb")

    st.audio(audio.read(), format="audio/mp3")

except Exception:
    st.toast("Audio generation failed.")



# ---------------- DYNAMIC OPTION BUTTONS ----------------

for option in st.session_state.options:

    if st.button(option):

        try:

            response = generate_story(
                option,
                genre,
                art_style
            )

            response = (
                response.replace("```json", "")
                .replace("```", "")
                .strip()
            )

            data = json.loads(response)

            # Save previous scene

            st.session_state.history.append(
                {
                    "story": st.session_state.story,
                    "image_prompt": st.session_state.image_prompt
                }
            )

            # Update current scene

            st.session_state.story = data["story_text"]

            st.session_state.image_prompt = data["image_prompt"]

            st.session_state.options = data["options"]

            st.rerun()

        except Exception as e:

            st.error(f"Error: {e}")



# ---------------- STORY HISTORY ----------------

if st.session_state.history:

    st.divider()

    st.markdown(
    '<div class="section-title">📚 Previous Scenes</div>',
    unsafe_allow_html=True,
)
    for i, scene in enumerate(st.session_state.history, start=1):

        st.markdown(
              f'<h3 style="color:white;">Scene {i}</h3>',
              unsafe_allow_html=True,
        )
        try:

            import requests

            image_url = (
                "https://image.pollinations.ai/prompt/"
                + requests.utils.quote(scene["image_prompt"])
            )

            st.image(image_url, width=400)

        except Exception:
            pass

        st.write(scene["story"])

        st.divider()